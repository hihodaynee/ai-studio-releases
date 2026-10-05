"""Publish checked beta artifacts to GitHub Releases.

Uses Git Credential Manager in memory. Never writes a GitHub token to disk.
Artifacts are immutable once a release is published; use a new version to fix one.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import time

import requests


REPOSITORY = "hihodaynee/ai-studio-releases"
API = f"https://api.github.com/repos/{REPOSITORY}"
HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}


class UploadStream(io.BufferedReader):
    def __init__(self, path: Path):
        super().__init__(io.FileIO(path, "rb"), buffer_size=1024 * 1024)
        self.label = path.name
        self.total = path.stat().st_size
        self.last_report = time.monotonic()

    def read(self, size=-1):
        # HTTP accepts arbitrary non-empty stream blocks. Larger blocks avoid
        # tens of thousands of small TLS writes for the Windows bundle.
        block = super().read(max(size, 1024 * 1024) if size > 0 else size)
        now = time.monotonic()
        if now - self.last_report >= 20 or not block:
            print(json.dumps({"uploading": self.label, "read_bytes": self.tell(),
                              "total_bytes": self.total}), flush=True)
            self.last_report = now
        return block


def credential() -> str:
    result = subprocess.run(["git", "credential", "fill"],
                            input="protocol=https\nhost=github.com\n\n", text=True,
                            capture_output=True, check=True)
    fields = dict(line.split("=", 1) for line in result.stdout.splitlines() if "=" in line)
    token = fields.get("password", "")
    if not token:
        raise RuntimeError("Git Credential Manager has no GitHub credential")
    return token


def checked(response):
    if not 200 <= response.status_code < 300:
        raise RuntimeError(f"GitHub returned HTTP {response.status_code} for {response.request.method} "
                           f"{response.request.url.split('?')[0]}")
    return response.json()


def local_digest(path: Path) -> tuple[int, str]:
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 2_000_000_000:
        raise RuntimeError("Invalid or oversized artifact")
    with path.open("rb") as stream:
        return path.stat().st_size, hashlib.file_digest(stream, "sha256").hexdigest()


def verify_asset(session, asset, expected_size: int, expected_hash: str):
    if asset.get("state") != "uploaded" or asset.get("size") != expected_size:
        raise RuntimeError("GitHub asset is incomplete or has the wrong size")
    if asset.get("digest") == "sha256:" + expected_hash:
        return
    with session.get(asset["url"], headers={"Accept": "application/octet-stream"},
                     stream=True, timeout=(30, 600)) as response:
        response.raise_for_status()
        if "application/json" in response.headers.get("Content-Type", ""):
            raise RuntimeError("GitHub served metadata rather than asset bytes")
        digest, size = hashlib.sha256(), 0
        for block in response.iter_content(1024 * 1024):
            size += len(block)
            if size > expected_size:
                raise RuntimeError("GitHub asset exceeds local size")
            digest.update(block)
    if size != expected_size or digest.hexdigest() != expected_hash:
        raise RuntimeError("GitHub asset does not match local file")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--notes", type=Path, required=True)
    parser.add_argument("--asset", type=Path, action="append", required=True)
    parser.add_argument("--publish", action="store_true", help="Make release public after read-back verification")
    args = parser.parse_args()
    if not args.tag.startswith("v0.1.0-dev.") and args.tag != "update-beta":
        raise RuntimeError("Unexpected beta release tag")
    if len({p.name for p in args.asset}) != len(args.asset):
        raise RuntimeError("Duplicate asset filenames")
    artifacts = {path.name: (path, *local_digest(path)) for path in args.asset}
    notes = args.notes.read_text(encoding="utf-8")
    if len(notes) > 4000:
        raise RuntimeError("Release notes too long")
    session = requests.Session()
    session.headers.update({**HEADERS, "Authorization": "Bearer " + credential()})
    existing = checked(session.get(API + "/releases", params={"per_page": 100}, timeout=30))
    matches = [item for item in existing if item["tag_name"] == args.tag]
    if len(matches) > 1 or matches and not matches[0]["draft"]:
        raise RuntimeError("Release already published; do not replace its assets")
    if matches:
        release = matches[0]
    else:
        release = checked(session.post(API + "/releases", json={"tag_name": args.tag,
            "target_commitish": "main", "name": args.title, "body": notes, "draft": True,
            "prerelease": True, "generate_release_notes": False}, timeout=30))
    upload_url = release["upload_url"].split("{", 1)[0]
    def upload_one(item):
        name, (path, size, digest) = item
        transfer = requests.Session()
        transfer.headers.update(session.headers)
        remote_assets = {item["name"]: item for item in checked(transfer.get(
            release["assets_url"], params={"per_page": 100}, timeout=30))}
        asset = remote_assets.get(name)
        # A broken HTTPS stream can leave a draft-only "starter" asset which
        # blocks a retry under the same filename. Never remove a completed one.
        if asset is not None and asset.get("state") != "uploaded":
            if not release["draft"]:
                raise RuntimeError("Incomplete asset on a published release")
            removal = transfer.delete(asset["url"], timeout=30)
            if removal.status_code != 204:
                raise RuntimeError(f"Cannot remove incomplete draft asset: HTTP {removal.status_code}")
            asset = None
        if asset is None:
            print(json.dumps({"uploading": name, "bytes": size}), flush=True)
            with UploadStream(path) as stream:
                asset = checked(transfer.post(upload_url, params={"name": name}, data=stream,
                    headers={"Content-Type": "application/octet-stream", "Content-Length": str(size)},
                    # requests also uses the connect timeout while writing the
                    # request body. Allow slow/stalled uplinks time to recover.
                    timeout=(300, 3600)))
        verify_asset(transfer, asset, size, digest)
        print(json.dumps({"verified": name, "sha256": digest}), flush=True)
        transfer.close()
    with ThreadPoolExecutor(max_workers=min(2, len(artifacts))) as pool:
        list(pool.map(upload_one, artifacts.items()))
    if args.publish:
        release = checked(session.patch(release["url"], json={"draft": False}, timeout=30))
    print(json.dumps({"tag": args.tag, "draft": release["draft"],
                      "url": release["html_url"]}), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Release publish failed: {type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)

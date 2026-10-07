# Lịch sử phát hành

## 1.0.0 (stable)

- Bản production đầu tiên với tên AI Studio, build từ source mới nhất sau dev.20.
- Sửa phục hồi kết quả gộp SRT từ Gemini và kiểm tra mốc phụ đề; giữ các sửa lỗi giọng đọc, timeline, thumbnail và đồng bộ cảnh.
- Chuyển sang feed cập nhật stable ký Ed25519. Cài đè bằng bộ cài stable một lần khi chuyển từ beta/dev.
- Bổ sung giới hạn log lỗi lặp và dọn diagnostics theo thời hạn cho hệ thống license.
- Kiểm tra EXE, payload bộ cài/gói cập nhật và diễn tập nâng cấp bằng Update.exe thật đạt; giữ dữ liệu và định danh máy trong môi trường thử nghiệm.


# 0.1.0-dev.15 (beta)

- Thử nghiệm thông báo và cài cập nhật từ feed GitHub có chữ ký cho người dùng dev.14.
- Giữ sửa lỗi yêu cầu Project/Brandkit trước khi tạo kịch bản và phân tích ngách YouTube theo từng quốc gia.

# 0.1.0-dev.14 (beta)

- Chặn tạo kịch bản khi chưa có Project hoặc Brandkit hợp lệ; hướng dẫn tạo các mục còn thiếu.
- Phân tích ngách YouTube tách kết quả theo quốc gia được chọn.
- Bổ sung khóa xác minh cập nhật trong ứng dụng Windows.

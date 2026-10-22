# AI Studio — Bản phát hành

Kho phân phối các bản cài đặt và cập nhật AI Studio cho Windows.

Tải [AI Studio 1.2.3 stable](https://github.com/hihodaynee/ai-studio-releases/releases/tag/v1.2.3) cho Windows x64, hoặc [tải trực tiếp bộ cài](https://github.com/hihodaynee/ai-studio-releases/releases/download/v1.2.3/HITechDev.AIStudio.F0-stable-Setup.exe). Dùng tệp `HITechDev.AIStudio.F0-stable-Setup.exe` để cài mới hoặc cài đè bản beta/dev; dữ liệu ứng dụng được giữ lại.

Máy đang dùng các phiên bản trước (1.0.0, 1.0.1, 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.2.0, 1.2.1, 1.2.2) có thể cập nhật trong **Cài đặt → Cập nhật ứng dụng**. Người dùng sẽ thấy thông báo cập nhật trực quan trên giao diện khi có bản mới.

Bản 1.2.3 cải thiện độ tin cậy Gemini, phục hồi tác vụ AI bằng chat mới, chọn đúng model Pro và mức tư duy Trung bình, lưu dần kết quả chủ đề/phụ đề, sửa bước nhân vật và chuẩn hóa thư mục kịch bản Windows. Brandkit giữ bản cũ khi đổi chủ đề; chọn nhân vật chính là tùy chọn trong kết quả, không dừng Auto.

Xem [lịch sử thay đổi](CHANGELOG.md) và ghi chú của từng bản phát hành trước khi cập nhật.

Các mục **Source code (zip/tar.gz)** do GitHub tạo chỉ chứa tài liệu công khai của kho này, không phải bộ cài ứng dụng.

## Quy ước phát hành

- Mỗi phiên bản có ghi chú thay đổi, bộ cài và các tệp kiểm tra/xác thực tương ứng.
- Chỉ công bố sau khi kiểm tra bản cài và cập nhật hoàn tất.
- Mã nguồn phát triển, dữ liệu người dùng và khóa ký không được lưu tại đây.
- Beta/dev theo dõi kênh beta. Chuyển sang stable lần đầu bằng bộ cài stable mới nhất; từ 1.0.0 ứng dụng theo dõi kênh stable có metadata ký Ed25519.
- Bộ cài hiện chưa ký Authenticode. Quy trình 1.2.3 kiểm tra payload Setup/gói cập nhật, smoke runtime, nâng cấp thật bằng Update.exe từ 1.2.2, feed/chữ ký public và trạng thái updater từ 10 phiên bản. Chưa nghiệm thu cài Setup trực tiếp trên Windows sạch; bộ cài chưa ký Authenticode. Tạo ảnh/video cảnh chưa được chạy trong nghiệm thu này.

YouTube Data API key và YouTube Analytics là hai cấu hình riêng. Analytics là tùy chọn và cần nhập cấu hình OAuth Desktop, sau đó cấp quyền kênh. Nhận xét AI từ số liệu Analytics chưa bật trong bản này; vẫn có xem số liệu, đối chiếu SRT và lưu bài học thủ công.

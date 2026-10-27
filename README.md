# AI Studio — Bản phát hành

Kho phân phối các bản cài đặt và cập nhật AI Studio cho Windows.

Tải [AI Studio 1.2.7 stable](https://github.com/hihodaynee/ai-studio-releases/releases/tag/v1.2.7) cho Windows x64, hoặc [tải trực tiếp bộ cài](https://github.com/hihodaynee/ai-studio-releases/releases/download/v1.2.7/HITechDev.AIStudio.F0-stable-Setup.exe). Dùng tệp `HITechDev.AIStudio.F0-stable-Setup.exe` để cài mới hoặc cập nhật; dữ liệu ứng dụng được giữ lại.

Máy đang dùng bản stable trước có thể cập nhật trong **Cài đặt → Cập nhật ứng dụng**. Người dùng sẽ thấy thông báo cập nhật trên giao diện khi có bản mới.

Bản 1.2.7 cải thiện điều phối đúng tài khoản và giữ phiên Gemini/ChatGPT/DeepSeek, đọc mốc reset tải tệp ChatGPT chính xác hơn và tự mở lại điều phối khi đến hạn. Giảm tải tệp lặp lại trên ChatGPT, giữ riêng skill/channel/ảnh, đồng thời sắp xếp lại Cài đặt và trạng thái kết nối. Các kết quả Auto đã hoàn tất và dữ liệu người dùng được giữ lại khi tiếp tục hoặc nâng cấp.

Xem [lịch sử thay đổi](CHANGELOG.md) và ghi chú của từng bản phát hành trước khi cập nhật.

Các mục **Source code (zip/tar.gz)** do GitHub tạo chỉ chứa tài liệu công khai của kho này, không phải bộ cài ứng dụng.

## Quy ước phát hành

- Mỗi phiên bản có ghi chú thay đổi, bộ cài và các tệp kiểm tra/xác thực tương ứng.
- Chỉ công bố sau khi kiểm tra bản đóng gói và cập nhật hoàn tất.
- Mã nguồn phát triển, dữ liệu người dùng và khóa ký không được lưu tại đây.
- Beta/dev theo dõi kênh beta. Chuyển sang stable lần đầu bằng bộ cài stable; từ 1.0.0 ứng dụng theo dõi kênh stable có metadata ký Ed25519.
- Kiểm thử v1.2.7 gồm đối chiếu payload Setup/gói cập nhật, runtime EXE, nâng cấp thật bằng Update.exe từ 1.2.5 và 1.2.6 với dữ liệu thử, migration quota ChatGPT và mở lại điều phối đúng hạn trên EXE. Bộ cài chưa ký Authenticode; chưa chạy Setup trên Windows sạch. Chat web thật được kiểm tra ở source trước đóng gói; QA EXE không gửi AI hay tạo ảnh/video thật.

YouTube Data API key và YouTube Analytics là hai cấu hình riêng. Analytics là tùy chọn, cần cấu hình OAuth Desktop và cấp quyền kênh. Nhận xét AI từ số liệu Analytics chưa bật; vẫn có xem số liệu, đối chiếu SRT và lưu bài học thủ công.

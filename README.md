# AI Studio — Bản phát hành

Kho phân phối các bản cài đặt và cập nhật AI Studio cho Windows.

Tải [AI Studio 1.2.9 stable](https://github.com/hihodaynee/ai-studio-releases/releases/tag/v1.2.9) cho Windows x64, hoặc [tải trực tiếp bộ cài](https://github.com/hihodaynee/ai-studio-releases/releases/download/v1.2.9/HITechDev.AIStudio.F0-stable-Setup.exe). Dùng tệp `HITechDev.AIStudio.F0-stable-Setup.exe` để cài mới hoặc cập nhật; dữ liệu ứng dụng được giữ lại.

Máy đang dùng bản stable trước có thể cập nhật trong **Cài đặt → Cập nhật ứng dụng**. Người dùng sẽ thấy thông báo cập nhật trên giao diện khi có bản mới.

Bản 1.2.9 sửa thao tác gửi DeepSeek và nhận diện ảnh ChatGPT, khôi phục kết quả phân tích đã hoàn tất, thêm lựa chọn Frame video hoặc Thumbnail và cải thiện lấy ảnh từ video dài. Đồng thời cải thiện tạo giọng đọc Google AI Studio, phụ đề DeepSeek và phục hồi cảnh Dola chưa xác nhận.

Xem [lịch sử thay đổi](CHANGELOG.md) và ghi chú của từng bản phát hành trước khi cập nhật.

Các mục **Source code (zip/tar.gz)** do GitHub tạo chỉ chứa tài liệu công khai của kho này, không phải bộ cài ứng dụng.

## Quy ước phát hành

- Mỗi phiên bản có ghi chú thay đổi, bộ cài và các tệp kiểm tra/xác thực tương ứng.
- Chỉ công bố sau khi kiểm tra bản đóng gói và cập nhật hoàn tất.
- Mã nguồn phát triển, dữ liệu người dùng và khóa ký không được lưu tại đây.
- Beta/dev theo dõi kênh beta. Chuyển sang stable lần đầu bằng bộ cài stable; từ 1.0.0 ứng dụng theo dõi kênh stable có metadata ký Ed25519.
- Kiểm thử v1.2.9 gồm đối chiếu payload Setup/gói cập nhật, runtime EXE và nâng cấp thật bằng Update.exe từ 1.2.7 và 1.2.8 với dữ liệu thử. Kiểm tra các module sửa lỗi được đóng gói, hai lựa chọn nguồn ảnh, migration và giữ dữ liệu/cài đặt. Các test theo phạm vi đã đạt; chưa tuyên bố toàn bộ suite repository. Metadata cập nhật ký Ed25519. Bộ cài chưa ký Authenticode; chưa chạy Setup trên Windows sạch. QA EXE không gọi AI hay tạo ảnh/video thật.

YouTube Data API key và YouTube Analytics là hai cấu hình riêng. Analytics là tùy chọn, cần cấu hình OAuth Desktop và cấp quyền kênh. Nhận xét AI từ số liệu Analytics chưa bật; vẫn có xem số liệu, đối chiếu SRT và lưu bài học thủ công.

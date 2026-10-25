# AI Studio — Bản phát hành

Kho phân phối các bản cài đặt và cập nhật AI Studio cho Windows.

Tải [AI Studio 1.2.5 stable](https://github.com/hihodaynee/ai-studio-releases/releases/tag/v1.2.5) cho Windows x64, hoặc [tải trực tiếp bộ cài](https://github.com/hihodaynee/ai-studio-releases/releases/download/v1.2.5/HITechDev.AIStudio.F0-stable-Setup.exe). Dùng tệp `HITechDev.AIStudio.F0-stable-Setup.exe` để cài mới hoặc cài đè bản beta/dev; dữ liệu ứng dụng được giữ lại.

Máy đang dùng các phiên bản trước (1.0.0, 1.0.1, 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.2.4) có thể cập nhật trong **Cài đặt → Cập nhật ứng dụng**. Người dùng sẽ thấy thông báo cập nhật trực quan trên giao diện khi có bản mới.

Bản 1.2.5 cải thiện phiên Gemini Web, trạng thái đăng nhập tài khoản và tiếp tục Auto theo cấu hình đã lưu. Phụ đề Gemini được tự duyệt để không bị chặn bởi bộ lọc độ tin cậy Whisper. Auto mặc định Google AI Studio, Nam Bodi khi nâng cấp; có thể thay đổi trong Cài đặt. Brandkit hỗ trợ thêm/xóa từng ảnh tham chiếu phong cách. Các phần giọng đọc được ghép thành một file trước nhận dạng; ảnh/video đã hoàn tất được giữ khi tiếp tục hoặc đổi công cụ cho phần chưa xong.

Xem [lịch sử thay đổi](CHANGELOG.md) và ghi chú của từng bản phát hành trước khi cập nhật.

Các mục **Source code (zip/tar.gz)** do GitHub tạo chỉ chứa tài liệu công khai của kho này, không phải bộ cài ứng dụng.

## Quy ước phát hành

- Mỗi phiên bản có ghi chú thay đổi, bộ cài và các tệp kiểm tra/xác thực tương ứng.
- Chỉ công bố sau khi kiểm tra bản cài và cập nhật hoàn tất.
- Mã nguồn phát triển, dữ liệu người dùng và khóa ký không được lưu tại đây.
- Beta/dev theo dõi kênh beta. Chuyển sang stable lần đầu bằng bộ cài stable mới nhất; từ 1.0.0 ứng dụng theo dõi kênh stable có metadata ký Ed25519.
- Quy trình 1.2.5 đã kiểm tra payload Setup/gói cập nhật, smoke runtime và nâng cấp thật bằng Update.exe từ 1.2.3 và 1.2.4, giữ dữ liệu thử. Đã kiểm tra cấu hình giọng mặc định chuyển một lần khi nâng cấp và giữ lựa chọn mới của người dùng sau đó. Metadata cập nhật được ký Ed25519. Bộ cài chưa ký Authenticode; chưa nghiệm thu cài Setup trên Windows sạch hoặc gọi Gemini/ChatGPT, tạo ảnh/video thật trong lượt QA đóng gói.

YouTube Data API key và YouTube Analytics là hai cấu hình riêng. Analytics là tùy chọn và cần nhập cấu hình OAuth Desktop, sau đó cấp quyền kênh. Nhận xét AI từ số liệu Analytics chưa bật trong bản này; vẫn có xem số liệu, đối chiếu SRT và lưu bài học thủ công.

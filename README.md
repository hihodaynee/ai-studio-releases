# AI Studio — Bản phát hành

Kho phân phối các bản cài đặt và cập nhật AI Studio cho Windows.

Tải [AI Studio 1.2.8 stable](https://github.com/hihodaynee/ai-studio-releases/releases/tag/v1.2.8) cho Windows x64, hoặc [tải trực tiếp bộ cài](https://github.com/hihodaynee/ai-studio-releases/releases/download/v1.2.8/HITechDev.AIStudio.F0-stable-Setup.exe). Dùng tệp `HITechDev.AIStudio.F0-stable-Setup.exe` để cài mới hoặc cập nhật; dữ liệu ứng dụng được giữ lại.

Máy đang dùng bản stable trước có thể cập nhật trong **Cài đặt → Cập nhật ứng dụng**. Người dùng sẽ thấy thông báo cập nhật trên giao diện khi có bản mới.

Bản 1.2.8 dùng cùng Studio giọng đọc và bộ giọng Manual trong Công cụ nhanh, dừng câu hỏi khám phá khi brief đã sẵn sàng và hỗ trợ tối đa 20 Gemini API key mã hóa để chuyển key khi bị giới hạn. Thêm lựa chọn Flash/Pro cho Gemini Web, cải thiện gửi chat/tệp ChatGPT và đăng nhập DeepSeek, hỗ trợ bản thu tự động dài đến 512 MB. DeepSeek Web được đặt làm mặc định một lần khi nâng cấp; lựa chọn sau đó được giữ.

Xem [lịch sử thay đổi](CHANGELOG.md) và ghi chú của từng bản phát hành trước khi cập nhật.

Các mục **Source code (zip/tar.gz)** do GitHub tạo chỉ chứa tài liệu công khai của kho này, không phải bộ cài ứng dụng.

## Quy ước phát hành

- Mỗi phiên bản có ghi chú thay đổi, bộ cài và các tệp kiểm tra/xác thực tương ứng.
- Chỉ công bố sau khi kiểm tra bản đóng gói và cập nhật hoàn tất.
- Mã nguồn phát triển, dữ liệu người dùng và khóa ký không được lưu tại đây.
- Beta/dev theo dõi kênh beta. Chuyển sang stable lần đầu bằng bộ cài stable; từ 1.0.0 ứng dụng theo dõi kênh stable có metadata ký Ed25519.
- Kiểm thử v1.2.8 gồm đối chiếu payload Setup/gói cập nhật, runtime EXE, nâng cấp thật bằng Update.exe từ 1.2.6 và 1.2.7 với dữ liệu thử, kiểm tra migration mặc định DeepSeek một lần và giữ lựa chọn sau đó trên EXE. 341 kiểm thử backend liên quan và 23 kiểm thử frontend đạt; một test cũ được loại khỏi bộ chọn và có ghi trong báo cáo source. Metadata cập nhật ký Ed25519. Bộ cài chưa ký Authenticode; chưa chạy Setup trên Windows sạch. QA EXE không gọi AI hay tạo ảnh/video thật.

YouTube Data API key và YouTube Analytics là hai cấu hình riêng. Analytics là tùy chọn, cần cấu hình OAuth Desktop và cấp quyền kênh. Nhận xét AI từ số liệu Analytics chưa bật; vẫn có xem số liệu, đối chiếu SRT và lưu bài học thủ công.

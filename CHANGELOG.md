# Lịch sử phát hành

## 1.1.3 (stable)

- Giữ đúng âm lượng video khi xuất CapCut, kể cả mức 0, và cho phép điều chỉnh tiếp trong CapCut.
- Bổ sung phụ đề xuất hiện từng từ hoặc theo nhóm từ; giữ bố cục và cỡ chữ khi xuất CapCut.
- Kiểm tra tài khoản và cấu hình trước khi dùng AI, tạo ảnh/video và phân tích YouTube; thông báo rõ thông tin còn thiếu.
- Gom thay đổi cài đặt vào nút Lưu chung; nút chỉ bật khi có thay đổi và nhắc khi đóng mà chưa lưu.
- Giữ thumbnail và phương án đã chọn sau khi mở lại app; dùng ảnh đã chọn làm bìa kịch bản và bổ sung ảnh tham chiếu nhân vật khi tạo thumbnail.
- Đăng nhập Google nhanh nhận danh sách email/mật khẩu bằng khoảng trắng, tab hoặc dấu |; tiếp tục điền mật khẩu sau CAPTCHA. Xác minh bảo mật của Google vẫn thực hiện trong trình duyệt.
- Đã kiểm tra bản EXE, payload bộ cài/gói cập nhật và nâng cấp bằng Update.exe từ 1.0.0 và 1.1.2, giữ dữ liệu thử.

## 1.1.2 (stable)

- Hiển thị thông báo và nhắc nhở nổi bật khi có phiên bản mới, cho phép cập nhật ngay hoặc bỏ qua.
- Tự động khắc phục lỗi gộp SRT / phụ đề: tích hợp cơ chế căn chỉnh từ Whisper (word alignment fallback) khi AI gián đoạn, cho phép bấm tạo lại thành công.
- Tăng cường độ tin cậy Gemini: biên nhận phản hồi bền vững (durable response receipts), thử lại lũy tiến (exponential backoff) và ngăn chặn trùng lặp yêu cầu.
- Nâng cấp Flow & Composer: hỗ trợ chọn model video Flow; bổ sung điều khiển âm lượng và âm thanh video trong Composer.
- Tối ưu bộ nhớ công cụ nhanh khi tải ảnh tham chiếu từ thư mục.
- Kiểm thử toàn diện nâng cấp tự động từ các phiên bản 1.0.0, 1.0.1 và 1.1.1.

## 1.1.1 (stable)

- Tự phục hồi kết nối kiểm tra và tải cập nhật bằng HTTPS của Windows khi kết nối ban đầu gặp lỗi chứng chỉ hoặc lỗi mạng.
- Giữ xác minh chữ ký thông tin cập nhật, kích thước và hash gói trước khi cài.
- Sửa thao tác kiểm tra cập nhật bị bỏ qua khi trùng với lúc giao diện đọc trạng thái.
- Cho thử lại sau lỗi kết nối trong 5 giây, hiển thị thời gian chờ và thông báo lỗi cụ thể hơn.
- Đã kiểm chứng EXE tự phục hồi lỗi TLS trên Revo mới và nâng cấp cục bộ từ 1.0.0/1.0.1, giữ dữ liệu thử. Bước cài Setup trực tiếp trên Revo được bỏ qua.

## 1.0.1 (stable)

- Giữ bản thu khi chuyển bước trong lúc tạo Voice; tự lưu đúng kịch bản và cho phép thử lại khi lưu lỗi. Đồng bộ lựa chọn giọng đọc sang Phụ đề.
- Tách nhân vật của từng câu chuyện khỏi nhân vật dùng chung của kênh; lưu vào Brandkit cần người dùng xác nhận.
- Phác thảo nhiều nhân vật song song, prompt theo phong cách hình ảnh và mô tả riêng cho vai chính.
- Form Brandkit dùng popup, hỗ trợ JSON và khôi phục ảnh xem trước trong kho mẫu.
- Sửa viết lại bản nháp trong đúng hội thoại; cải thiện YouTube Shorts, chọn thư mục và nhận diện model Flow/Gemini.
- Giữ kênh stable và định danh cài đặt của 1.0.0 để cập nhật tại chỗ.

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

# Lịch sử phát hành

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

# Lịch sử phát hành

## 1.2.6 (stable) — 27/10/2026

- Viết nháp, biên tập và hoàn thiện kịch bản theo từng phần trên Gemini, ChatGPT và DeepSeek Web. Đếm lượng lời kể thực tế, chỉ bổ sung phần thiếu và giữ các phần đã đạt khi thử lại.
- Thêm DeepSeek Web trong Cài đặt Chat AI, đăng nhập bằng profile tài khoản đã lưu; tự giữ DeepThink và Search được bật.
- ChatGPT tự điều phối nhiều tài khoản. Đọc gói Free/Plus từ giao diện; phát hiện hạn mức tải tệp và cho phép dùng lại theo ngày/giờ ChatGPT thông báo.
- Cải thiện đính kèm đủ TXT/skill, nhận câu trả lời hoàn tất và đọc lại đúng kết quả ChatGPT đã gửi. Skill tiếp tục là tệp riêng.
- Dùng Chromium đi kèm app và đúng profile tài khoản. Cải thiện xác nhận sau đăng nhập, hiển thị trạng thái cần thao tác và icon trình duyệt để theo dõi.
- Tạm dừng Auto đóng phiên chat đang chạy và giải phóng tài khoản; có thể xóa kịch bản đã tạm dừng. Bỏ các nút Thêm tài khoản Google và Dừng lượt chạy cũ.
- Tiếp tục video theo provider/model và ảnh đầu vào hiện tại, giữ video đã xong; thông báo phân biệt Google Flow và Dola, hỗ trợ thay ảnh đầu cho cảnh lỗi.

Windows x64. Tải HITechDev.AIStudio.F0-stable-Setup.exe để cài mới hoặc cập nhật. Giữ dữ liệu dự án, tài khoản, Brandkit và các thiết lập đã lưu.

### Kiểm tra phát hành

- 396 kiểm thử backend liên quan, bốn kiểm thử giao diện tài khoản/chat và kiểm tra TypeScript đạt. Kiểm thử công cụ phát hành: 29 ca và 79 kiểm tra con đạt.
- Đối chiếu payload Setup/gói cập nhật, kiểm tra runtime EXE và nâng cấp bằng Update.exe từ 1.2.4/1.2.5, giữ dữ liệu thử. Các migration DeepSeek, chọn ảnh đầu video và lưu phần kịch bản có trong bản đóng gói.
- Kiểm thử chat web thật tại source: draft DeepSeek 8.450 ký tự Nhật (~28:53 cho ca 30 phút), Gemini 548 ký tự (~1:52), ChatGPT 521 ký tự (~1:47 cho ca 2 phút). Đây là thời lượng ước tính; không phải đo TTS. Gemini/GPT được giới hạn thử đến draft theo yêu cầu.
- Metadata cập nhật ký Ed25519. Chưa ký Authenticode hoặc chạy Setup trên Windows sạch; QA EXE không gọi provider thật.

## 1.2.5 (stable) — 25/10/2026

- Cải thiện Gemini Web: giữ phiên và tệp đầu vào, nhận phản hồi hoàn tất, chọn đúng Pro/Tự động và tư duy Trung bình theo tài khoản/cài đặt. Tài khoản mất đăng nhập được hiển thị rõ và không bị thử lặp vô ích.
- Auto đọc lại cấu hình khi tiếp tục, giữ các bước đã hoàn tất và không gửi trùng lượt đã có biên nhận. Dữ liệu AI đi trong TXT, skill được đính kèm riêng.
- Phụ đề: Gemini nhận kịch bản chuẩn và SRT thô để sửa chữ, chia cue. Kết quả SRT được tự duyệt; các kiểm tra độ tin cậy từ Whisper không còn chặn hàng đợi. Giữ nguyên cách chia và mốc thời gian AI trả về.
- Giọng đọc Google AI Studio Web: Nam Bodi/Nữ Fola, chia ở cuối câu với tối đa 8.500 ký tự/phần, chạy theo số luồng đã chọn và ghép thành một file trước nhận dạng lời nói. Khi nâng cấp lần này, mặc định Auto chuyển sang Google AI Studio, Nam Bodi; người dùng vẫn đổi được trong Cài đặt.
- Brandkit: thêm và xóa từng ảnh tham chiếu phong cách, có xác nhận khi xóa; giữ nguyên các kịch bản và tài sản đã lưu.
- Cải thiện Dola/Flow cho ảnh và video: kiểm tra phiên, mode và ảnh đầu, lưu biên nhận, phân biệt từ chối nội dung với lỗi kỹ thuật. Prompt bị từ chối được sửa bằng AI tối đa một lần; nếu vẫn lỗi, hướng dẫn đổi công cụ trong Cài đặt.
- Tiếp tục các phần còn thiếu, giữ ảnh/video/giọng đọc đã xong, timeline và dữ liệu dự án. Hướng dẫn ElevenLabs phân biệt quyền API/Voice Library với lỗi hạn mức.

Windows x64. Tải HITechDev.AIStudio.F0-stable-Setup.exe để cài mới hoặc cập nhật từ bản cũ. Dữ liệu dự án, tài khoản và Brandkit được giữ lại.

### Kiểm tra phát hành

- Đã đối chiếu nội dung Setup/gói cập nhật, kiểm tra runtime đóng gói và nâng cấp thật bằng Update.exe từ 1.2.3 và 1.2.4, giữ dữ liệu thử.
- EXE thật đã kiểm tra cấu hình giọng mặc định chuyển một lần khi nâng cấp và giữ lựa chọn mới sau lần khởi động tiếp theo.
- Giới hạn: bộ cài chưa ký Authenticode; chưa chạy Setup trên Windows sạch. Lượt QA đóng gói không gọi Gemini/ChatGPT hoặc tạo ảnh/video thật.

## 1.2.4 (stable) — 24/10/2026

### Chat AI và tiếp tục tác vụ

- Thêm ChatGPT bằng giao diện web, quản lý tài khoản và giới hạn tải tệp trong Cài đặt. Gemini tiếp tục là nguồn chat AI mặc định.
- Tách dữ liệu đầu vào thành tệp TXT và gửi skill bằng tệp riêng. Khi chat lỗi, lần tiếp theo mở hội thoại mới với các dữ liệu đã lưu.
- Phụ đề và prompt ảnh chạy các phần theo số luồng đã cấu hình, hiển thị tiến độ và giữ các phần hợp lệ khi tiếp tục.

### Quy trình video và giọng đọc

- Quy trình video mới mặc định Auto. Lưu nhân vật chính vào Brandkit là lựa chọn trong kết quả và không dừng hàng đợi.
- Cải thiện nhận dạng lời nói, căn thời gian và tiếp tục tạo phụ đề; giữ kết quả đã hoàn thành.
- Thêm công cụ giọng đọc local trong Công cụ nhanh. Âm thanh chỉ tồn tại trong phiên hiện tại để nghe và tải về; không lưu vào thư viện dự án.
- Cải thiện khởi động lại backend trên Windows và xử lý tên thư mục kịch bản.

### Kiểm tra phát hành

- Đã đối chiếu payload Setup/gói cập nhật, kiểm tra runtime đóng gói và nâng cấp thật bằng Update.exe từ 1.2.2 và 1.2.3, giữ dữ liệu thử.
- Giới hạn: bộ cài chưa ký Authenticode; chưa chạy Setup trên Windows sạch. Lượt QA đóng gói không gọi Gemini/ChatGPT hoặc tạo ảnh/video thật.

## 1.2.3 (stable) — 22/10/2026

### Gemini và phục hồi tác vụ AI

- Khi chat AI lỗi, lượt thử tiếp theo mở hội thoại mới với đầy đủ dữ liệu đã lưu. Kết quả hợp lệ của các bước trước được giữ để tiếp tục.
- Tài khoản Pro chọn model Pro theo tên và phiên bản đang có trong menu, xác nhận mức tư duy Trung bình trước gửi. Thay đổi thứ tự menu không làm app chọn nhầm Flash; nếu không xác định được Pro, app báo lỗi thay vì tự hạ model.
- Sửa trường hợp trình duyệt báo ngắt luồng mạng dù câu trả lời hợp lệ vẫn đang xuất hiện trong chat.
- Gợi ý nhiều chủ đề lưu từng kết quả đã duyệt. Lượt thử mới chỉ làm phần còn thiếu.
- Continue sau khi hết lượt thử ở Nhân vật, Phụ đề và Thumbnail mở một chu kỳ có giới hạn, giữ lịch sử và tổng số lượt đã gửi. Thumbnail tự chọn tài khoản có thể chuyển sang tài khoản Pro khác sau lỗi; lựa chọn tài khoản trực tiếp của người dùng vẫn được giữ.

### Phụ đề và lưu kịch bản trên Windows

- Chỉ dùng tên nhân vật thật sự có trong lời kể để gợi ý nhận dạng giọng đọc, tránh tên dịch ở giao diện làm sai phụ đề tiếng Nhật.
- Phụ đề dài lưu từng phần do AI chia theo mốc Whisper đã đo, rồi kiểm tra toàn bộ lời và thời gian trước khi dùng. Phần đã hợp lệ được giữ khi một phần sau gặp lỗi.
- Tên thư mục kịch bản được chuẩn hóa ngắn, không dấu, dùng dấu gạch nối và xử lý tên dành riêng của Windows. Kịch bản không có ký tự Latin dùng mã ổn định. Tên hiển thị trong app vẫn giữ nguyên; thư mục cũ có nhật ký chuyển đổi để phục hồi.
- Sửa vòng lặp dùng lại phân tích nhân vật đã sai dẫn chứng khi bấm Tiếp tục.

### Brandkit

- Lưu nhân vật chính vào Brandkit là thao tác tùy chọn trong kết quả Nhân vật/Ảnh nhân vật. Người dùng bấm mới mở; thao tác này không dừng queue Auto.
- Thay đổi chủ đề tạo một Brandkit mới dựa trên Brandkit đang chọn và giữ Brandkit gốc.

### Hỗ trợ

- Bổ sung công cụ thu log Gemini dùng được trên máy cài app mà không cần thư mục chẩn đoán cố định ở ổ D. Công cụ chỉ thu dữ liệu chẩn đoán, không gửi yêu cầu AI và loại thông tin xác thực khỏi gói log.

- Đã xác minh hash asset trên GitHub, tải ẩn danh bộ cài/gói cập nhật, feed Ed25519 bằng EXE đóng gói và trạng thái cập nhật cho 10 phiên bản. Nâng cấp thật từ 1.2.2 giữ dữ liệu thử.
- Giới hạn: chưa chạy Setup trên Windows sạch; bộ cài chưa ký Authenticode. Không tạo ảnh/video cảnh hoặc timeline trong lượt nghiệm thu này.

## 1.2.2 (stable) — 19/10/2026

### Giọng đọc ElevenLabs

- Thêm ElevenLabs API bên cạnh Voice Local trong quy trình Auto. Nhập API key và Voice ID, lưu để kiểm tra giọng, model và ngôn ngữ hỗ trợ.
- Kịch bản dài được chia theo giới hạn model và ưu tiên ngắt ở cuối câu. Các phần đã tạo được giữ để tiếp tục; lỗi credit hoặc quyền truy cập có hướng dẫn xử lý cụ thể.
- Thêm nút hướng dẫn tạo API key, bật quyền cần thiết và lấy Voice ID. API key được bảo vệ trên máy.

### Giao diện Việt và Anh

- Chuyển ngôn ngữ ở thanh bên, phía trên nút đổi sáng/tối. Dịch giao diện và nhật ký Auto theo ngôn ngữ đã chọn, giữ nguyên nội dung do người dùng soạn.
- Bản tiếng Việt giữ bảng gói và thanh toán hiện tại. Bản English hiển thị QR và liên hệ Telegram để đối tác ngoài Việt Nam kích hoạt bản quyền.
- Tour làm quen giới thiệu thêm Quy trình video, Gợi ý tiêu đề, Brandkit, YouTube và Công cụ nhanh. Tour tính năng mới giữ các bước cũ và thêm hướng dẫn ElevenLabs.

### Bản quyền và khôi phục

- Tăng bảo vệ chống trùng mã bản quyền, gắn khóa xác thực với định danh thiết bị và chặn dùng lại khóa đã thuộc thiết bị khác.
- Cải thiện lưu và phục hồi khóa máy khi cài lại trên cùng máy và tài khoản Windows. Các trường hợp thay đổi định danh có hướng dẫn kiểm tra, giữ dữ liệu và liên hệ hỗ trợ.
- Kế thừa bản vá v1.2.1: chặn xóa thư mục dự án trùng hoặc lồng với thư mục của dự án khác, giúp bảo vệ tài nguyên đang dùng chung.

Xem lại tour tại **Cài đặt → Cấu hình chung → Hướng dẫn sử dụng**. Trạng thái tour đã xem được giữ khi nâng cấp. ElevenLabs sử dụng hạn mức của tài khoản/API key do bạn cung cấp.

- Đã đối chiếu payload Setup/gói cập nhật và diễn tập nâng cấp bằng Update.exe từ 1.2.0, 1.2.1; giữ dữ liệu mẫu. Metadata cập nhật được ký Ed25519. Bộ cài chưa ký Authenticode.

## 1.2.1 (stable) — 17/10/2026

### Sửa lỗi bảo vệ tài nguyên
- Chặn xóa cả thư mục dự án nếu thư mục đó trùng hoặc lồng với thư mục của dự án khác, tránh xóa nhầm ảnh, video và tài nguyên đang sử dụng.
- Thông báo rõ dự án cần được bảo vệ. Bạn có thể bỏ chọn xóa thư mục để giữ tệp trên ổ đĩa và chỉ xóa dự án khỏi ứng dụng.

### Bao gồm các tính năng mới của v1.2.0
- Thêm quy trình Auto bên cạnh Manual. Auto chuẩn bị kịch bản, nhân vật, giọng đọc, phụ đề, thumbnail và cảnh đến bản dựng; bạn chỉnh sửa rồi tự xuất sang CapCut.
- Theo dõi Auto bằng thanh tiến độ, nhật ký gọn và âm báo lỗi. Tạm dừng, lưu cài đặt và tiếp tục để áp dụng lựa chọn mới cho phần chưa thực hiện.
- Chọn chế độ chỉ ảnh, ảnh xen video hoặc toàn bộ video; thiết lập model ảnh/video và số luồng theo tài khoản khả dụng.
- Thumbnail có ba phương án với ảnh và tiêu đề riêng. Chọn ảnh bìa trong kết quả và giữ lựa chọn khi mở lại.
- Cải thiện gửi/nhận và khôi phục Gemini Web dùng chung cho Auto và Manual, hỗ trợ tài khoản Pro hoặc chỉ có Gemini Tự động. Giữ Gemini Web mặc định, thêm Gemini API bên cạnh DeepSeek.
- Cải thiện khôi phục JSON và xử lý nội dung đa ngôn ngữ; hiệu chỉnh thời lượng kịch bản theo 32 mẫu giọng đọc thực tế.
- Sắp xếp lại Cài đặt và tổng quan Auto; hướng dẫn lần đầu và tính năng mới bằng Product Tour, không lặp lại hướng dẫn đã xem.
- Sửa khởi động lại desktop và khôi phục tác vụ media, giữ kết quả đã hoàn thành khi tiếp tục.

Kịch bản cũ giữ chế độ Manual. Dữ liệu, cài đặt và trạng thái hướng dẫn đã xem được giữ khi nâng cấp. Bản vá không tự phục hồi những tệp đã bị xóa trước đó.

- Đã kiểm tra lớp bảo vệ trên EXE, payload Setup/gói cập nhật và nâng cấp bằng Update.exe từ 1.1.4, 1.2.0, giữ dữ liệu mẫu.

## 1.2.0 (stable) — 17/10/2026

- Thêm quy trình Auto bên cạnh Manual. Auto chuẩn bị kịch bản, nhân vật, giọng đọc, phụ đề, thumbnail và cảnh đến bản dựng; bạn chỉnh sửa rồi tự xuất sang CapCut. Kịch bản cũ giữ chế độ Manual.
- Theo dõi Auto bằng thanh tiến độ, nhật ký gọn và âm báo lỗi. Tạm dừng, lưu cài đặt và tiếp tục để áp dụng lựa chọn mới cho phần chưa thực hiện.
- Chọn chế độ chỉ ảnh, ảnh xen video hoặc toàn bộ video; thiết lập model ảnh/video và số luồng theo tài khoản khả dụng.
- Thumbnail có ba phương án với ảnh và tiêu đề riêng. Chọn ảnh bìa trong kết quả và giữ lựa chọn khi mở lại.
- Cải thiện gửi/nhận và khôi phục Gemini Web dùng chung cho Auto và Manual, hỗ trợ tài khoản Pro hoặc chỉ có Gemini Tự động. Giữ Gemini Web mặc định, thêm Gemini API bên cạnh DeepSeek.
- Cải thiện khôi phục JSON và xử lý nội dung đa ngôn ngữ; hiệu chỉnh thời lượng kịch bản theo 32 mẫu giọng đọc thực tế.
- Sắp xếp lại Cài đặt và tổng quan Auto; hướng dẫn lần đầu và tính năng mới bằng Product Tour, không lặp lại hướng dẫn đã xem.
- Sửa khởi động lại desktop và khôi phục tác vụ media, giữ kết quả đã hoàn thành khi tiếp tục.
- Đã kiểm tra EXE, payload Setup/gói cập nhật và nâng cấp bằng Update.exe từ 1.0.0, 1.1.4, giữ dữ liệu thử.

## 1.1.4 (stable)

- Làm mới YouTube với tìm nguồn theo thị trường/ngôn ngữ/chủ đề/danh mục, lưu nguồn, theo dõi kênh và so sánh nguồn.
- Thêm Kênh của tôi: OAuth Desktop, liên kết video với kịch bản, YouTube Analytics, đối chiếu SRT và bài học để thử trong kịch bản mới.
- Tách hướng dẫn Data API key và Analytics; hỗ trợ nhập file JSON Desktop và cải thiện giao diện báo cáo/tab.
- Thêm ảnh tham chiếu phong cách theo Brandkit, kiểm tra ảnh và dọn khi không còn nơi sử dụng.
- Dọn nguồn phân tích và tệp tạm hết hạn, bảo vệ tài nguyên đang được dùng trong Brandkit/kịch bản.
- Thumbnail chỉ dùng ảnh nhân vật chính; kịch bản chỉ có nhân vật phụ không gửi ảnh tham chiếu.
- Lưu media vào đúng thư mục kịch bản và cải thiện khôi phục ngữ cảnh Gemini.
- Analytics cần cấu hình/cấp quyền riêng. Nhận xét AI từ số liệu Analytics chưa bật; có xem số liệu và lưu bài học thủ công.

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

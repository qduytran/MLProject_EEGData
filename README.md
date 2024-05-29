**Bài tập lớn môn Học máy (INT3405 3)**

Thành viên nhóm
- Trần Quang Duy (21020136)
- Trần Khánh Phương (21020147)
- Đỗ Nguyên Đăng Thi (21020149)
- Đinh Văn Khải (21020444)

Để chạy giao diện
- Đảm bảo cài đặt streamlit: Tutorial (https://www.youtube.com/watch?v=K1GiIgMw6mI)
- Chạy lệnh trên cmd: streamlit run app.py
- Nhập vào thông tin của 19 kênh (việc này nhóm đang muốn cải tiến phù hợp cho thực tế hơn là đọc vào file eeg đo trực tiếp từ não, tất nhiên sẽ thêm nhiều bước hơn)
- Nhấn predict dự đoán (model chạy tốt với tập test độ chính xác khoảng 83%)

Dữ liệu
- Nguồn dữ liệu lấy từ bên Bỉ (private) với 307 bệnh nhân, 178 bệnh nhân không bị bệnh, 129 bệnh nhân bị bệnh
- Feature: với 19 kênh, mỗi kênh có 5 feature, 3 feature của thành phần tuần hoàn, 2 feature của thành phần không tuần hoàn.
- Dữ liệu huấn luyện trên 19 kênh, vậy có 95 trường thông tin cần để cho mô hình học được

Thuật toán (thử nghiệm trong file notebook)
- Hiện tại dùng tuning hyper parameter thì thấy với thuật toán xgboost cho được bộ siêu tham số với độ chính xác trên tập test tốt hơn cả.
<img width="909" alt="image" src="https://github.com/qduytran/MLProject_EEGData/assets/139730440/37b66135-4568-4c77-aab0-fb83df54ab00">

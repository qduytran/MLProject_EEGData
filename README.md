Bài tập lớn môn Học máy (INT3405 3)

Để chạy giao diện:
- Đảm bảo cài đặt streamlit: Tutorial (https://www.youtube.com/watch?v=K1GiIgMw6mI)
- Chạy lệnh trên cmd: streamlit run app.py
- Nhập vào thông tin của 19 kênh (việc này nhóm đang muốn cải tiến phù hợp cho thực tế hơn là đọc vào file eeg đo trực tiếp từ não, tất nhiên sẽ thêm nhiều bước hơn)
- Nhấn predict dự đoán (model chạy tốt với tập test độ chính xác khoảng 83%)

Dữ liệu
- Nguồn dữ liệu lấy từ bên bỉ với 307 bệnh nhân, 178 bệnh nhân không bị bệnh, 129 bệnh nhân bị bệnh
- Feature: với 19 kênh, mỗi kênh có 5 feature, 3 feature của thành phần tuần hoàn, 2 feature của thành phần không tuần hoàn.
- Dữ liệu huấn luyện trên 19 kênh, vậy có 95 trường thông tin cần để cho mô hình học được

Thuật toán (thử nghiệm trong file notebook)
- Hiện tại dùng tuning hyper parameter thì thấy với thuật toán xgboost cho được bộ siêu tham số với độ chính xác trên tập test tốt hơn cả.
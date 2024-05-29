# **Bài tập lớn môn Học máy (INT3405 3)**

> ***Thành viên nhóm***
> 
> 1. Trần Quang Duy (21020136)
> 2. Trần Khánh Phương (21020147)
> 3. Đỗ Nguyên Đăng Thi (21020149)


|     Họ và tên      |   MSV    | Đóng góp |
|:------------------:|:--------:|:--------:|
|   Trần Quang Duy   | 21020136 |   40%   |
| Đỗ Nguyên Đăng Thi |   21020149   |   20%   |
| Trần Khánh Phương  |   21020147   |   20%   |
|   Đinh Văn Khải    |   21020444   |   20%   |

***Các bước cài đặt để chạy giao diện người dùng***

1. Đảm bảo cài đặt streamlit: [Tutorial](https://www.youtube.com/watch?v=K1GiIgMw6mI)
2. Chạy lệnh trên cmd: streamlit run app.py
3. Nhập vào thông tin của 19 kênh (việc này nhóm đang muốn cải tiến phù hợp cho thực tế hơn là đọc vào file eeg đo trực tiếp từ não, tất nhiên sẽ thêm nhiều bước hơn)
4. Nhấn predict dự đoán (model chạy tốt với tập test độ chính xác khoảng 83%)

***Dữ liệu và mô hình***

* Nguồn dữ liệu lấy từ bên Bỉ (private) với 307 bệnh nhân, 178 bệnh nhân không bị bệnh, 129 bệnh nhân bị bệnh
* Feature: với 19 kênh, mỗi kênh có 5 feature, 3 feature của thành phần tuần hoàn, 2 feature của thành phần không tuần hoàn.
* Dữ liệu huấn luyện trên 19 kênh, vậy có 95 trường thông tin cần để cho mô hình học được
* Thuật toán (thử nghiệm trong file notebook)
* Hiện tại dùng tuning hyper parameter thì thấy với thuật toán xgboost cho được bộ siêu tham số với độ chính xác trên tập test tốt hơn cả.
![image](https://github.com/qduytran/MLProject_EEGData/assets/139730440/9c8fdaf3-b482-4dbe-a1f9-c9a9a5e1ddb4)

****

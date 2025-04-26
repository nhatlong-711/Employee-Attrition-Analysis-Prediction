# I. Phân tích và Dự đoán Tỷ lệ nghỉ việc của nhân viên bằng Python (Employee Attrition Analysis & Prediction)

## Mô tả

Dự án nhằm phân tích dữ liệu nhân sự để hiểu rõ các yếu tố ảnh hưởng đến việc nghỉ việc của nhân viên, đồng thời xây dựng mô hình học máy dự đoán khả năng nghỉ việc (Attrition) dựa trên các đặc điểm của từng cá nhân.

Dữ liệu sử dụng từ tập `HR-Employee.csv` bao gồm 1470 mẫu và 35 cột đặc trưng.

---

##  Mục tiêu

- Phân tích dữ liệu khám phá (EDA) để tìm hiểu các yếu tố ảnh hưởng đến nghỉ việc
- Xây dựng mô hình học máy dự đoán khả năng nghỉ việc của nhân viên
- Đánh giá hiệu quả mô hình và rút ra insight từ dữ liệu

---

## Các bước thực hiện

### 1. Tiền xử lý dữ liệu
- Đọc file Excel với định dạng đặc biệt (delimiter = `;`)
- Chuyển cột mục tiêu `Attrition` thành nhị phân: Yes = 1, No = 0
- Encode các biến phân loại dùng `LabelEncoder`
- Chia dữ liệu thành tập huấn luyện và kiểm tra (80-20)

### 2. Phân tích dữ liệu (EDA)
- Phân tích mối quan hệ giữa Attrition với:
  - OverTime (Tăng ca)
  - JobSatisfaction (Mức độ hài lòng)
  - MonthlyIncome (Thu nhập)
  - Age (Tuổi)
  - Department (Phòng ban)
  - YearsAtCompany (Số năm làm việc)
- Trực quan hóa bằng biểu đồ: Countplot, Boxplot, Heatmap,...

### 3. Huấn luyện mô hình
- Mô hình sử dụng: **Logistic Regression**
- Cân bằng lớp bằng `class_weight='balanced'`
- Đánh giá mô hình qua:
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-score)
  - Accuracy Score

---

## Kết quả đạt được

- Mô hình Logistic Regression đạt độ chính xác khoảng **~85%**
- Một số insight rút ra từ dữ liệu:
  - Nhân viên làm tăng ca có xu hướng nghỉ việc nhiều hơn
  - Nhân viên có mức hài lòng công việc thấp hoặc thu nhập thấp cũng dễ nghỉ việc hơn
  - Các phòng ban khác nhau có tỷ lệ nghỉ việc khác nhau
  - Số năm làm việc ít → dễ nghỉ hơn

---

## Kỹ thuật sử dụng

- Python (Pandas, Seaborn, Scikit-learn, Matplotlib)
- Logistic Regression
- Label Encoding
- Train/Test Split
- Class Imbalance Handling

---

## Hướng phát triển tiếp theo

- Tối ưu mô hình bằng Random Forest, XGBoost
- Ứng dụng kỹ thuật SMOTE để cân bằng tập dữ liệu
- Xây dựng dashboard trực quan bằng Power BI

---



# II. HR Dashboard Power BI Project
## Mô tả dự án
Dashboard phân tích dữ liệu nhân sự được xây dựng bằng Power BI, dựa trên file dữ liệu HR-Employee.csv. Dashboard tập trung vào các yếu tố như tỷ lệ nghỉ việc, sự hài lòng công việc, tổng thu nhập và làm việc ngoài giờ.

### Các bước thực hiện
1. Tải dữ liệu

Sử dụng tính năng Get Data → Text/CSV để tải file HR-Employee.csv.

Chọn dấu phân cách là Semicolon (;) và Load dữ liệu.

2. Xử lý dữ liệu

Kiểm tra và chỉnh đúng kiểu dữ liệu cho các cột (số, văn bản, ngày tháng).

3. Xây dựng biểu đồ

Donut Chart: Phân tích tỷ lệ nghỉ việc (Attrition) theo số lượng nhân viên (EmployeeNumber).

Column Chart: Phân tích mức độ hài lòng công việc (JobSatisfaction).

Stacked Bar Chart: Tổng thu nhập trung bình theo phòng ban (MonthlyIncome - Department).

Line and Column Chart: Phân tích mức độ đào tạo và thăng chức (TrainingTimesLastYear và YearsSinceLastPromotion).

Donut Chart thêm: Phân tích tỷ lệ làm việc ngoài giờ (OverTime).

4. Tùy chỉnh giao diện

Thêm slicer cho các trường Gender, Department, EducationField.

Căn chỉnh, bo góc biểu đồ, đặt tiêu đề rõ ràng cho từng biểu đồ.

Sử dụng màu sắc đồng nhất và thân thiện.

5. Lưu dashboard

Lưu dưới dạng .pbix hoặc xuất ra file PDF.

*** Ghi chú
Tất cả biểu đồ đều hiển thị dữ liệu theo tỷ lệ phần trăm và số lượng để tăng độ trực quan.

Dashboard hỗ trợ bộ lọc đa chiều, giúp phân tích chi tiết theo phòng ban, giới tính và trình độ học vấn.

Thực hiện bởi: Hoang Phuc Nhat Long
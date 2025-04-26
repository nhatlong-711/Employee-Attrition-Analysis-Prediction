# Phân tích và Dự đoán Tỷ lệ nghỉ việc của nhân viên (Employee Attrition Analysis & Prediction)

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

Thực hiện bởi: Hoang Phuc Nhat Long


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data from file Excel
df = pd.read_csv('D:\STUDY\HR-Employee\HR-Employee.csv',delimiter=';')
df_info = df.info()
df_head = df.head()
df_shape = df.shape
df_describe = df.describe(include='all')
df_shape, df_head, df_describe

import matplotlib.pyplot as plt
import seaborn as sns

# Sao chép DataFrame để xử lý
df_ml = df.copy()

# Chuyển cột mục tiêu 'Attrition' thành nhị phân: Yes=1, No=0
df_ml['Attrition'] = df_ml['Attrition'].map({'Yes': 1, 'No': 0})

# Kiểm tra tỷ lệ nghỉ việc
attrition_rate = df_ml['Attrition'].value_counts(normalize=True)

# Biểu đồ tỷ lệ nghỉ việc
plt.figure(figsize=(6, 4))
sns.countplot(x='Attrition', data=df_ml)
plt.title('Tỷ lệ nghỉ việc của nhân viên')
plt.xticks([0, 1], ['Không nghỉ', 'Nghỉ việc'])
plt.ylabel('Số lượng')
plt.xlabel('Tình trạng nghỉ việc')
plt.tight_layout()
plt.show()

attrition_rate

sns.countplot(x='OverTime', hue='Attrition', data=df)
plt.title('Nghỉ việc theo OverTime')
plt.show()
sns.countplot(x='JobSatisfaction', hue='Attrition', data=df)
plt.title('Attrition theo mức độ hài lòng công việc')
plt.show()

sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title('Phân bố thu nhập theo tình trạng nghỉ việc')
plt.show()

sns.histplot(data=df, x='Age', hue='Attrition', multiple='stack')
plt.title('Phân bố tuổi theo nghỉ việc')
plt.show()

dept_attrition = df.groupby('Department')['Attrition'].value_counts(normalize=True).unstack().fillna(0)
dept_attrition.plot(kind='bar', stacked=True)
plt.title('Tỷ lệ nghỉ việc theo phòng ban')
plt.ylabel('Tỷ lệ')
plt.show()

sns.boxplot(x='Attrition', y='YearsAtCompany', data=df)
plt.title('Số năm làm việc theo nghỉ việc')
plt.show()

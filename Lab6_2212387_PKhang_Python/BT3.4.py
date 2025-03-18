import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"
df = pd.read_csv(file_path)

# Giả sử dữ liệu có cột 'Tháng', 'Sữa rửa mặt', 'Kem dưỡng da mặt'
months = df['month_number']
face_wash_sales = df['facewash']
moisturizer_sales = df['facecream']

# Vẽ biểu đồ tán xạ
plt.figure(figsize=(8, 6))
plt.scatter(months, face_wash_sales, color='green', label='Sữa rửa mặt')
plt.scatter(months, moisturizer_sales, color='magenta', label='Kem dưỡng da mặt')

# Cài đặt tiêu đề và nhãn
plt.title("Số lượng bán của sữa rửa mặt và kem dưỡng da mặt theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Số lượng bán")
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

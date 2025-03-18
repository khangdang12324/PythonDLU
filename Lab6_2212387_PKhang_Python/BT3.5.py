import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn file đã tải lên
df = pd.read_csv(file_path)

# Vẽ biểu đồ cột
plt.figure(figsize=(8, 6))
plt.bar(df["month_number"], df["bathingsoap"], color='pink', edgecolor='black')

# Cài đặt tiêu đề và nhãn
plt.title("Số lượng bán của xà bông tắm theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Số lượng bán")
plt.xticks(df["month_number"])  # Hiển thị tất cả các tháng trên trục x
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Đường lưới ngang

# Hiển thị biểu đồ
plt.show()
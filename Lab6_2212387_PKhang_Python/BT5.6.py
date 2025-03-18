import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn đến file CSV đã tải lên
df = pd.read_csv(file_path)

# Lấy dữ liệu cột cần thiết
months = df["month_number"]
facewash = df["facewash"]
moisturizer = df["moisturizer"]

# Thiết lập vị trí các cột
x = np.arange(len(months))  # Tạo vị trí cho từng tháng
width = 0.4  # Độ rộng của mỗi cột

# Vẽ biểu đồ
plt.figure(figsize=(8,6))
plt.bar(x - width/2, moisturizer, width, color="green", label="Kem dưỡng da mặt")
plt.bar(x + width/2, facewash, width, color="brown", label="Sữa rửa mặt")

# Thiết lập nhãn và tiêu đề
plt.xlabel("Tháng")
plt.ylabel("Số lượng bán")
plt.title("So sánh số lượng bán của sữa rửa mặt và kem dưỡng da mặt theo tháng")
plt.xticks(x, months)  # Hiển thị tháng trên trục x
plt.legend()

# Hiển thị biểu đồ
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

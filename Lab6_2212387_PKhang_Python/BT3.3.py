import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn file đã tải lên
df = pd.read_csv(file_path)

# Lấy danh sách các tháng
monthList = df["month_number"].tolist()

# Vẽ biểu đồ đường cho từng sản phẩm
plt.figure(figsize=(10, 6))

plt.plot(monthList, df["facecream"], marker='o', label="Face cream")
plt.plot(monthList, df["facewash"], marker='o', label="Face Wash")
plt.plot(monthList, df["toothpaste"], marker='o', label="ToothPaste")
plt.plot(monthList, df["bathingsoap"], marker='o', label="BathingSoap")
plt.plot(monthList, df["shampoo"], marker='o', label="Shampoo")
plt.plot(monthList, df["moisturizer"], marker='o', label="Moisturizer")

# Thêm tiêu đề và nhãn
plt.xlabel("Tháng")
plt.ylabel("Số lượng bán")
plt.title("Số lượng bán của từng sản phẩm")
plt.xticks(monthList)
plt.legend()  # Hiển thị chú thích
plt.grid(True)  

# Hiển thị biểu đồ
plt.show()

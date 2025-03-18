import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn đến file CSV đã tải lên
df = pd.read_csv(file_path)

# Lấy tổng số lượng bán của từng loại sản phẩm
product_sales = {
    "FaceWash": df["facewash"].sum(),
    "FaceCream": df["facecream"].sum(),
    "Moisturizer": df["moisturizer"].sum(),
    "Shampoo": df["shampoo"].sum(),
    "Bathing soap": df["bathingsoap"].sum(),
    "ToothPaste": df["toothpaste"].sum()
}

# Lấy danh sách sản phẩm và giá trị bán
labels = product_sales.keys()
sizes = product_sales.values()

# Danh sách màu sắc cho từng phần của biểu đồ
colors = ["orange", "blue", "brown", "purple", "red", "green"]

# Vẽ biểu đồ tròn
plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)

# Tiêu đề biểu đồ
plt.title("Thống kê mặt hàng đã bán năm 2021")

# Hiển thị biểu đồ
plt.show()

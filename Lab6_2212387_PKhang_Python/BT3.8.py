import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn đến file CSV đã tải lên
df = pd.read_csv(file_path)

# Lọc dữ liệu cho tháng 3 (giả sử cột "month" lưu giá trị tháng)
df_march = df[df["month_number"] == 3]

# Tính tổng số lượng bán của từng sản phẩm trong tháng 3
product_sales_march = {
    "FaceWash": df_march["facewash"].sum(),
    "FaceCream": df_march["facecream"].sum(),
    "Moisturizer": df_march["moisturizer"].sum(),
    "Shampoo": df_march["shampoo"].sum(),
    "Bathing soap": df_march["bathingsoap"].sum(),
    "ToothPaste": df_march["toothpaste"].sum()
}

# Lấy danh sách sản phẩm và số lượng bán tương ứng
labels = product_sales_march.keys()
sizes = product_sales_march.values()

# Danh sách màu sắc cho từng phần của biểu đồ
colors = ["orange", "blue", "brown", "purple", "red", "green"]

# Vẽ biểu đồ tròn
plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)

# Tiêu đề biểu đồ
plt.title("Thống kê mặt hàng đã bán tháng 3 năm 2021")

# Hiển thị biểu đồ
plt.show()

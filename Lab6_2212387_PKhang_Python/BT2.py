
import pandas as pd

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn file đã tải lên
df = pd.read_csv(file_path)

# 1) Hiển thị thông tin dữ liệu
print("🔹 Thông tin dữ liệu:")
print(df.info())  # Thông tin về số cột, kiểu dữ liệu, giá trị null

# 2) Hiển thị nội dung toàn bộ dữ liệu
print("\n🔸 Nội dung dữ liệu:")
print(df)

# 3) Xuất hàng có lợi nhuận cao nhất
max_profit_row = df[df["total_profit"] == df["total_profit"].max()]
print("\n🔹 Hàng có lợi nhuận cao nhất:")
print(max_profit_row)

# 4) Xuất hàng của tháng bán nhiều mặt hàng nhất
max_units_row = df[df["total_units"] == df["total_units"].max()]
print("\n🔸 Hàng của tháng bán nhiều mặt hàng nhất:")
print(max_units_row)

# 5) Xuất hàng bán nhiều kem đánh răng nhất
max_toothpaste_row = df[df["toothpaste"] == df["toothpaste"].max()]
print("\n🔹 Hàng bán nhiều kem đánh răng nhất:")
print(max_toothpaste_row)

# 6) Tổng lợi nhuận cả năm
total_profit_year = df["total_profit"].sum()
print("\n💰 Tổng lợi nhuận cả năm:", total_profit_year)

# 7) Tổng số lượng đã bán theo từng mặt hàng
total_units_each = df.drop(columns=["month_number", "total_units", "total_profit"]).sum()
print("\n📊 Tổng số lượng từng mặt hàng đã bán trong năm:")
print(total_units_each)

# 8) Số lượng các mặt hàng bán trong tháng 2
february_data = df[df["month_number"] == 2]
print("\n🔹 Dữ liệu tháng 2:")
print(february_data)

# 9) Mặt hàng bán chạy nhất tháng 2
best_seller_feb = february_data.drop(columns=["month_number", "total_units", "total_profit"]).max(axis=1).values[0]
print("\n🔥 Mặt hàng bán chạy nhất tháng 2:", best_seller_feb)

# 10) Mặt hàng bán chạy nhất trong năm
best_seller_year = total_units_each.idxmax()
print("\n🏆 Mặt hàng bán chạy nhất trong năm:", best_seller_year)

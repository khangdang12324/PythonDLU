import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
file_path = "E:\Python\Lab6_2212387_PKhang_Python\sales_data.csv"  # Đường dẫn file đã tải lên
df = pd.read_csv(file_path)

# Lấy danh sách lợi nhuận và số tháng
profitList = df["total_profit"].tolist()
monthList = df["month_number"].tolist()

# Vẽ biểu đồ đường
plt.figure("Biểu đồ đoạn thẳng")
plt.plot(monthList, profitList, marker='o', linestyle='--', color='green', linewidth=2)  
plt.xlabel("Tháng")
plt.ylabel("Lợi nhuận ($)")
plt.xticks(monthList)
plt.yticks(range(100000, 600000, 100000))  
plt.title("Lợi nhuận hàng tháng năm 2021")
plt.grid(True)  
plt.show()
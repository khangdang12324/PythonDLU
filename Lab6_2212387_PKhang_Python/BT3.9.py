import matplotlib.pyplot as plt

# Dữ liệu số lượng bán theo tháng
months = list(range(1, 13))  # 12 tháng
bathing_soap_sales = [8500, 6200, 9100, 8700, 8200, 7800, 8600, 9200, 8900, 10300, 12000, 14000]
facewash_sales = [5500, 6000, 5300, 4700, 4200, 4000, 4500, 4800, 5100, 4900, 3000, 2500]

# Tạo 2 biểu đồ con (subplot)
fig, axes = plt.subplots(2, 1, figsize=(8, 6))

# Biểu đồ 1: Số lượng xà bông tắm đã bán
axes[0].plot(months, bathing_soap_sales, marker='o', linestyle='-', color='green')
axes[0].set_title("Số lượng xà bông tắm đã bán", color='green')
axes[0].grid(True)

# Biểu đồ 2: Số lượng sữa rửa mặt đã bán
axes[1].plot(months, facewash_sales, marker='o', linestyle='-', color='red')
axes[1].set_title("Số lượng sữa rửa mặt đã bán", color='red')
axes[1].set_xlabel("Tháng")
axes[1].set_ylabel("Số lượng")
axes[1].grid(True)

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()

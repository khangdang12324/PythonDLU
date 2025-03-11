# 1. Khai báo một List chứa 10 số nguyên
dsSoNguyen = [5, 12, 7, 9, 3, 15, 20, 8, 11, 6]
print("1. Danh sách ban đầu:")
print(dsSoNguyen)
print("")

# 2. Xuất tất cả các số lẻ không chia hết cho 5
dsSoLeKoChiaCho5 = [x for x in dsSoNguyen if (x % 2 != 0) and (x % 5 != 0)]
print("2. Các số lẻ không chia hết cho 5:")
print(dsSoLeKoChiaCho5)
print("")

# 3. Xuất 10 số Fibonacci đầu tiên
print("3. 10 số Fibonacci đầu tiên:")
n = 10  # Số lượng số Fibonacci muốn in ra
a, b = 0, 1  # Khởi tạo 2 số đầu tiên của dãy Fibonacci
fibo = []
for i in range(n):
    fibo.append(a)
    a, b = b, a + b
print(fibo)
print("")

# 4. Tìm số Fibonacci bé nhất (lớn hơn 0) trong dãy trên
# (Trong dãy Fibonacci trên, số bé nhất > 0 là 1)
fibo_nonzero = [x for x in fibo if x > 0]
min_fibo = min(fibo_nonzero) if fibo_nonzero else None
print("4. Số Fibonacci bé nhất (> 0):")
print(min_fibo)
print("")

# 5. Tính trung bình các số lẻ trong dsSoNguyen
dsSoLe = [x for x in dsSoNguyen if x % 2 != 0]
if dsSoLe:
    trung_binh_so_le = sum(dsSoLe) / len(dsSoLe)
else:
    trung_binh_so_le = 0
print("5. Trung bình các số lẻ:")
print(trung_binh_so_le)
print("")

# 6. Tính tích các phần tử là số lẻ không chia hết cho 3 trong dsSoNguyen
dsSoLeKhongChia3 = [x for x in dsSoNguyen if (x % 2 != 0) and (x % 3 != 0)]
tich = 1
for num in dsSoLeKhongChia3:
    tich *= num
print("6. Tích các số lẻ không chia hết cho 3:")
print(tich)
print("")

# 7. Đổi chỗ 2 phần tử của dsSoNguyen, đầu vào là 2 vị trí cần đổi chỗ
# Ví dụ: đổi vị trí index 1 và index 3
index1, index2 = 1, 3
dsSoNguyen[index1], dsSoNguyen[index2] = dsSoNguyen[index2], dsSoNguyen[index1]
print("7. Danh sách sau khi đổi chỗ phần tử tại vị trí", index1, "và", index2, ":")
print(dsSoNguyen)
print("")

# 8. Đảo ngược trật tự các phần tử của dsSoNguyen
dsSoNguyenDaoNguoc = dsSoNguyen[::-1]
print("8. Danh sách đảo ngược:")
print(dsSoNguyenDaoNguoc)
print("")

# 9. Xuất tất cả các số lớn thứ nhì của dsSoNguyen
# Ta tìm số lớn thứ hai từ các phần tử duy nhất
unique_numbers = list(set(dsSoNguyen))
if len(unique_numbers) >= 2:
    unique_numbers.sort()
    second_largest = unique_numbers[-2]
    print("9. Số lớn thứ nhì:")
    print(second_largest)
else:
    print("9. Không đủ số để xác định số lớn thứ nhì")
print("")

# 10. Tính tổng các chữ số của tất cả các số trong dsSoNguyen
def sum_digits(n):
    # Hàm tính tổng các chữ số của số n (hỗ trợ số âm)
    return sum(int(digit) for digit in str(abs(n)))

tong_chu_so = sum(sum_digits(x) for x in dsSoNguyen)
print("10. Tổng các chữ số của tất cả các số trong danh sách:")
print(tong_chu_so)
print("")

# 11. Đếm số lần xuất hiện của một số trong dsSoNguyen
# Giả sử: đếm số lần xuất hiện của số 15
so_can_dem = 15
so_lan_xuat_hien = dsSoNguyen.count(so_can_dem)
print("11. Số lần xuất hiện của số", so_can_dem, "trong danh sách:")
print(so_lan_xuat_hien)
print("")

# 12. Xuất các số xuất hiện n lần trong dsSoNguyen
# Giả sử: tìm các số xuất hiện đúng 1 lần
n_occurrence = 1
so_xuat_hien_n_lan = [x for x in set(dsSoNguyen) if dsSoNguyen.count(x) == n_occurrence]
print("12. Các số xuất hiện đúng", n_occurrence, "lần:")
print(so_xuat_hien_n_lan)
print("")

# 13. Xuất các số xuất hiện nhiều lần nhất trong dsSoNguyen
max_occurrence = max(dsSoNguyen.count(x) for x in set(dsSoNguyen))
so_xuat_hien_nhieu_nhat = [x for x in set(dsSoNguyen) if dsSoNguyen.count(x) == max_occurrence]
print("13. Các số xuất hiện nhiều nhất (", max_occurrence, "lần):", sep="")
print(so_xuat_hien_nhieu_nhat)
print("")

# Lưu ý: Các bài tập từ 9 đến 13 được đánh số theo thứ tự yêu cầu của bạn.

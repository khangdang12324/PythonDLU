import math

###############################################
# Bài 3: Cài đặt lớp Phân Số
###############################################

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu số phải khác 0")
        # Đưa về dạng mẫu số dương
        if mau < 0:
            tu, mau = -tu, -mau
        self.tu = tu
        self.mau = mau
        self.rut_gon()
    
    def rut_gon(self):
        """Rút gọn phân số dựa trên ước chung lớn nhất."""
        gcd = math.gcd(self.tu, self.mau)
        if gcd != 0:
            self.tu //= gcd
            self.mau //= gcd
        return self

    # Ghi đè toán tử cộng
    def __add__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    
    # Ghi đè toán tử trừ
    def __sub__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    
    # Ghi đè toán tử nhân
    def __mul__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    
    # Ghi đè toán tử chia
    def __truediv__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử số bằng 0")
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau)
    
    # Để so sánh hai phân số (đã được rút gọn)
    def __eq__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu == other.tu and self.mau == other.mau

    # Dùng để so sánh theo giá trị thực của phân số (cho sắp xếp)
    def __lt__(self, other):
        if not isinstance(other, PhanSo):
            return NotImplemented
        return self.tu * other.mau < other.tu * self.mau

    def value(self):
        """Trả về giá trị thực của phân số."""
        return self.tu / self.mau

    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
    def __repr__(self):
        return self.__str__()

# --- Kiểm thử Bài 3 ---
ps1 = PhanSo(2, 4)    # rút gọn thành 1/2
ps2 = PhanSo(3, 6)    # rút gọn thành 1/2

print("Bài 3: Lớp PhanSo")
print("PhanSo 1:", ps1)                  # 1/2
print("PhanSo 2:", ps2)                  # 1/2
print("Cộng:", ps1 + ps2)                # 1/2 + 1/2 = 1/1
print("Trừ:", ps1 - ps2)                 # 1/2 - 1/2 = 0/1
print("Nhân:", ps1 * ps2)                # 1/2 * 1/2 = 1/4
print("Chia:", ps1 / ps2)                # 1/2 / 1/2 = 1/1

###############################################
# Bài 4: Cài đặt lớp Danh Sách Phân Số
###############################################

class DanhSachPhanSo:
    def __init__(self):
        self.ds = []  # danh sách các đối tượng PhanSo
    
    def them_phan_so(self, ps):
        if isinstance(ps, PhanSo):
            self.ds.append(ps)
        else:
            raise ValueError("Phải thêm đối tượng kiểu PhanSo")
    
    def hien_thi(self):
        for i, ps in enumerate(self.ds):
            print(f"Vị trí {i}: {ps}")
    
    # 1. Đếm số phân số âm trong mảng
    def dem_phan_so_am(self):
        return sum(1 for ps in self.ds if ps.value() < 0)
    
    # 2. Tìm phân số dương nhỏ nhất
    def tim_phan_so_duong_nho_nhat(self):
        positives = [ps for ps in self.ds if ps.value() > 0]
        if positives:
            return min(positives, key=lambda ps: ps.value())
        else:
            return None
    
    # 3. Tìm tất cả vị trí của phân số x trong mảng
    def tim_vi_tri_phan_so(self, x):
        # x: đối tượng PhanSo cần tìm
        positions = []
        for i, ps in enumerate(self.ds):
            if ps == x:
                positions.append(i)
        return positions
    
    # 4. Tổng tất cả các phân số âm trong mảng
    def tong_phan_so_am(self):
        negatives = [ps for ps in self.ds if ps.value() < 0]
        if not negatives:
            return None
        result = negatives[0]
        for ps in negatives[1:]:
            result = result + ps
        return result
    
    # 5. Xóa phân số x trong mảng (xóa lần xuất hiện đầu tiên)
    def xoa_phan_so(self, x):
        for i, ps in enumerate(self.ds):
            if ps == x:
                del self.ds[i]
                return True
        return False
    
    # 6. Xóa tất cả phân số có tử là x
    def xoa_tat_ca_phan_so_co_tu(self, x):
        self.ds = [ps for ps in self.ds if ps.tu != x]
    
    # 7. Sắp xếp phân số theo:
    #    a) Giá trị (tăng hoặc giảm)
    def sap_xep_theo_gia_tri(self, tang=True):
        self.ds.sort(key=lambda ps: ps.value(), reverse=not tang)
    
    #    b) Theo mẫu rồi tử (tăng theo mẫu, tử; giảm theo mẫu, tử)
    def sap_xep_theo_mau_tu(self, tang=True):
        # Sắp xếp theo (mẫu, tử) theo thứ tự tăng nếu tang=True, ngược lại giảm.
        self.ds.sort(key=lambda ps: (ps.mau, ps.tu), reverse=not tang)
    
    def get_ds(self):
        return self.ds

# --- Kiểm thử Bài 4 ---
ds_ps = DanhSachPhanSo()

# Thêm một số phân số (có cả số dương và âm)
ds_ps.them_phan_so(PhanSo(1, 2))    # 1/2
ds_ps.them_phan_so(PhanSo(-3, 4))   # -3/4
ds_ps.them_phan_so(PhanSo(2, 3))    # 2/3
ds_ps.them_phan_so(PhanSo(-1, 3))   # -1/3
ds_ps.them_phan_so(PhanSo(5, 10))   # rút gọn thành 1/2
ds_ps.them_phan_so(PhanSo(3, -6))   # rút gọn thành -1/2
ds_ps.them_phan_so(PhanSo(2, 5))    # 2/5

print("\nDanh sách phân số ban đầu:")
ds_ps.hien_thi()

# 1. Đếm số phân số âm
print("\nSố phân số âm:", ds_ps.dem_phan_so_am())

# 2. Tìm phân số dương nhỏ nhất
ps_duong_nho_nhat = ds_ps.tim_phan_so_duong_nho_nhat()
print("Phân số dương nhỏ nhất:", ps_duong_nho_nhat)

# 3. Tìm tất cả vị trí của phân số 1/2 (sau rút gọn)
ps_can_tim = PhanSo(1, 2)
positions = ds_ps.tim_vi_tri_phan_so(ps_can_tim)
print("Vị trí của phân số", ps_can_tim, "trong danh sách:", positions)

# 4. Tổng tất cả các phân số âm
tong_am = ds_ps.tong_phan_so_am()
print("Tổng các phân số âm:", tong_am)

# 5. Xóa phân số 2/3 (chỉ xóa lần xuất hiện đầu tiên)
ps_xoa = PhanSo(2, 3)
ket_qua_xoa = ds_ps.xoa_phan_so(ps_xoa)
print("Xóa phân số", ps_xoa, ":", ket_qua_xoa)
print("Danh sách sau khi xóa:")
ds_ps.hien_thi()

# 6. Xóa tất cả các phân số có tử là 1 (ví dụ: xóa các phân số có tử = 1)
ds_ps.xoa_tat_ca_phan_so_co_tu(1)
print("\nDanh sách sau khi xóa tất cả các phân số có tử = 1:")
ds_ps.hien_thi()

# 7. Sắp xếp phân số:
# a) Theo giá trị tăng dần
ds_ps.sap_xep_theo_gia_tri(tang=True)
print("\nDanh sách sau sắp xếp theo giá trị (tăng dần):")
ds_ps.hien_thi()

# b) Theo giá trị giảm dần
ds_ps.sap_xep_theo_gia_tri(tang=False)
print("\nDanh sách sau sắp xếp theo giá trị (giảm dần):")
ds_ps.hien_thi()

# c) Theo mẫu rồi tử (tăng dần)
ds_ps.sap_xep_theo_mau_tu(tang=True)
print("\nDanh sách sau sắp xếp theo mẫu, tử (tăng dần):")
ds_ps.hien_thi()

# d) Theo mẫu rồi tử (giảm dần)
ds_ps.sap_xep_theo_mau_tu(tang=False)
print("\nDanh sách sau sắp xếp theo mẫu, tử (giảm dần):")
ds_ps.hien_thi()

# File: sinh_vien.py
import datetime

class SinhVien:
    def __init__(self, ma_sv, ho_ten, ngay_sinh, diem_ren_luyen, trinh_do=None):
        """
        :param ma_sv: Mã sinh viên (int)
        :param ho_ten: Họ tên (str)
        :param ngay_sinh: Ngày sinh (datetime.date)
        :param diem_ren_luyen: Điểm rèn luyện (float)
        :param trinh_do: Trình độ (str): có thể là "chinh quy" hoặc "cao dang"
        """
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.diem_ren_luyen = diem_ren_luyen
        self.trinh_do = trinh_do

    def __str__(self):
        return (f"MaSV: {self.ma_sv}, HoTen: {self.ho_ten}, NgaySinh: {self.ngay_sinh}, "
                f"DiemRenLuyen: {self.diem_ren_luyen}, TrinhDo: {self.trinh_do}")

# File: sinh_vien_chinh_quy.py
# Lớp SinhVienChinhQuy kế thừa từ SinhVien, có thêm thuộc tính điểm học tập.
class SinhVienChinhQuy(SinhVien):
    def __init__(self, ma_sv, ho_ten, ngay_sinh, diem_ren_luyen, diem_hoc_tap):
        # Gán trinh_do là "chinh quy"
        super().__init__(ma_sv, ho_ten, ngay_sinh, diem_ren_luyen, trinh_do="chinh quy")
        self.diem_hoc_tap = diem_hoc_tap

    def __str__(self):
        return super().__str__() + f", DiemHocTap: {self.diem_hoc_tap}"

# File: sv_phi_chinh_quy.py
# Lớp SinhVienPhiCQ kế thừa từ SinhVien, có thêm thuộc tính số tín chỉ.
# Theo đề bài, sinh viên phi CQ được xem là có trình độ "cao dang".
class SinhVienPhiCQ(SinhVien):
    def __init__(self, ma_sv, ho_ten, ngay_sinh, diem_ren_luyen, so_tin_chi):
        # Gán trinh_do là "cao dang"
        super().__init__(ma_sv, ho_ten, ngay_sinh, diem_ren_luyen, trinh_do="cao dang")
        self.so_tin_chi = so_tin_chi

    def __str__(self):
        return super().__str__() + f", SoTinChi: {self.so_tin_chi}"

# File: danh_sach_sinh_vien.py
# Lớp DanhSachSinhVien chứa danh sách các đối tượng SinhVien và các phương thức xử lý.
class DanhSachSinhVien:
    def __init__(self):
        self.ds = []  # danh sách các đối tượng SinhVien

    def them_sinh_vien(self, sv):
        self.ds.append(sv)

    def xuat_sinh_vien(self):
        for sv in self.ds:
            print(sv)

    # 1. Tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def tim_sv_diem_ren_luyen_cao(self):
        return [sv for sv in self.ds if sv.diem_ren_luyen >= 80]

    # 2. Tìm sinh viên có trình độ cao đẳng (trinh_do == "cao dang")
    #    và sinh trước ngày 15/8/1999
    def tim_sv_cao_dang_sinh_truoc(self):
        ngay_chuan = datetime.date(1999, 8, 15)
        return [sv for sv in self.ds if sv.trinh_do == "cao dang" and sv.ngay_sinh < ngay_chuan]

# File: main.py
# File main để tạo danh sách sinh viên và kiểm tra các hàm.
def main():
    ds_sv = DanhSachSinhVien()

    # Tạo một số đối tượng SinhVienChinhQuy (chính quy)
    sv1 = SinhVienChinhQuy(1001, "Nguyen Van A", datetime.date(1998, 5, 10), 85, 8.5)
    sv2 = SinhVienChinhQuy(1002, "Le Thi B", datetime.date(2000, 3, 22), 75, 7.0)

    # Tạo một số đối tượng SinhVienPhiCQ (phi chính quy, trình độ cao đẳng)
    sv3 = SinhVienPhiCQ(2001, "Tran Van C", datetime.date(1997, 12, 1), 90, 32)
    sv4 = SinhVienPhiCQ(2002, "Pham Thi D", datetime.date(2000, 10, 5), 65, 28)
    sv5 = SinhVienPhiCQ(2003, "Do Van E", datetime.date(1999, 1, 15), 80, 30)

    # Thêm sinh viên vào danh sách
    ds_sv.them_sinh_vien(sv1)
    ds_sv.them_sinh_vien(sv2)
    ds_sv.them_sinh_vien(sv3)
    ds_sv.them_sinh_vien(sv4)
    ds_sv.them_sinh_vien(sv5)

    print("Danh sách sinh viên:")
    ds_sv.xuat_sinh_vien()

    print("\nSinh viên có điểm rèn luyện từ 80 trở lên:")
    for sv in ds_sv.tim_sv_diem_ren_luyen_cao():
        print(sv)

    print("\nSinh viên có trình độ cao đẳng sinh trước 15/8/1999:")
    for sv in ds_sv.tim_sv_cao_dang_sinh_truoc():
        print(sv)

if __name__ == "__main__":
    main()

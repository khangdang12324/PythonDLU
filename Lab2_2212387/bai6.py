import math

# ---------------------------
# Định nghĩa các lớp Hình Học
# ---------------------------
class HinhHoc:
    def tinh_dien_tich(self):
        raise NotImplementedError("Phương thức tinh_dien_tich() phải được ghi đè trong lớp con.")

    def loai_hinh(self):
        raise NotImplementedError("Phương thức loai_hinh() phải được ghi đè trong lớp con.")

    def __str__(self):
        return f"{self.loai_hinh()} - Diện tích: {self.tinh_dien_tich():.2f}"


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)

    def loai_hinh(self):
        return "HinhTron"

    def __str__(self):
        return f"HinhTron (bán kính: {self.ban_kinh}) - Diện tích: {self.tinh_dien_tich():.2f}"


class HinhChuNhat(HinhHoc):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def loai_hinh(self):
        return "HinhChuNhat"

    def __str__(self):
        return f"HinhChuNhat (dài: {self.chieu_dai}, rộng: {self.chieu_rong}) - Diện tích: {self.tinh_dien_tich():.2f}"


# ---------------------------
# Lớp DanhSachHinhHoc
# ---------------------------
class DanhSachHinhHoc:
    def __init__(self):
        self.ds = []  # Danh sách các đối tượng HinhHoc

    def themHinh(self, hh: HinhHoc):
        self.ds.append(hh)

    def xuat(self):
        for i, hh in enumerate(self.ds):
            print(f"Vị trí {i}: {hh}")

    def timHinhCoDienTichLonNhat(self) -> 'DanhSachHinhHoc':
        result = DanhSachHinhHoc()
        if not self.ds:
            return result
        max_area = max(hh.tinh_dien_tich() for hh in self.ds)
        for hh in self.ds:
            if abs(hh.tinh_dien_tich() - max_area) < 1e-9:
                result.themHinh(hh)
        return result

    def timHinhCoDienTichNhoNhat(self) -> 'DanhSachHinhHoc':
        result = DanhSachHinhHoc()
        if not self.ds:
            return result
        min_area = min(hh.tinh_dien_tich() for hh in self.ds)
        for hh in self.ds:
            if abs(hh.tinh_dien_tich() - min_area) < 1e-9:
                result.themHinh(hh)
        return result

    def TimHinhTronNhoNhat(self) -> 'DanhSachHinhHoc':
        result = DanhSachHinhHoc()
        # Lọc ra tất cả các hình tròn
        circles = [hh for hh in self.ds if hh.loai_hinh() == "HinhTron"]
        if not circles:
            return result
        min_area = min(hh.tinh_dien_tich() for hh in circles)
        for hh in circles:
            if abs(hh.tinh_dien_tich() - min_area) < 1e-9:
                result.themHinh(hh)
        return result

    def SapGiamTheoDienTich(self):
        self.ds.sort(key=lambda hh: hh.tinh_dien_tich(), reverse=True)

    def DemSoLuongHinh(self, kieu: str) -> int:
        return sum(1 for hh in self.ds if hh.loai_hinh() == kieu)

    def TinhTongDienTich(self) -> float:
        return sum(hh.tinh_dien_tich() for hh in self.ds)

    def timHinhCoDienTichLonNhat_theoLoai(self, kieu: str) -> 'DanhSachHinhHoc':
        result = DanhSachHinhHoc()
        filtered = [hh for hh in self.ds if hh.loai_hinh() == kieu]
        if not filtered:
            return result
        max_area = max(h.tinh_dien_tich() for h in filtered)
        for hh in filtered:
            if abs(hh.tinh_dien_tich() - max_area) < 1e-9:
                result.themHinh(hh)
        return result

    def TimViTriCuaHinh(self, h: HinhHoc) -> int:
        # So sánh dựa trên diện tích và loại hình, 
        # hoặc bạn có thể ghi đè __eq__ trong từng lớp
        for i, hh in enumerate(self.ds):
            if (type(hh) == type(h) and 
                abs(hh.tinh_dien_tich() - h.tinh_dien_tich()) < 1e-9):
                return i
        return -1

    def XoaTaiViTri(self, viTri: int) -> bool:
        if 0 <= viTri < len(self.ds):
            del self.ds[viTri]
            return True
        return False

    def TimHinhTheoDTich(self, dt: float) -> 'DanhSachHinhHoc':
        result = DanhSachHinhHoc()
        for hh in self.ds:
            if abs(hh.tinh_dien_tich() - dt) < 1e-9:
                result.themHinh(hh)
        return result

    def XoaHinh(self, hh: HinhHoc) -> bool:
        for i, h in enumerate(self.ds):
            # Kiểm tra loại hình và diện tích (hoặc ghi đè __eq__ cho chính xác)
            if (type(h) == type(hh) and 
                abs(h.tinh_dien_tich() - hh.tinh_dien_tich()) < 1e-9):
                del self.ds[i]
                return True
        return False

    def XoaHinhTheoLoai(self, kieu: str):
        self.ds = [hh for hh in self.ds if hh.loai_hinh() != kieu]

    def XuatHinhTheoChieuTangGiam(self, kieu: str, tang: bool):
        filtered = [hh for hh in self.ds if hh.loai_hinh() == kieu]
        filtered.sort(key=lambda hh: hh.tinh_dien_tich(), reverse=not tang)
        for hh in filtered:
            print(hh)

    def TinhTongDTTheoKieuHinh(self, kieu: str) -> float:
        return sum(hh.tinh_dien_tich() for hh in self.ds if hh.loai_hinh() == kieu)


# ---------------------------
# Hàm main() để chạy kiểm thử
# ---------------------------
def main():
    ds = DanhSachHinhHoc()
    # Thêm một số hình
    ds.themHinh(HinhTron(5))          # Diện tích ≈ 78.54
    ds.themHinh(HinhTron(3))          # Diện tích ≈ 28.27
    ds.themHinh(HinhChuNhat(4, 5))    # Diện tích = 20
    ds.themHinh(HinhChuNhat(6, 7))    # Diện tích = 42
    ds.themHinh(HinhTron(7))          # Diện tích ≈ 153.94

    print("Danh sách các hình:")
    ds.xuat()

    print("\nHình có diện tích lớn nhất:")
    ds_max = ds.timHinhCoDienTichLonNhat()
    ds_max.xuat()

    print("\nHình có diện tích nhỏ nhất:")
    ds_min = ds.timHinhCoDienTichNhoNhat()
    ds_min.xuat()

    print("\nHình tròn nhỏ nhất:")
    ds_tron_nho = ds.TimHinhTronNhoNhat()
    ds_tron_nho.xuat()

    print("\nDanh sách sau khi sắp giảm theo diện tích:")
    ds.SapGiamTheoDienTich()
    ds.xuat()

    print("\nSố lượng hình tròn:", ds.DemSoLuongHinh("HinhTron"))
    print("Số lượng hình chữ nhật:", ds.DemSoLuongHinh("HinhChuNhat"))

    print("\nTổng diện tích của các hình:", ds.TinhTongDienTich())

    print("\nHình có diện tích lớn nhất trong số các hình tròn:")
    ds_max_tron = ds.timHinhCoDienTichLonNhat_theoLoai("HinhTron")
    ds_max_tron.xuat()

    # Tìm vị trí của một hình (ví dụ: HinhChuNhat(4, 5))
    test_hinh = HinhChuNhat(4, 5)
    print("\nVị trí của hình", test_hinh, ":", ds.TimViTriCuaHinh(test_hinh))

    print("\nTìm hình theo diện tích 42:")
    ds_tim = ds.TimHinhTheoDTich(42)
    ds_tim.xuat()

    print("\nXóa hình HinhTron(3):", ds.XoaHinh(HinhTron(3)))
    print("Danh sách sau khi xóa:")
    ds.xuat()

    print("\nXóa tất cả hình chữ nhật:")
    ds.XoaHinhTheoLoai("HinhChuNhat")
    ds.xuat()

    print("\nXuất hình tròn theo chiều tăng (theo diện tích):")
    ds.XuatHinhTheoChieuTangGiam("HinhTron", tang=True)

    print("\nTổng diện tích các hình tròn:", ds.TinhTongDTTheoKieuHinh("HinhTron"))


# ---------------------------
# Chạy chương trình
# ---------------------------
if __name__ == "__main__":
    main()

import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime)-> None:
        self.__maSo = maSo 
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @property
    def hoTen(self):
        return self.__hoTen
    
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso))== 7
    
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    
    def __str__(self)-> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print (f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    def timVTSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    def XoaSvTheoMssv(self, maSo : int)->bool:
        vt = self.timSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSVTheoTem(self,ten: str):
        pass

    def timSvSinhTruocNgay(self, ngay:datetime):
        pass
    def sapXepTheoTen(self, giamDan = False):
        self.dssv.sort(key = lambda sv: sv.hoTen, reverse =giamDan)

    def docTuFile(self, filename):
     with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                # Phần đầu là maSo, phần cuối là ngày sinh, phần giữa nối lại thành họ tên
                maSo = int(parts[0])
                ngaySinh_str = parts[-1]
                hoTen = " ".join(parts[1:-1])
                # Chuyển đổi ngày sinh theo định dạng dd/mm/yyyy
                ngaySinh = datetime.datetime.strptime(ngaySinh_str, "%d/%m/%Y").date()
                # Tạo đối tượng SinhVien và thêm vào danh sách
                self.themSinhVien(SinhVien(maSo, hoTen, ngaySinh))


ds = DanhSachSv()
ds.docTuFile(r"E:\Python\lab2_2212387_PKhang_Python\Lab2_2212387\dssv.txt")

ds.sapXepTheoTen(giamDan = False)

print("\n DS dam dan:")

ds.xuat()

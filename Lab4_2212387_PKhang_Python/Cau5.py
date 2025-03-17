import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime
import openpyxl
from openpyxl import Workbook
import os

class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Đăng ký học phần")
        self.geometry("550x450")
        self.configure(bg="#33ff33")

        # Tiêu đề lớn
        lbl_title = tk.Label(self, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN",
                             font=("Arial", 14, "bold"), fg="red", bg="#33ff33")
        lbl_title.place(x=150, y=10)

        # ============= Khung nhập liệu =============
        # Mã số sinh viên
        tk.Label(self, text="Mã số sinh viên", bg="#33ff33").place(x=20, y=60)
        self.var_mssv = tk.StringVar()
        self.entry_mssv = tk.Entry(self, textvariable=self.var_mssv)
        self.entry_mssv.place(x=160, y=60, width=200)

        # Họ tên
        tk.Label(self, text="Họ tên", bg="#33ff33").place(x=20, y=90)
        self.var_name = tk.StringVar()
        tk.Entry(self, textvariable=self.var_name).place(x=160, y=90, width=200)

        # Ngày sinh
        tk.Label(self, text="Ngày sinh", bg="#33ff33").place(x=20, y=120)
        self.var_dob = tk.StringVar()
        tk.Entry(self, textvariable=self.var_dob).place(x=160, y=120, width=200)

        # Email
        tk.Label(self, text="Email", bg="#33ff33").place(x=20, y=150)
        self.var_email = tk.StringVar()
        tk.Entry(self, textvariable=self.var_email).place(x=160, y=150, width=200)

        # Số điện thoại
        tk.Label(self, text="Số điện thoại", bg="#33ff33").place(x=20, y=180)
        self.var_phone = tk.StringVar()
        tk.Entry(self, textvariable=self.var_phone).place(x=160, y=180, width=200)

        # Học kỳ
        tk.Label(self, text="Học kỳ", bg="#33ff33").place(x=20, y=210)
        self.var_hocky = tk.StringVar()
        tk.Entry(self, textvariable=self.var_hocky).place(x=160, y=210, width=200)

        # Năm học (combobox)
        tk.Label(self, text="Năm học", bg="#33ff33").place(x=20, y=240)
        self.var_namhoc = tk.StringVar()
        combo_namhoc = ttk.Combobox(self, textvariable=self.var_namhoc,
                                    values=["2022-2023","2023-2024","2024-2025"])
        combo_namhoc.place(x=160, y=240, width=200)
        combo_namhoc.current(0)

        # ============= Chọn môn học =============
        tk.Label(self, text="Chọn môn học", bg="#33ff33").place(x=20, y=270)

        self.var_mon_python = tk.BooleanVar()
        tk.Checkbutton(self, text="Lập trình Python",
                       variable=self.var_mon_python, bg="#33ff33").place(x=160, y=270)

        self.var_mon_java = tk.BooleanVar()
        tk.Checkbutton(self, text="Lập trình Java",
                       variable=self.var_mon_java, bg="#33ff33").place(x=160, y=295)

        self.var_mon_cnpm = tk.BooleanVar()
        tk.Checkbutton(self, text="Công nghệ phần mềm",
                       variable=self.var_mon_cnpm, bg="#33ff33").place(x=320, y=270)

        self.var_mon_web = tk.BooleanVar()
        tk.Checkbutton(self, text="Phát triển ứng dụng web",
                       variable=self.var_mon_web, bg="#33ff33").place(x=320, y=295)

        # ============= Nút =============
        btn_dangky = tk.Button(self, text="Đăng ký", width=10, command=self.handle_dangky)
        btn_dangky.place(x=200, y=350)

        btn_thoat = tk.Button(self, text="Thoát", width=10, command=self.quit)
        btn_thoat.place(x=300, y=350)

    # ============= Hàm kiểm tra và lưu Excel =============
    def handle_dangky(self):
        mssv = self.var_mssv.get().strip()
        name = self.var_name.get().strip()
        dob = self.var_dob.get().strip()
        email = self.var_email.get().strip()
        phone = self.var_phone.get().strip()
        hocky = self.var_hocky.get().strip()
        namhoc = self.var_namhoc.get()

        # Môn học
        mon_list = []
        if self.var_mon_python.get():
            mon_list.append("Lập trình Python")
        if self.var_mon_java.get():
            mon_list.append("Lập trình Java")
        if self.var_mon_cnpm.get():
            mon_list.append("Công nghệ phần mềm")
        if self.var_mon_web.get():
            mon_list.append("Phát triển ứng dụng web")

        # 1) Mã số sinh viên: chỉ cho nhập số, đủ 7 số
        if not (mssv.isdigit() and len(mssv) == 7):
            messagebox.showwarning("Cảnh báo", "Mã số sinh viên phải gồm 7 chữ số!")
            return

        # 2) Kiểm tra email hợp lệ (regex)
        pattern_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern_email, email):
            messagebox.showwarning("Cảnh báo", "Email không hợp lệ!")
            return

        # 3) Số điện thoại: chỉ nhập số, 10 số
        if not (phone.isdigit() and len(phone) == 10):
            messagebox.showwarning("Cảnh báo", "Số điện thoại phải gồm 10 chữ số!")
            return

        # 4) Học kỳ: 1, 2 hoặc 3
        if hocky not in ["1", "2", "3"]:
            messagebox.showwarning("Cảnh báo", "Học kỳ chỉ được nhập 1, 2 hoặc 3!")
            return

        # 5) Kiểm tra định dạng ngày sinh dd/mm/yyyy (regex)
        pattern_dob = r'^\d{2}/\d{2}/\d{4}$'
        if not re.match(pattern_dob, dob):
            messagebox.showwarning("Cảnh báo", "Ngày sinh phải định dạng dd/mm/yyyy!")
            return

        # Kiểm tra có nhập đủ thông tin tên, v.v. chưa
        if not name:
            messagebox.showwarning("Cảnh báo", "Họ tên không được để trống!")
            return

        # 6) Năm học: có thể chọn từ 3 giá trị
        # Đã kiểm tra khi khởi tạo combobox, nên không cần check

        # 7) Đã chọn môn học nào chưa
        if not mon_list:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn môn học nào!")
            return

        # Lưu vào file Excel
        self.save_to_excel(mssv, name, dob, email, phone, hocky, namhoc, mon_list)

        messagebox.showinfo("Thông báo", "Đăng ký thành công!")

    def save_to_excel(self, mssv, name, dob, email, phone, hocky, namhoc, mon_list):
        filename = "dangky.xlsx"

        # Nếu file chưa tồn tại, tạo workbook mới
        if not os.path.exists(filename):
            import openpyxl
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "DangKy"
            # Tạo tiêu đề cột
            ws.append(["MSSV", "Họ tên", "Ngày sinh", "Email", "Số ĐT", "Học kỳ", "Năm học", "Môn học"])
            wb.save(filename)

        # Mở file excel
        import openpyxl
        wb = openpyxl.load_workbook(filename)
        ws = wb.active

        # Mỗi môn học -> 1 dòng
        for mon in mon_list:
            ws.append([mssv, name, dob, email, phone, hocky, namhoc, mon])

        wb.save(filename)

if __name__ == "__main__":
    app = RegistrationForm()
    app.mainloop()

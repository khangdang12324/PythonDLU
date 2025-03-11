import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []  # Danh sách công việc

        self.create_widgets()

    def create_widgets(self):
        # Khung chứa Entry và nút thêm công việc
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.add_button = tk.Button(self.entry_frame, text="Thêm Công Việc", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Listbox hiển thị danh sách công việc kèm Scrollbar
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack()

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(self.list_frame, width=50, height=10, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Khung chứa các nút: Sửa, Xoá, Lưu và Tải danh sách
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.edit_button = tk.Button(self.button_frame, text="Sửa Công Việc", command=self.edit_task)
        self.edit_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Xoá Công Việc", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Lưu Công Việc", command=self.save_tasks)
        self.save_button.grid(row=0, column=2, padx=5)

        self.load_button = tk.Button(self.button_frame, text="Tải Công Việc", command=self.load_tasks)
        self.load_button.grid(row=0, column=3, padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Cảnh báo", "Bạn chưa nhập công việc nào.")

    def edit_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            current_task = self.tasks[index]
            new_task = simpledialog.askstring("Sửa Công Việc", "Sửa nội dung công việc:", initialvalue=current_task)
            if new_task:
                self.tasks[index] = new_task.strip()
                self.update_listbox()
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn công việc cần sửa.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn công việc cần xoá.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", 
            filetypes=[("Text Files", "*.txt")],
            title="Lưu danh sách công việc"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    for task in self.tasks:
                        file.write(task + "\n")
                messagebox.showinfo("Lưu công việc", "Danh sách công việc đã được lưu thành công!")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi khi lưu file: {str(e)}")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")],
            title="Chọn file danh sách công việc"
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    tasks = file.readlines()
                # Loại bỏ ký tự xuống dòng và các dòng trống
                self.tasks = [task.strip() for task in tasks if task.strip()]
                self.update_listbox()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi khi tải file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

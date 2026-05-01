import tkinter as tk
from tkinter import messagebox

class NotificationToast:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Hide the main window
        self.toast = tk.Toplevel(self.root)
        self.toast.overrideredirect(True)  # Remove window decorations
        self.toast.geometry("300x50")  # Set toast size
        self.toast.resizable(False, False)  # Make toast non-resizable
        self.toast.attributes("-alpha", 0.9)  # Set toast transparency
        self.toast.attributes("-topmost", True)  # Make toast always on top

    def show_success(self, message):
        self.toast.title("Success")
        self.toast.config(bg="#C6F4D6")  # Set success background color
        self.label = tk.Label(self.toast, text=message, bg="#C6F4D6", fg="#2E865F")
        self.label.pack(padx=10, pady=10)

    def show_error(self, message):
        self.toast.title("Error")
        self.toast.config(bg="#F2DEDE")  # Set error background color
        self.label = tk.Label(self.toast, text=message, bg="#F2DEDE", fg="#8B0A1A")
        self.label.pack(padx=10, pady=10)

    def show_info(self, message):
        self.toast.title("Info")
        self.toast.config(bg="#D9E5F9")  # Set info background color
        self.label = tk.Label(self.toast, text=message, bg="#D9E5F9", fg="#2F4F7F")
        self.label.pack(padx=10, pady=10)

    def show(self, message, toast_type):
        if toast_type == "success":
            self.show_success(message)
        elif toast_type == "error":
            self.show_error(message)
        elif toast_type == "info":
            self.show_info(message)
        else:
            messagebox.showerror("Error", "Invalid toast type")
        self.toast.after(2000, self.hide)  # Hide toast after 2 seconds

    def hide(self):
        self.toast.destroy()

root = tk.Tk()
toast = NotificationToast(root)

toast.show("Success message", "success")
toast.show("Error message", "error")
toast.show("Info message", "info")

root.mainloop()
```

Bu kodda, `NotificationToast` klassi yaratiladi, u quyidagi xususiyatlarni boshqaradi:

* `show_success`, `show_error`, `show_info` metodlari - har biriga xos rangga ega toastni ko'rsatadi.
* `show` metodi - toastni ko'rsatadi va 2 soniyadan keyin yashiradi.
* `hide` metodi - toastni yashiradi.

`mainloop` metodi bilan dastur ishga tushiriladi.

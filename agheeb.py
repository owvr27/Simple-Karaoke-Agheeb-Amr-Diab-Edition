# -*- coding: utf-8 -*-
import tkinter as tk
import time

# الكلمات مع التوقيت (بالثواني)
lyrics = [
    (0.0, "أغيب وأقول ده زمانه نسيني"),
    (4.0, "ماهو لو ينسى هينسيني"),
    (8.0, "طول ما هو فاكر هفضل فاكر"),
    (12.0, "ايوه أمال أنا بسأل ليه"),
]

TOTAL_DURATION = 16  # المدة الكلية (ثواني)

class SimpleKaraoke:
    def __init__(self, root):
        self.root = root
        self.root.title("أغيب - عرض كلمات")
        self.root.geometry("600x300")
        self.root.configure(bg="black")

        self.start_time = time.time()
        self.current_time = 0

        self.label = tk.Label(root, text="", font=("Arial", 24), fg="white", bg="black", wraplength=580, justify="center")
        self.label.pack(expand=True)

        # ابدأ العرض مباشرة
        self.update_display()

    def update_display(self):
        self.current_time = time.time() - self.start_time
        if self.current_time >= TOTAL_DURATION:
            self.current_time = TOTAL_DURATION

        # تحديد السطر الحالي
        current_line = ""
        for t, text in lyrics:
            if self.current_time >= t:
                current_line = text

        self.label.config(text=current_line)
        self.root.after(100, self.update_display)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleKaraoke(root)
    root.mainloop()

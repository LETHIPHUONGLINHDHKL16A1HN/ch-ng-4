import tkter as tk
class RadioButtonExample:
def __init__(self, root):
self.root = root
self.root.title("Radio Button Example")
self.root.geometry('300x80')
# Biến kiểu IntVar để lưu giá trị radio button được chọn
self.selected_option = tk.IntVar()
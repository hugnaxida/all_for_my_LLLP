import tkinter as tk

def show_complete_message(str1):
    root = tk.Tk()
    root.geometry("500x200")  # 设置弹窗的宽度和高度
    root.title("made--by--chengdenghe")  # 设置弹窗的标题
    #root.iconbitmap("icon.ico")  # 设置弹窗的图标（icon.ico是自定义的图标文件路径）
    label = tk.Label(root, text=str1, font=("Arial", 16))
    label.pack(pady=50)

    root.mainloop()
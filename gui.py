from tkinter import *


root = Tk()

root.title("Explorer")
root.iconbitmap(default='icons/папка.ico')
root.config(bg="#ffffff")
width = int(root.winfo_screenwidth() * 0.45)
height = int(root.winfo_screenheight() * 0.45)
root.geometry(f'{width}x{height}')
root.resizable(False,False)




root.mainloop()
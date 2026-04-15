from tkinter import *
from tkinter import ttk
import os

def load():
    for line in current_path:
        tree.insert("", END, values=line)

def on_double_click(event):
    info = tree.focus()
    fileName = tree.item(info)
    new_path = fileName['values'][0]
    global current_path
    current_path = os.listdir(path=f'C:/{new_path}')
    print(current_path)
    load()
    

root = Tk()

root.title("Explorer")
root.iconbitmap(default='icons/папка.ico')
root.config(bg="#ffffff")
width = int(root.winfo_screenwidth() * 0.45)
height = int(root.winfo_screenheight() * 0.45)
root.geometry(f'{width}x{height}')
root.resizable(False,False)

search = Frame(width=width, background="#F3F3F3", borderwidth=1, highlightbackground="#808080", relief=RIDGE)
search.pack(anchor=NW)


back = Button(search, width=6, height=2, text='<-')
back.pack(side=LEFT)
next = Button(search, width=6, height=2, text='->')
next.pack(side=LEFT)
refresh = Button(search, width=6, height=2, text='⟳', command=load)
refresh.pack(side=LEFT)


actions = Frame(width=width, height=45, background="#D4D4D4", borderwidth=1, highlightbackground="#808080", relief=RIDGE)
actions.pack(anchor=NW)



quickAccess = Frame(width=200, height=height-90, background="#F3F3F3", borderwidth=1, highlightbackground="#808080", relief=RIDGE)
quickAccess.pack(side=LEFT)

mainTable = Frame(width=width-200, height=height-90, background="#FFF")
mainTable.pack(side=LEFT)

current_path = os.listdir(path='C:/')
columns = ('Имя')
tree = ttk.Treeview(mainTable, columns=columns, show="headings")
tree.pack()
load()


tree.heading("Имя", text=f"Имя")
tree.bind("<Double-1>", on_double_click)


root.mainloop()
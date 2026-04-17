from tkinter import *
from tkinter import ttk
from functions import load, openFile, backFile
import os



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


back = Button(search, width=6, height=2, text='<-', command=lambda: backFile.back(currentPath, tree))
back.pack(side=LEFT)
next = Button(search, width=6, height=2, text='->')
next.pack(side=LEFT)
refresh = Button(search, width=6, height=2, text='⟳', command=lambda: load.load_data(currentPath, tree))
refresh.pack(side=LEFT)




actions = Frame(width=width, height=45, background="#D4D4D4", borderwidth=1, highlightbackground="#808080", relief=RIDGE)
actions.pack(anchor=NW)




quickAccess = Frame(width=200, height=height-90, background="#F3F3F3", borderwidth=1, highlightbackground="#808080", relief=RIDGE)
quickAccess.pack(side=LEFT)


mainTable = Frame(width=width, height=height)
mainTable.pack(anchor=CENTER)

columns = ('Имя')
tree = ttk.Treeview(mainTable, columns=columns, show="headings", height=25)
tree.column('Имя', width=width-200)
tree.pack()
tree.heading("Имя", text="Имя", anchor=W)

currentPath = ["C:/"]
tree.bind("<Double-Button-1>", lambda event: openFile.open(tree, currentPath))

load.load_data(currentPath, tree)



root.mainloop()
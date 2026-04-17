from tkinter import *
import os


def load_data(path, table):
    fipath = '/'.join(path)
    for item in table.get_children():
        table.delete(item)
    for line in os.listdir(fipath):
        table.insert("", END, values=line)
    
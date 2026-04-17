from functions import load

def back(currentPath, table):
    currentPath.pop()
    load.load_data(currentPath, table)
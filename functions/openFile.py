from functions import load

def open(table, currentPath):
    line_id = table.focus()
    file = table.item(line_id)
    fileName = file['values'][0]
    currentPath.append(fileName)
    load.load_data(currentPath, table) 
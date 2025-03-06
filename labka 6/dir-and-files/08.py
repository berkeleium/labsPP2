import os

path = input("Enter path to delete: ")
if os.access(path, os.F_OK):
    os.remove(path)
else:
    print("File does not exists")
import os

path = input("Input path of file: ")
Directories = []
Files = []
All = os.listdir(path)
for i in All:
    if os.path.isdir(i):
        Directories.append(i)
    else:
        Files.append(i)
print(f"Directories: {Directories}")
print(f"Files: {Files}")
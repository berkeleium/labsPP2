f = open(r'C:\Users\Admin\Desktop\LAB\labka 6\dir-and-files\text.txt', 'r')
count = 0
for i in f:
    count += 1
print(count)
f.close()
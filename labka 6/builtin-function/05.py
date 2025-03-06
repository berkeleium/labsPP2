tuple = ("a", 1, "A", "B", 5, "")
check = True
for i in tuple:
    if bool(i) == False:
        check = False
if check:
    print("True")
else:
    print("False")
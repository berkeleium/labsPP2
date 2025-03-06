n = "HelloKBTU"
Upper = 0
Lower = 0
for letter in map(lambda x: x, n):
    if ord(letter) >= 65 and ord(letter) <= 90:
        Upper += 1
    else:
        Lower += 1
print(f"upper : {Upper}")
print(f"lower : {Lower}")
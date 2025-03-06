import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
print("Input the length of a side:", round((n * pow(l, 2)) / (4 * math.tan(math.pi / n))))
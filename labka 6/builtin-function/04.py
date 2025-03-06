import time, math

n = int(input("Sample Input:\n"))
t = int(input())
n_square = math.sqrt(n)
t = float(t / 1000)
time.sleep(t)
print(f"Square root of {n} after {int(t * 1000)} miliseconds is {n_square}")
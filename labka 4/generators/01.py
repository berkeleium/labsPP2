def Square():
    start = 1
    while True:
        yield start ** 2
        start += 1
n = int(input())
gen = Square()
for i in range(n):
    print(next(gen), end=" ")
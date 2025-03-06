def ViceVersa(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
gen = ViceVersa(n)
for i in gen:
    print(i)
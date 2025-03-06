def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

start = int(input())
end = int(input())
gen = squares(start, end)
for i in gen:
    print(i)
# for i in squares(start, end):
#     print(i)
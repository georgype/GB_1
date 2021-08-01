def fact(n, a=1):
    for i in range(n):
        a *= (i + 1)
        yield a


n = int(input())
for el in fact(n):
    print(el)
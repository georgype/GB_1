from itertools import count, cycle


def iter_a(n):
    for i in count(n):
        yield i
        if i > n + 20:
            break


n = int(input())
for i in iter_a(n):
    print(i)


def iter_b(l):
    n = 1
    for i in cycle(l):
        yield i
        n += 1
        if n > len(l)*3:
            break


l = input().split()
for i in iter_b(l):
    print(i)
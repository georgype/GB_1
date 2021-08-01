l = input().split()
[print(i, end=' ') for i in l if l.count(i) == 1]

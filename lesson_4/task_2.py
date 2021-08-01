l = input().split()
[print(l[i], end=' ') for i in range(1, len(l)) if l[i] > l[i - 1]]

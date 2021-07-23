def func(l):
    global s
    for i in l:
        if i.isnumeric():
            s += int(i)
        else:
            return False
    return True


s = 0
b = True
while b:
    a = input().split()
    b = func(a)
    print(s)

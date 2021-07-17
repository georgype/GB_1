n = input()
num_max = 0
count = 0
while count < len(n):
    c = int(n[count])
    if c > num_max:
        num_max = c
    count += 1
print(num_max)

from functools import reduce

l = [i for i in range(100, 1001) if i % 2 == 0]
print(l)
print(reduce((lambda prev, next_el: prev * next_el), l))

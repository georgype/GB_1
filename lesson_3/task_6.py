# def int_func(s):
#     return s.title()


def int_func_2(s):
    return s.capitalize()


my_str = input()
# print(int_func(my_str))
print(int_func_2(my_str))

for i in my_str.split():
    print(int_func_2(i), end=' ')

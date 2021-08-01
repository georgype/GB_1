import re

with open('text_task_6.txt') as t:
    d = {}
    for i in t:
        d[i.split()[0]] = sum([int(j) for j in re.findall('\d+', i)])
    print(d)
import json

with open('text_task_7.txt') as t:
    n = 0
    s = 0
    d = {}
    l = []
    for i in t:
        a = i.split()
        profit = int(a[2]) - int(a[3])
        if profit >= 0:
            s += profit
            n += 1
        d[a[0]] = profit
    mid = s / n
    l.append(d)
    d_mid = {'average_profit': mid}
    l.append(d_mid)
    with open('json_task_7.json', 'w') as js:
        json.dump(l, js)

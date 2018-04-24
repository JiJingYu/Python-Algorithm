d = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']  # 0-12
d2 = ['', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
N = int(input())
for i in range(N):
    num = input()
    if num.isdigit():
        a, b = int(num) // 13, int(num) % 13
        if a == 0:
            print(d[b])
        elif b == 0:
            print(d2[a])
        else:
            print(d2[a], d[b])
    else:
        num = num.split()
        if len(num) == 1:
            a = num[0]
            if a in d:
                print(d.index(a))
            else:
                print(d2.index(a) * 13)
        else:
            a, b = num
            a = d2.index(a)
            b = d.index(b)
            print(a * 13 + b)

"""
6
29
5
elo nov
tam
0
10
"""
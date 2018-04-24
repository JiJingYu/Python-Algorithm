rate = 1.0
d = {0: 'W', 1: 'T', 2: 'L'}
s = []
for i in range(3):
    num = [float(x) for x in input().split()]
    choise = max([0, 1, 2], key=lambda x: num[x])
    s.append(d[choise])
    rate *= num[choise]
    profit = (rate * 0.65 - 1) * 2
    print(' '.join(s), '{:.1f}'.format(profit))


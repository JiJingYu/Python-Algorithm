import datetime

N = int(input())
info = []
for i in range(N):
    name, t1, t2 = input().split()
    h, m, s = list(map(int, t1.split(':')))
    t1 = datetime.timedelta(hours=h, minutes=m, seconds=s)
    h, m, s = list(map(int, t2.split(':')))
    t2 = datetime.timedelta(hours=h, minutes=m, seconds=s)
    info.append({'name': name, 't1': t1, 't2': t2})
p1 = min(info, key=lambda d: d["t1"])
p2 = max(info, key=lambda d: d["t2"])
print(p1['name'], p2['name'])

"""
3
CS301111 15:30:28 17:00:10
SC3021234 08:00:00 11:25:25
CS301133 21:45:00 21:58:40
"""

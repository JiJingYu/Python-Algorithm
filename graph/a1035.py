N = int(input())
flag = False
d = {'1': '@', '0': '%', 'l': 'L', 'O': 'o'}
res = []
for i in range(N):
    user, password = input().split()
    curr_flag = False
    for l in d:
        if l in password:
            curr_flag, flag=True, True
            password=password.replace(l, d[l])
    if curr_flag:
        res.append((user, password))
if not res and N == 1:
    print('There is 1 account and no account is modified')
elif not res:
    print('There are {} accounts and no account is modified'.format(N))
else:
    print(len(res))
    for r in res:
        print(r[0], r[1])


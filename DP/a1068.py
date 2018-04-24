N, value = [int(x) for x in input().split()]
coins = sorted([int(x) for x in input().split()], reverse=True)
res = []


def dfs(i, path, value):
    if value == 0 and not path:
        return
    if value == 0:
        print(" ".join(map(str, path)))
        exit(0)
        # res.append(path)
        # return
    if i < 0:
        return
    if coins[i] <= value:
        dfs(i - 1, path + [coins[i]], value - coins[i])
        dfs(i - 1, path, value)
    else:
        dfs(i - 1, path, value)
dfs(N-1, [], value)
if not res:
    print("No Solution")
    exit(0)
# print(" ".join(map(str, res[0])))

"""
4 8
1 2 3 3
"""

add=[]
n=0
sum=0
for i, x in enumerate(input().split()):
    if i==0:
        n=int(x)
        add = [0 for i in range(n+1)]
        continue
    sum += int(x)
    add[i]=sum
M = int(input())
for i in range(M):
  d1, d2 = [int(x) for x in input().split()]
  if d1>d2:
      d1, d2 = d2, d1
  dist = add[d2-1]-add[d1-1]
  print(min(dist, sum-dist))
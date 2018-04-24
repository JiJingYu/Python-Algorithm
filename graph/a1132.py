def foo(num):
  n = len(num)//2
  n1,n2,p = int(num[:n]), int(num[n:]), int(num)
  if not n1 or not n2:
      print("No")
      return 
  if p % (n1*n2)==0:
    print("Yes")
  else:
    print("No")
N = int(input())
res = []
for i in range(N):
  res.append(input().split()[0])
[foo(s) for s in res]

"""
4
167334
10
12345678
123456789123456789
"""
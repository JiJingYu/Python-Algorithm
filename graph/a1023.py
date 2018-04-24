from collections import Counter

num = int(input())
num2 = num * 2
c1 = Counter(list(str(num)))
c2 = Counter(list(str(num2)))
if c1==c2:
  print("Yes")
else:
  print("No")
print(num2)
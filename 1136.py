def Palin(num):
  num = str(num)
  return num == num[::-1], int(num[::-1])

x = int(input())
for i in range(10):
  isPalin, x_r = Palin(x)
  if not isPalin:
    x_next = x+x_r
    print("{} + {} = {}".format(x, x_r, x_next))
  else:
    print('{} is a palindromic number.'.format(x))
    exit(0)
print('Not found in 10 iterations.')
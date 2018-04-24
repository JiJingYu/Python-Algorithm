import math


def rev(num, base):
    ret = 0
    while num:
        a = num % base
        num = num // base
        ret = ret * base + a
    return ret


def isPrime(num):
    if num in [0, 1]: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


while True:
    l = [int(x) for x in input().split()]
    if l[0] < 0: break
    num, base = l
    if isPrime(num) and isPrime(rev(num, base)):
        print("Yes")
    else:
        print("No")

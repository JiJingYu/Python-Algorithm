d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
num = input().split()[0]
num = str(sum(map(int, list(num))))
res = []
for i in num:
  res.append(d[i])
print(' '.join(res))
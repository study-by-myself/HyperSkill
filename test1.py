result = 1
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
a = 100
b = 200
c = 1

for n in range(a, b + 1):
  count = 1
  while n != 1:
    if n % 2 == 0:
      n /= 2
      count += 1
    elif n % 2 == 1:
      n = n * 3 + 1
      if n > b / 3 and c > 0:
        c -= 1
        n += 10
      count += 1
  if count > result:
    result = count

print(result)

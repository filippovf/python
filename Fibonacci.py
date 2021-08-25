# Fibonacci
i = 0
j = 1
x = 0
print(i)
print(j)
while x < 1000:
  x = i + j
  i = j
  j = x
  print(x)

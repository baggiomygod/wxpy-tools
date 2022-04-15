print(list(range(1,11)))
l1 = [x*x for x in range(1,11)]
print(l1)

l2 = [x*x for x in range(1,11) if x % 2 == 0]
print(l2)

g = (x * x for x in range(10))

print(g)

for n in g:
  print(n)
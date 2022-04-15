# def calc(nums):
#   sum = 0
#   for n in nums:
#     sum += n*n
#   return sum

# print(calc([1,2,3]))
# print(calc((3,4,5)))


# def calc(*nums):
#   print('*args:', nums)
#   sum = 0
#   for n in nums:
#     sum += n*n
#   return sum

# print(calc(1,2,3))
# print(calc(3,4,5))
# print(calc())

# def person(name, age, **kw):
#    print('name:', name, 'age:', age, 'other:', kw)
   
# print(person('Michael', 30))
# print(person('Michael', 30, city="hz"))
# print(person('Michael', 30, city="hz", job='web'))

# ex={'c': 'bei', 'j': 'dev'}
# print(person('xx', 12, c=ex['c'], j = ex['j']))


def f(a,b=1,*c,**kw):
  print(a, b, c, kw)

f(1, 2)
f(1,2, c=2)
f(1,'a', 'b', l=1)
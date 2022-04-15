from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75, 'A'), ('Adam', 92, 'B'), ('Bart', 66, 'C'), ('Lisa', 88, 'D')]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=itemgetter(1)))
print(sorted(students, key=lambda t: t[0])) # 匿名函数 lambda t: t[0]
print(sorted(students, key=lambda t: t[2])) # 匿名函数 lambda t: t[2]
print(sorted(students, key=itemgetter(1), reverse=True)) # 第二个反向排序
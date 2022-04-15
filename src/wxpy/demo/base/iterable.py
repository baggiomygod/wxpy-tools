from typing import Iterable


print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('adf', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
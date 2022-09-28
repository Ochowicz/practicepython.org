import random

a = []
b = []
for x in range(0, 11):
    a.append(random.randint(0, 20))
    b.append(random.randint(3, 24))
a.sort()
b.sort()

print(a, '\n', b, '\n')
print(list(dict.fromkeys([i for i in a if i in b])))

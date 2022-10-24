import random
a = [random.randint(0, 20) for item in range(random.randint(0, 15))]
b = [random.randint(0, 20) for item in range(random.randint(0, 15))]

print(a)
print(b)

common = [item_a for item_a in a if item_a in b]
common.sort()
print(common)
common_without_dubble = []
for num in common:
    if num not in common_without_dubble:
        common_without_dubble.append(num)
common_without_dubble.sort()
print(common_without_dubble)

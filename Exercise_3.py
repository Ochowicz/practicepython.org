a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# rozwiązanie podstawowe
for number in a:
    if number < 5:
        print(number)

# rozwiązanie extra 1 i 2
print([number for number in a if number < 5])

# rozwiązanie extra 3
less_than_5 = []
less_than_n = []

for number in a:
    if number < 5:
        less_than_5.append(number)
        less_than_5.sort()
print(less_than_5)

n = int(input("Write any number: "))
for number in a:
    if number < n:
        less_than_n.append(number)
        less_than_n.sort()
print(less_than_n)
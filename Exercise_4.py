number = int(input("Write any number to check it divisors: "))

# zadanie podstawowe - wypisane dzielniki w osobnych liniach
for n in range(1, number + 1):
    if number % n == 0:
        print(n)

# zadanie podstawowe - dzielniki jako nowa lista (jedna linijka)
print([n for n in range(1, number + 1) if number % n == 0])

# zadanie podstawowe - ładniej
dzielniki = []
for n in range(1, number + 1):
    if number % n == 0:
        dzielniki.append(n)
        dzielniki.sort()
print(dzielniki)
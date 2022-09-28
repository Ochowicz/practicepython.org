# Import Random Module
import random

# creating lists
list_a = [random.randint(1, 20) for numbers in range(random.randint(5, 20))]
print(list_a)
list_b = []
for numbers in range(random.randint(5, 20)):
    list_b.append(random.randint(1, 20))
print(list_b)

# common elements of lists
list_common = []
for number_a in list_a:
    if number_a in list_a and number_a in list_b:
        if number_a not in list_common:
            list_common.append(number_a)

# print common list without repetition and in order
list_common.sort()
print(list_common)

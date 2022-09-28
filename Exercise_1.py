name = input("Your name: ")
age = int(input("Your age: "))
year = 2022 - age + 100
messenge = name + ", You will have 100 years in " + str(year)
print(messenge)
number_of_copies = int(input("Please write any number: "))
while number_of_copies > 0:
    print(messenge)
    number_of_copies -= 1

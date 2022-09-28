number = int(input("Write a number: "))
check  = int(input('Write a number to divide: '))

if number % 4 == 0:
    print(number, "is multiple of 4")
elif (number % 2) == 0:
    print(number, 'is even number')
else:
    print(number, 'is odd number')

if number % check == 0:
    print (number, "is multiple of", check)
else:
    print (number, "isn't multiple of", check)
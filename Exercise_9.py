import random
# Lets start this shit
guessed_number = ''
attempts = 1
while guessed_number.lower != 'exit':
    generated_number = random.randint(1, 10)
    guessed_number = input("Guess the number which is generated in range <1, 10>:\n")
    if guessed_number.lower == 'exit':
        print('See Ya')
        break
    while int(guessed_number) != generated_number:
        if guessed_number.lower == 'exit':
            print('See Ya')
            break
        elif int(guessed_number) > generated_number:
            print('Too high, find another one in range <1', guessed_number, '>')
        elif int(guessed_number) < generated_number:
            print('Too low, find another one in range <', guessed_number, ', 10>')
        else:
            print("That's it!")
            if attempts < 2:
                print("Excellent, You need only ", attempts, " attempts")
            elif 2 < attempts < 5:
                print("Nice, You need only ", attempts, " attempts.")
            else:
                print("Not perfect but finally it in ", attempts, ". attempts")

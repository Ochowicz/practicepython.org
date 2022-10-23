player_1 = input('Give name to player_1:\n')
player_2 = input('Give name to player_2:\n')

while True:
    sign_1 = input(f'{player_1}, give me Your sign:\n')
    sign_2 = input(f'{player_2}, give me Your sign:\n')
    if (sign_1 == "rock" and sign_2 == "rock") or (sign_1 == "paper" and sign_2 == "paper") or (sign_1 == "scisors" and sign_2 == "scisors"):
        print("It's a draw")
    elif (sign_1 == "rock" and sign_2 == "paper") or (sign_1 == "paper" and sign_2 == "scisors") or (sign_1 == "scisors" and sign_2 == "rock"):
        print(f'{player_2} won')
    elif (sign_2 == "rock" and sign_1 == "paper") or (sign_2 == "paper" and sign_1 == "scisors") or (sign_2 == "scisors" and sign_1 == "rock"):
        print(f'{player_1} won')
    else:
        print ("One or both of You give illegal sign")

    exit = input('Do You wanna play again? (y/n)\n')
    if exit == 'y':
        print('Get ready for the rumble!!!')
    elif exit == 'n':
        break
    else:
        print("unnown commend")
        break


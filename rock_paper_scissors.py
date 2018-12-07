import random, sys

rockpaperscissors = {
    1:'Steen',
    2:'Papier',
    3:'Schaar'
    }

winner_dict = {
    0:'Equal',
    1:'User',
    2:'Computer'
}

ronde = 1

user_name = input("Wat is je naam: ")
winner_dict[1] = user_name
score_user = 0
score_computer = 0

def gameround(user_choice):
    computer_choice = random.randint(1,3)
    global score_user
    global score_computer

    roundwinner = 0

    if int(user_choice) == 1 and computer_choice == 3:
        print(f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}')
        roundwinner = 1
        score_user += 1


    elif int(user_choice) == 2 and computer_choice == 1:
        print(f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}')
        roundwinner = 1
        score_user += 1

    elif int(user_choice) == 3 and computer_choice == 2:
        print(f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}')
        roundwinner = 1
        score_user += 1

    elif int(user_choice) == computer_choice:
        print(f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}')
        roundwinner = 0


    else:
        print(f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}')
        roundwinner = 2
        score_computer += 1

    if roundwinner == 0:
        print(f'Equal game\n')
    else:
        print(f'{winner_dict[roundwinner]} wins\n')


while True:
    rounds = input('Hoeveel rondes?(3/5/7): ')

    try:
       val = int(rounds)
       if int(rounds) % 2 == 0:
           print('Kies een oneven nummer')
       elif not int(rounds) or rounds not in ['3', '5', '7']:
           print('Kies alleen 3, 5 of 7')
       else:
           while ronde <= int(rounds):
               user_input = input('Steen(1), papier(2) of schaar(3):')
               if not user_input or user_input not in ['1', '2', '3']:
                   print('Kies alleen 1, 2 of 3')
                   continue
               gameround(user_input)
               ronde += 1

    except ValueError:
       print("Je moet een cijfer invullen")
       print("Geen letter(s)")
    again = input('Nog een spelletje? (j/n)').lower()
    if again == 'j':
        ronde = 1
        continue
    else:
        break

# Print scores
print(f'\n')
print(f'De computer heeft {score_computer} keer gewonnen')
print(f'{winner_dict[1]} heeft {score_user} keer gewonnen\n')

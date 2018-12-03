import random, sys
from menu import Menuutje
from tkinter import *

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

round = 1
# click and collect functie



root = Tk()

m = Menuutje(root)
askUsername = Label(root, text="Wat is je naam wat kom je doen je lijkt me aardig:")
askUsername.grid(row=0, column=0)
entryUser = Text(root, height=2)
entryUser.bind("<Return>", usernameFill)

def usernameFill(event):
    user_name = entryUser.get()
    askUsername['text']=user_name


def steenKeus():
    gameround(1)

def papierKeus():
    gameround(2)

def schaarKeus():
    gameround(3)

steen = Button(root, text="Steen" command=steenKeus)
papier = Button(root, text="Papier" command=papierKeus)
schaar = Button(root, text="Schaar" command=schaarKeus)


#user_name = input("Wat is je naam: ")
winner_dict[1] = user_name
score_user = 0
score_computer = 0
labelText = Label(root, text='')
labelText.pack(side=TOP)
labelRound = Label(root, text='')
labelRound.pack(side=TOP)

# ronde functie
def gameround(user_choice):
    computer_choice = random.randint(1,3)
    global score_user
    global score_computer
    global labelText
    global labelRound

    roundwinner = 0

    if int(user_choice) == 1 and computer_choice == 3:
        labelText['text'] = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner = 1
        score_user += 1


    elif int(user_choice) == 2 and computer_choice == 1:
        labelText['text'] = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner = 1
        score_user += 1

    elif int(user_choice) == 3 and computer_choice == 2:
        labelText['text'] = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner = 1
        score_user += 1

    elif int(user_choice) == computer_choice:
        labelText['text'] = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner = 0


    else:
        labelText = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner['text'] = 2
        score_computer += 1

    if roundwinner == 0:
        labelRound['text'] = f'Equal game\n'
    else:
        labelRound['text'] = f'{winner_dict[roundwinner]} wins\n'

# while loop voor de echte rondes


while True:
    rounds = input('Hoeveel rondes?(3/5/7): ')

    try:
       val = int(rounds)
       if int(rounds) % 2 == 0:
           print('Kies een oneven nummer')
       elif not int(rounds) or rounds not in ['3', '5', '7']:
           tkinter.message('Kies alleen 3, 5 of 7')
       else:
           while round <= int(rounds):
               steen.grid(row=1, column=1)

               papier.grid(row=1, column=2)
               schaar.grid(row=1, column=3)
               round += 1

    except ValueError:
       print("Je moet een cijfer invullen")
       print("Geen letter(s)")
    again = input('Nog een spelletje? (j/n)').lower()
    if again == 'j':
        round = 1
        continue
    else:
        break

# Print scores
print(f'\n')
print(f'De computer heeft {score_computer} keer gewonnen')
print(f'{winner_dict[1]} heeft {score_user} keer gewonnen\n')

root.mainloop()

import random, sys
from menu import Menuutje
from tkinter import *
import tkinter.messagebox

rockpaperscissors = {
    1: 'Steen',
    2: 'Papier',
    3: 'Schaar'
    }

winner_dict = {
    0: 'Equal',
    1: 'User',
    2: 'Computer'
}
rounds = 0
ronde = 1
# click and collect functie
user_name = ''
root = Tk()


def usernameFill(event):
    global user_name
    user_name = entryUser.get()
    askUsername['text']=user_name


def roundsFill(event):
    global rounds
    rounds = entryRounds.get()
    # if username is not set in previous <Return> event do it again
    global user_name
    user_name = entryUser.get()
    askUsername['text'] = user_name
    winner_dict[1] = user_name
    showBuutons()


def startGameButton():
    global rounds
    rounds = entryRounds.get()
    # if username is not set in previous <Return> event do it again
    global user_name
    user_name = entryUser.get()
    askUsername['text'] = user_name
    winner_dict[1] = user_name
    showBuutons()


# vraag de gamer om naam:
askUsername = Label(root, text="Wat is je naam wat kom je doen je lijkt me aardig:")
askUsername.grid(row=0, column=0)
entryUser = Entry(root)
entryUser.grid(row=0, column=1)
entryUser.bind("<Return>", usernameFill)

# de steen papier schaar knoppen
def steenKeus():
    gameround(1)
    checkNogeens()

def papierKeus():
    gameround(2)
    checkNogeens()

def schaarKeus():
    gameround(3)
    checkNogeens()


steen = Button(root, text="Steen", command=steenKeus)
papier = Button(root, text="Papier", command=papierKeus)
schaar = Button(root, text="Schaar", command=schaarKeus)


# user_name = input("Wat is je naam: ")
winner_dict[1] = user_name
score_user = 0
score_computer = 0
labelText = Label(root, text='')
labelText.grid(row=3, column=0, columnspan=3)
labelRound = Label(root, text='')
labelRound.grid(row=4, column=0, columnspan=3)

# ronde functie
def gameround(user_choice):
    computer_choice = random.randint(1,3)
    global score_user
    global score_computer
    global labelText
    global labelRound
    global ronde
    global winner_dict

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
        labelText['text'] = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner = 2
        score_computer += 1

    if roundwinner == 0:
        labelRound['text'] = f'Equal game\n'
    else:
        labelRound['text'] = f'{winner_dict[roundwinner]} wins\n'
    ronde += 1

# while loop voor de echte rondes

# show de buttons als de input klopt

def showBuutons():
    try:
        val = int(rounds)
        if int(rounds) % 2 == 0:
            tkinter.messagebox.showinfo('Oneven nummers', 'Kies een oneven nummer')
        elif not int(rounds) or rounds not in ['3', '5', '7']:
            tkinter.messagebox.showinfo('Oneven nummers', 'Kies alleen 3, 5 of 7')
        else:
            steen.grid(row=2, column=0)

            papier.grid(row=2, column=1)
            schaar.grid(row=2, column=2)


    except ValueError:
        tkinter.messagebox.showinfo('Alleen cijfers', 'Je moet een cijfer invullen, Geen letter(s)')


# toon de totaal scores:
def showScores():
    global score_computer
    global score_user
    global winner_dict

    tkinter.messagebox.showinfo('Totaal score',
                                f'De computer heeft {score_computer} keer gewonnen \n {winner_dict[1]} heeft {score_user} keer gewonnen')
    exit()



# hoofd ronde loop functie

def checkNogeens():
    global ronde
    global rounds
    again = 'init'
    if ronde > int(rounds):
        again = tkinter.messagebox.askquestion('Nog eens', 'Wil je nog een keer?')
        print('Doet ie ut of doet ie ut niet')
    if again == 'yes':
        ronde = 1
    elif again == 'init':
        print(f'Niks te doen; ronde {ronde} van {rounds} rondes')
    else:
        showScores()


# vraag om hoeveel rondes
askRounds = Label(root, text="Hoeveel rondes?(3/5/7):")
askRounds.grid(row=1, column=0)
entryRounds = Entry(root)
entryRounds.grid(row=1, column=1)
entryRounds.bind("<Return>", roundsFill)
saveNameRounds = Button(root, text='Start', command=startGameButton)
saveNameRounds.grid(row=1, column=2)
# Print scores


root.mainloop()

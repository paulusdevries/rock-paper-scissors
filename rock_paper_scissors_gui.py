import random, sys
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
equal_score = 0
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
    global equal_score

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
        equal_score += 1


    else:
        labelText['text'] = f'Je koos {rockpaperscissors[int(user_choice)]} en Computer koos {rockpaperscissors[computer_choice]}'
        roundwinner = 2
        score_computer += 1

    if roundwinner == 0:
        labelRound['text'] = f'Equal game\n'
    else:
        labelRound['text'] = f'{winner_dict[roundwinner]} wins\n'
    ronde += 1


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
                                f'De computer heeft {score_computer} keer gewonnen \n{winner_dict[1]} heeft {score_user} keer gewonnen \n{equal_score} keer gelijkspel')
    sys.exit()

# scherm legen

def emptyGrid():
    global labelRound
    global labelText
    global entryRounds
    steen.grid_forget()
    papier.grid_forget()
    schaar.grid_forget()
    labelRound['text'] = ''
    labelText['text'] = ''
    entryRounds.delete(0, END)

# hoofd ronde loop functie


def checkNogeens():
    global ronde
    global rounds
    again = 'init'
    if ronde > int(rounds):
        again = tkinter.messagebox.askquestion('Nog eens', 'Wil je nog een keer?')
        # debug printing commented
        # print('Doet ie ut of doet ie ut niet')
    if again == 'yes':
        ronde = 1
        emptyGrid()
    elif again == "no":
        showScores()


class MenuGameRPS:
    def __init__(self, master):
        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New Game...", command=self.newGame)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=self.exitGame)

    def exitGame(self):
        sys.exit()

    def newGame(self):
        emptyGrid()


# hoofdscherm
# vraag de gamer om naam:
askUsername = Label(root, text="Wat is je naam wat kom je doen je lijkt me aardig:")
askUsername.grid(row=0, column=0)
entryUser = Entry(root)
entryUser.grid(row=0, column=1)
entryUser.bind("<Return>", usernameFill)
# vraag om hoeveel rondes
askRounds = Label(root, text="Hoeveel rondes?(3/5/7):")
askRounds.grid(row=1, column=0)
entryRounds = Entry(root)
entryRounds.grid(row=1, column=1)
entryRounds.bind("<Return>", roundsFill)
saveNameRounds = Button(root, text='Start', command=startGameButton)
saveNameRounds.grid(row=1, column=2)
# Print scores

menu = MenuGameRPS(root)
root.mainloop()

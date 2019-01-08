import random
password = ''


class PasswordGen:

    def __init__(self, strength):
        global password
        i = 0
        while i < strength:
            password = password + random.choice('abcdefghijklmnopqrstuvwxyz+-_)(*&^%$#@!/.,<>;:~`')
            i += 1

    def printPass(self):
        print(f"Password: {password}")


def askStrength():
    choice = input('What strength do you want your password choose 1, 2 or 3 for light, medium or strong; ')
    if choice == '1':
        return 8
    elif choice == '2':
        return 16
    elif choice == '3':
        return 24


p = PasswordGen(askStrength())
p.printPass()

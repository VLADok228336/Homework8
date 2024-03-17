from random import*
from time import*
def coolPrint(s1):
    s11 = list(s1)
    for i in s11:
        print(i, end="")
        sleep(0.05)
    sleep(1)
    print("")
def start():
    hello()
def hello():
    coolPrint("Hello boys and girls, my name is Fat Lip. And this is my friend Robert the Robot('What 'do?')")
    coolPrint("Today we gonna teach you some fun facts about binary search, and a brand new game")
    instructions()
def instructions():
    coolPrint("Let me introduce to you a brand new game/ I know you gonna love it if you give it one chance")
    coolPrint("It's not complicated, it's not too hard. You don't even have to be a hip hop star")
    coolPrint("That was joke")
    coolPrint("...")
    coolPrint("Okay, there's instructions. You gonna guess number, which my friend Robert has guessed")
    coolPrint("Go ahead")
    guess()
def check(num, guess):
    if guess == num:
        return "="
    elif guess>num:
        return ">"
def guess():
    tries = 1
    number = randint(0, 10000)
    while True:
        coolPrint("Enter a number:")
        guess = int(input())
        if check(number, guess)=="=":
            coolPrint("OMG! What a nice guess!")
            coolPrint(f"You win only with {tries} tries!")
            coolPrint("Wanna play again(y/n)?")
            s = input()
            if s == "n":
                coolPrint("Goodbye! Thanks for playing!")
                exit("Don't forget listen to Metallica!")
            else:
                tries = 1
                number = randint(0, 10000)
        elif check(number, guess)==">":
            coolPrint("That was nice try, but no")
            tries+=1
            if number>guess:
                coolPrint("Higher!")
            if number< guess:
                coolPrint("Lower!")
start()                
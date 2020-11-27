import random
#FOR WELCOME SCREEN
def welcome():
    print("**********WELCOME TO GUESSING GAME**********")
    print("________________GAME DESCRIPTION_____________")
    print("YOU WILL BE GIVEN A CHANCE TO GUESS A NUMBER AND IF YOUR NUMBER IS SAME AS THE NUMBER SLELCTED BY COMPUTER THEN YOU WIN OR ELSE YOU LOOSE")
    print("SO WHAT ARE WE WAITING FOR LETS GET STARTED")

#FOR SINGLE/TWO PLAYERS
def choose():
    x=input("THERE IS TWO OPTION 1.SINGLE PLAYER TYPE 'S' 2.TWO PLAYER TYPE 'D'")
    return x
#for single player
def single():
    score=0
    r=int(input("enter the last value of range:"))
    guess=int(input("GUESS THE NUMBER:"))
    num=random.randint(1,r)
    if guess==num:
        print("YOU GUESSED IT RIGHT!!!!")
        score=+1
        print("score:",score)
    else:
        print("YOU GUESSED IT WRONG :(")
        print("THE NUMBER WAS:",num)
        print("TRY AGAIN NEXT TIME")

#for  two player
def double():
    p1=input("ENTER THE NAME OF PLAYER1:")
    p2=input("ENTER THE NAME OF PLAYER2")
    dr=int(input("ENTER THE LAST NUMBER OF RANGE"))
    dguess1=int(input("ENTER THE GUESS NUMBER PLAYER1:"))
    dguess2=int(input("ENTER THE GUESS NUMBER PLAYER2:"))
    dnum=random.randint(1,dr)
    if dguess1==dguess2==dnum:
        print("!!!!YOU BOTH WON!!!!!")
    elif dguess1==dnum:
        print("!!PLAYER 1 WON!!!!")
    elif dguess2==dnum:
        print("!!!PLAYER 2 WON!!!!")
    else:
        print("YOU BOTH LOOSE :(")
        print("the number was:",dnum)

#CALLING THE FUNCTION
#FIRST WELCOME SCREEN
welcome()
#WETHER SHINGLE OT TWO PLAYER
play=choose()
#S FOR SINGLE ELSE TWO PLAYERS
if play=="S":
    single()
else:
    double()
#IF THEY WANNA PLAY AGIN THEN REPEAT THE PROCESS OR THANK YOU STATEMENT
jn=input("WANNA PLAY THE GAME AGAIN Y/N")
if jn=="Y":
    if play=="S":
        single()
    else:
        double()
else:
    print("~~~~~~~~~~~THANK YOU FOR PLAYING~~~~~~~~~~~~")

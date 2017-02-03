import random

name = input("Hello whats your name ? ")
print("Welcome " +   name)
decksize= input("How many cards do you want, 3 , 6, 10: ")
print("Ok , So you want to play with " + decksize,  "cards!")
player = input("play with a friend or the computer ? [Friend : Computer]")

if player == 'Friend':
    player2 = input("What will his/her name be?:")
    print("Hello! " + player2)

    if decksize=='3':
        namecard = random.randint(0,3)
        print("Ok", name,"your card is", namecard)
        namecard2= random.randint(0,3)
        print("Ok", player2,"your card is", namecard2)
    if namecard > namecard2:
        print(name,"wins!")
    if namecard == namecard2:
        print("Draw")
    if namecard2 < namecard:
        print(player2,"Wins")

elif player == 'Computer':
    print("Be lonely then")


import random

name = input("Hello whats your name ? ")
print("Welcome " +   name)
decksize= input("How many cards do you want, 3 , 6, 10: ")
print("Ok , So you want to play with " + decksize,  "cards!")

player = input("play with a friend or the computer ? [Friend : Computer]")

if player == 'Friend':
    player2 = input("What will his/her name be?:")
    print("Hello! " + player2)

elif player == 'Computer':
    print("Be lonely then")


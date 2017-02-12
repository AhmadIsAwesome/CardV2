import random

print("                                                                               ")
name = input("                             Hello whats your name ?                                                                  ")
print("                                  Welcome " +   name)
print("")
print()
decksize= input("How many cards do you want to use ? 3 , 6, 10, 12, 24: ")
if decksize == '3' or decksize == '6' or decksize == '10' or decksize == '12' or decksize =='24':
    print()
    print("So you want to play with " + decksize,  "cards!")
    print()
    player = input("play with a friend or the computer ? [Friend : Computer] ")
if player == 'Friend':
    print()
    player2 = input("What will his/her name be?:")
    print()
    print("")
    print("                             Welcome! " + player2)
    print("")
    if decksize =='3':
        namecard = random.randint(1,3)
        print(name,"your card is", namecard)
        playercard = random.randint(1,3)
        print(player2,"your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print(player2,"Wins")
    if decksize=='6':
        namecard = random.randint(1,6)
        print(name,"your card is", namecard)
        playercard = random.randint(1,6)
        print(player2,"your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print(player2,"Wins")
    if decksize=='10':
        namecard = random.randint(1,10)
        print(name,"your card is", namecard)
        playercard = random.randint(1,10)
        print(player2,"your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print(player2,"Wins")
    if decksize=='12':
        namecard = random.randint(1,12)
        print(name,"your card is", namecard)
        playercard = random.randint(1,12)
        print(player2,"your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print(player2,"Wins")
    if decksize=='24':
        namecard = random.randint(1,24)
        print(name,"your card is", namecard)
        playercard = random.randint(1,24)
        print(player2,"your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print(player2,"Wins")
        
elif player == 'Computer':
    print("no friends ?")
    if decksize=='3':
        namecard = random.randint(1,3)
        print(name,"your card is", namecard)
        playercard = random.randint(1,3)
        print("Computer your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print("Computer Wins")
    if decksize=='6':
        namecard = random.randint(1,6)
        print(name,"your card is", namecard)
        playercard = random.randint(1,6)
        print("Computer your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print("Computer Wins")
    if decksize=='10':
        namecard = random.randint(1,10)
        print(name,"your card is", namecard)
        playercard = random.randint(1,10)
        print("Computer your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print("Computer Wins")
    if decksize=='12':
        namecard = random.randint(1,12)
        print(name,"your card is", namecard)
        playercard = random.randint(1,12)
        print("Computer your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print("Computer Wins")
    if decksize=='24':
        namecard = random.randint(1,24)
        print(name,"your card is", namecard)
        playercard = random.randint(1,24)
        print("Computer your card is", playercard)
        if namecard > playercard:
             print(name,"wins!")
        if namecard ==playercard:
            print("Draw")
        if playercard > namecard:
            print("Computer Wins")

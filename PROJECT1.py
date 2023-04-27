'''
Joni Ndrecaj

This is a blackjack game made in python.
In this game, the dealer is the computer.
The computer's deck is infinite. 1 player Only.

'''

'''
DISCLAIMER:
1. 1 or 11 is A
2.  same value cards (like J, K, Q) are calculated as a 10 value
and therefore K and 10 is allowed to split.
3. when splitting 2 A's (given 11 value) fails, then it's going to first
check if computer got a higher value meaning you win if computer gets over 21.
4. Splitting only works if your 2 most recent cards are the same.
'''

'''
Algorithm explanation (skip if known):
1. ask the player if he wants to play
2. let the player make decisions, (but show him the options)
a) Player can either Hit
- hit gives a card (randomly given)
- if the sum of all cards is over 21, it's a bust and therefore a loss
b) or Stand
- Player doesn't take any card

c) now is computer's turn
- computer draws until the sum of the cards are equal or over 17
- computer can also bust
- if the sum of cards are equal/over 17, computer stands

d) if both sides stand:
check for 3 conditions
1. player win condition
2. computer win condition
3. it's a tie

e) game ends

'''

import random
#1. ask player if they want to play
print("welcome, press 1 to play!")
DRAWP = int(input("type 1 for draw, 0 for hold: ")) #player's turn
DRAWC = 0
DRAWP = 1
#2. here the cards, the deck, and player/computer cards  are announced:
A = 0
J, K, Q = 10, 10, 10

DECK_OF_CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, A, J, Q, K]

PLAYER_CARDS = []


COMPUTER_CARDS = []
sumComputer = 0

SPLIT = 0

splitCount = 0
#3. Player's first draw
xP = int(DECK_OF_CARDS[random.randint(0, 13)])
yP = int(DECK_OF_CARDS[random.randint(0, 13)])
xC = int(DECK_OF_CARDS[random.randint(0, 13)])
yC = int(DECK_OF_CARDS[random.randint(0, 13)])

if xP == 0:
    xP = int(input("You got an A, choose 11 or 1: "))
if yP == 0:
    yP = int(input("You got an A, choose 11 or 1: "))
# xC/yC, when they're A, are given random values between 11 or 1:

if xC == 0:
    randomChoice = [1, 11]
    xC = int(randomChoice[random.randint(0, 1)])
if yC == 0:
    randomChoice = [1, 11]
    yC = int(randomChoice[random.randint(0, 1)])

    
PLAYER_CARDS.append(xP)

PLAYER_CARDS.append(yP)


firstDraw = 0
print("Your first 2 cards: ", PLAYER_CARDS)
print("Computer's first card: ", xC)

# splitting option on first draw (check 5. for more information)
if  xP == yP:
    splitA = [xP]
    splitB = [yP]
    SPLIT = int(input("Do you want to split? 1 for yes, 0 for no: "))
    
    splitCount = 1

else:
    splitCount = 0
    




                
#4. Player Consecutive Draws
while DRAWP == 1:
  
    #5. Player Splitting (rest of cards) phase:
    # firstDraw is only true if the first 2 cards were the same value.
    
    
    if splitCount == 0:
        for i in range(len(PLAYER_CARDS)):
            for j in range(len(PLAYER_CARDS)):
                if PLAYER_CARDS[(i - 2)] == PLAYER_CARDS [(i - 1)] and splitCount == 0:
                    #splitA, splitB defined, choice to split
                    splitA = [PLAYER_CARDS[(i-2)]] 
                    splitB = [PLAYER_CARDS[(i-1)]]
                    SPLIT = int(input("Do you want to split? 1 for yes, 0 for no: "))
                    if SPLIT == 0:
                        break
                    break
            if SPLIT == 0:
                break
                
                    
        if PLAYER_CARDS[(i-1)] == PLAYER_CARDS[(i-2)] or xP == yP: #prevents running it twice
            break
            
                
        

    # initially, drawSplitA and ... are 0
    if SPLIT == 1:
        drawSplitA = 0
        sumA = 1 # ensures if statement runs only when splitA = splitB
        drawSplitB = 0
        sumB = 0

    #splitting process
    
    while SPLIT == 1:
        if sumA == sumB:
            sumPlayer = sumA
            PLAYER_CARDS = [sumPlayer]
            DRAWP = 0
            print("Your sums are equal. Previous hand will be shown with overall hand Value: ", sumPlayer)
            SPLIT == 0
            splitCount == 1
            
            break
   
        if drawSplitB == 0:
            drawSplitA = int(input ("start drawing (from the left side ?) 1 for yes, 0 for no: "))
        
        while drawSplitA == 1 and SPLIT == 1:
            if drawSplitA != 1:
                break
            A = int(DECK_OF_CARDS[random.randint(0, 13)])
            if A == 0:
                A = int(input("You got an A, choose 11 or 1: "))
            splitA.append(A)
            print("left hand: " + str(splitA))

            sumA = 0 # ensures loop starts at 0
            for i in splitA:
                sumA = sumA + int(i)
            if sumA > 21:
                print("You busted in split (left hand) ")
                exit()
            
            drawSplitA = int(input("press 1 to draw, or 0 to hold (for your left hand): "))
            if drawSplitA != 1:
                break
              
        # works only after 1st hand is finished
        drawSplitB = int(input("press 1 to draw, or 0 to hold (for your right hand): "))
            
        while drawSplitB == 1 and SPLIT == 1:
            if drawSplitB != 1:
                break
            B = int(DECK_OF_CARDS[random.randint(0, 13)])
            if B == 0:
                 B = int(input("You got an A, choose 11 or 1: "))
            splitB.append(B)
            print("right hand: " + str(splitB))
            
            sumB = 0 # makes sure the loop below starts at 0
            for i in splitB:
                sumB = sumB + int(i)
            if sumB > 21:
                print("You busted in split (right hand)")
                exit()
            
            drawSplitB = int(input("press 1 to draw, or 0 to hold (for your right hand): "))
            

        if sumA != sumB:
            print("left hand is not the same as right hand. Back to drawing... ")
            
            print("Your cards so far: ", PLAYER_CARDS)
            SPLIT == 0
            splitCount == 1
            break

        

    DRAWP = int(input("type 1 for draw, 0 for hold: "))
    if DRAWP == 0: # breaks out of playet drawing
        break
    
    # 6. Drawing process
    
    zP = int(DECK_OF_CARDS[random.randint(0, 13)]) #consecutive cards added
        
    if zP == 0:
        zP = int(input("You got an A, choose 11 or 1: ")) # makes sure consecutive card
            
    PLAYER_CARDS.append(zP)
    print("Your cards so far: ", PLAYER_CARDS)
        
        
    # 7. Hold condition (breaks out draw  condition)  
    if DRAWP == 0:
        print("You are holding, here are the cards so far: ", PLAYER_CARDS)
        break
    
    
            
    # 8. Fail condition
    sumPlayer = 0
    for i in PLAYER_CARDS:
        sumPlayer = sumPlayer + int(i)
        
    if sumPlayer > 21:
        print("Your cards " + str(PLAYER_CARDS) + " sum up to: " + str(sumPlayer))
        print("You bust")
        exit()

    if DRAWP == 0:
        print("Dealer's (computer) turn")
        print("Your cards: ", PLAYER_CARDS)
        break
    

      

#8. computer draw condition
DRAWC = 1
sumComputer = xC + yC # sumComputer is initially first 2 cards
zC = 0 # new card initially doesn't exist
COMPUTER_CARDS = [xC, yC]
if sumComputer <= 17 and DRAWC == 1:       
    while DRAWC == 1:
        #computer fail state
        if sumComputer > 21:
            print("Dealer's cards " + str(COMPUTER_CARDS) + " sum up to: " + str(sumComputer))
            print("Computer loses, you win!")
            exit()
        if sumComputer >= 17: # control clause
            drawC = 0
            break
        
        
        
        zC = int(DECK_OF_CARDS[random.randint(0, 13)])
        
        if zC == 0: # random choice when zC (new cards) is A
            randomChoice = [1, 11]
            zC = int(randomChoice[random.randint(0, 1)])
            
        COMPUTER_CARDS.append(zC)
        
        #computer sum 
        sumComputer = sumComputer + zC
        
        
       

       
        
       
        
        
        
            
    
        

    
        
        
        
# sumPlayer wasn't defined outside of that loop. Maybe because it was defined in nested loop
sumPlayer = 0     
for i in PLAYER_CARDS:
    sumPlayer = sumPlayer + int(i)
print("This is your card sum: " + str(sumPlayer) + "\n")
if sumComputer >= 17:
    print("these are the dealer's cards: ", COMPUTER_CARDS)
    print("ComputerSum: ", str(sumComputer))
    
    for i in PLAYER_CARDS:
        if i == 0:
            i == int(input("there's an A choose 1 or 11: "))
            
    if sumComputer > sumPlayer:
        print("Computer wins")
        exit()
    if sumPlayer > sumComputer:
        print("You win")
        exit()
    if sumPlayer == sumComputer:
        print("It's a tie")
        exit()
    if sumPlayer > 21:
        print("You got over 21, therefore you've lost!")
        exit()

import random

deck = []
icons = ["♠","♥","♦","♣"]
hand = []

def buildNewDeck():
    global deck
    global icons

    for i in range (4):
        deck.append(icons[i]+"A")
        for j in range (9):
            deck.append(icons[i]+str((j+2)))
        deck.append(icons[i]+"J")
        deck.append(icons[i]+"Q")
        deck.append(icons[i]+"K")

buildNewDeck()
#print(deck)

def dealCards(count):
    global deck
    for i in range (count):
        pickedCard = random.randint(0, len(deck))
        hand.append(deck[pickedCard])
        deck.pop(pickedCard)

dealCards(2)

print(hand)

def calculateValue(hand):
    totalValue = 0
    
    for i in range (len(hand)):
        hand[i] = (hand[i])[1:]
        #print (hand[i])
        if (hand[i]) == "J" or (hand[i]) == "Q" or (hand[i]) == "K":
            cardVal = 10
        elif (hand[i]) == ("A"):
            cardVal = 11        
        else:
            cardVal = (hand[i])   
        totalValue = totalValue + int(cardVal)
    print ("Value:",(totalValue))

calculateValue(hand)

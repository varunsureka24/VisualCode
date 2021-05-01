import random
import math
import time

#These are the three arrays I use for the various boards
EnemyBoard = [100] #stores enemy ships
MyBoard = [100] #user ships
ShotBoard = [100] #user shoots here

#These are global variables that I use for counting if a ship has been sunk. 
#E stands for enemy and these variables are called in the UserInput() function
ECarrierSunk = 0
EBattleshipSunk = 0
ECruiserSunk = 0
ESubmarineSunk = 0
EDestroyerSunk = 0

#U stands for user and these variables are called in the AIshoots() function
UCarrierSunk = 0
UBattleshipSunk = 0
UCruiserSunk = 0
USubmarineSunk = 0
UDestroyerSunk = 0

#These are colors for when I print the board
RESET = "\u001B[0m" #resets to white
RED = "\u001B[31m" #sets color to red
BLUE = "\u001B[34m" #sets color to blue

def clearField(): #intializes the arrays
    for i in range(100):
        EnemyBoard.insert(i, ' ')
        MyBoard.insert(i, ' ')
        ShotBoard.insert(i, ' ')

def drawUserField(): # this is the function I use to print the user field
    print("  .a.b.c.d.e.f.g.h.i.j.")
    for i in range(100):
        if (i % 10 == 0):
            if (i != 0):
                print("")
            for dash in range(23):
                print("-", end="")
            print("")
            if ((i//10)+1 == 10):
                print((i//10)+1, "|", end="", sep="")
            else:
                print((i//10)+1, " |", end="", sep="")
        marker = MyBoard[i]
        if (marker == 'X'): #hit = red
            print(RED + marker, end="")
        elif (marker == 'O'): #miss = blue
            print(BLUE + marker, end="")
        else: 
            print(marker, end="")
        print(RESET + "|", end="") #resets to white
    print("")
    for dash in range(23):
        print("-", end="")
    print("")


def drawShotBoard(): #where the user shoots            
    print("  .a.b.c.d.e.f.g.h.i.j.") 
    for i in range(100):
        if (i % 10 == 0):
            if (i != 0):
                print("")
            for dash in range(23):
                print("-", end="")
            print("")
            if ((i//10)+1 == 10):
                print((i//10)+1, "|", end="", sep="")
            else:
                print((i//10)+1, " |", end="", sep="")
        marker = ShotBoard[i] #uses ShotBoard[] instead
        if (marker == 'X'):  #hit = red
            print(RED + marker, end="")
        elif (marker == 'O'): #miss = blue
            print(BLUE + marker, end="")
        else:
            print(marker, end="")
        print(RESET + "|", end="") #the color resets here
    print("")
    for dash in range(23):
        print("-", end="")
    print("")


def positionCalc(spot): #translates coordinates into a position
    x = ord(spot[0].lower()) - 97 #calculates x position
    y = int(spot[1]) #calculates y position
    position = ((y-1) * 10) + (x) #calculates position
    return position 





#-------------------------------------------------# Enemy Ship Functions
#checks to see if there is enough space for an enemy ship to be placed
def EpositionChecker(position, lengthOfShip, direction, shipCharacter): 
    for x in range(lengthOfShip): 
        if (direction == 1): #horizontal
            #prevents ship from printing off side
            if ((position % 10) + lengthOfShip > 10): 
                return False
                #checks if spaces are clear
            if (EnemyBoard[position +  x] != ' '): 
                return False
        else: #vertical
            #doesn't print out of the grid vertically.
            if ((math.floor(position / 10)) + lengthOfShip > 10): 
                return False
            #spaces bellow the ship are empty.
            if (EnemyBoard[position + (x*10)] != ' '): 
                return False
    #fills the array with the ship
    EshipPlacer(position, lengthOfShip, direction, shipCharacter) 
    return True

#this function prints the ship and is called in the function above. 
def EshipPlacer(position, lengthOfShip, direction, shipCharacter):
    for x in range(lengthOfShip): #it runs for the length of the ship
        EnemyBoard[position] = shipCharacter
        if (direction == 1): #horizontal
            position +=1 #prints to the right
        else:              #vertical
            position +=10 #prints down


def randomizeShips(): #this function randomizes the ships. 
    tempBool = False
    #these while loops guarantee that the ship is placed correctly
    while(not tempBool):
        ECarrierPos = random.randint(0,99)
        ECarrierDir = random.randint(1,2)
        #this is where i check to see if the ship can be placed there
        tempBool = EpositionChecker(ECarrierPos, 5, ECarrierDir, 'C') 
    
    tempBool = False
    while(not tempBool):
        EBattleshipPos = random.randint(0,99)
        EBattleshipDir = random.randint(1,2)
        tempBool = EpositionChecker(EBattleshipPos, 4, ECarrierDir, 'B')
    
    tempBool = False
    while(not tempBool):
        ECruiserPos = random.randint(0,99)
        ECruiserDir = random.randint(1,2)
        tempBool = EpositionChecker(ECruiserPos, 3, ECruiserDir, 'c')
    
    tempBool = False
    while(not tempBool):
        ESubmarinePos = random.randint(0,99)
        ESubmarineDir = random.randint(1,2)
        tempBool = EpositionChecker(ESubmarinePos, 3, ESubmarineDir, 'S')
    
    tempBool = False
    while(not tempBool):
        EDestroyerPos = random.randint(0,99)
        EDestroyerDir = random.randint(1,2)
        tempBool = EpositionChecker(EDestroyerPos, 2, EDestroyerDir, 'D')



#-------------------------------------------------# User Ship Functions

#main algorithem
#this function checks to see if the user can place ships where they picked.
def UpositionChecker(position, lengthOfShip, direction, shipCharacter):  
    if (direction == 1): #vertical
        #it checks the amount of spaces that the ship would take up
        for x in range(lengthOfShip):
            #checks to see if the spots bellow are clear
            if (MyBoard[position + (x*10)] != ' '): 
                return False
    else: #horizontal
        #it checks the amount of spaces that the ship would take up
        for x in range(lengthOfShip):
            #checks to see if the spots to the right of the ship are clear
            if (MyBoard[position +  x] != ' '):
                return False
    #fills the array
    UshipPlacer(position, lengthOfShip, direction, shipCharacter) 
    return True
    
     
#fills array
def UshipPlacer(position, lengthOfShip, direction, shipCharacter):
    #it runs for the length of the ship
    for x in range(lengthOfShip):
        if (direction == 1): #vertical
            #fills the array with the ship values vertically
            MyBoard[position + (x*10)] = shipCharacter 
        else: #horizontal
            #fills the array with the ship values horizontally
            MyBoard[position + x] = shipCharacter 


#-------------------------------------------------# Shooting Functions
#this function uses where the user shoots to determine if they can shoot there
#also determines if you sink any enemy ships
def UserInput(shot): 
    position = positionCalc(shot) 

    #global so that I can modify them here.
    #they determine if any of the ships have been sunk
    global ECarrierSunk
    global EBattleshipSunk
    global ECruiserSunk
    global ESubmarineSunk
    global EDestroyerSunk


    #if the user has already shot at they position that they picked
    if (ShotBoard[position] == 'X' or ShotBoard[position] == 'O'): 
        print("you already shot there!")
        time.sleep(1)
        return False
    else: #these statements check to see if the user hit an enemy ship
        if (EnemyBoard[position] == 'C'): #if carrier
            ShotBoard[position] = 'X'
            ECarrierSunk +=1
            if (ECarrierSunk == 5):
                print("You have sunk their carrier!")
                time.sleep(1)

        elif (EnemyBoard[position] == 'B'): #if battleship
            ShotBoard[position] = 'X'
            EBattleshipSunk +=1
            if (EBattleshipSunk == 4):
                print("You have sunk their battleship!")
                time.sleep(1)

        elif (EnemyBoard[position] == 'c'): #if cruiser
            ShotBoard[position] = 'X'
            ECruiserSunk +=1
            if (ECruiserSunk == 3):
                print("You have sunk their cruiser!")
                time.sleep(1)

        elif (EnemyBoard[position] == 'S'): #if submarine
            ShotBoard[position] = 'X'
            ESubmarineSunk +=1
            if (ESubmarineSunk == 3):
                print("You have sunk their submarine!")
                time.sleep(1)

        elif (EnemyBoard[position] == 'D'): #if destroyer
            ShotBoard[position] = 'X'
            EDestroyerSunk +=1
            if (EDestroyerSunk == 2):
                print("You have sunk their destroyer!")
                time.sleep(1)
        else: #if the user missed
            ShotBoard[position] = 'O'
        return True

#this function determines where the AI shoots
def AIshoots():
    #picks a random spot between 1 and 99
    position = random.randint(0,99)

    #global so that I can modify them here.
    #they determine if any of the ships have been sunk
    global UCarrierSunk 
    global UBattleshipSunk
    global UCruiserSunk
    global USubmarineSunk
    global UDestroyerSunk

    #if the AI shoots in a spot that it has already shot, it will move over to the right and test again
    while (MyBoard[position] == 'X' or MyBoard[position] == 'O'):
        if (position > 99):
            position = 0
        else:
            position +=1
    
    #these statements check to see if the enemy hit a user ship
    if (MyBoard[position] == 'C'): #if carrier
        MyBoard[position] = 'X'
        UCarrierSunk +=1
        if (UCarrierSunk == 5):
            print("The AI has sunk your carrier!")
            time.sleep(1)

    elif (MyBoard[position] == 'B'): #if battleship
        MyBoard[position] = 'X'
        UBattleshipSunk +=1
        if (UBattleshipSunk == 4):
            print("The AI has sunk your  battleship!")
            time.sleep(1)

    elif (MyBoard[position] == 'c'): #if cruiser
        MyBoard[position] = 'X'
        UCruiserSunk +=1
        if (UCruiserSunk == 3):
            print("The AI has sunk your cruiser!")
            time.sleep(1)

    elif (MyBoard[position] == 'S'): #if submarine
        MyBoard[position] = 'X'
        USubmarineSunk +=1
        if (USubmarineSunk == 3):
            print("The AI has sunk your submarine!")
            time.sleep(1)

    elif (MyBoard[position] == 'D'): # if destroyer
        MyBoard[position] = 'X'
        UDestroyerSunk +=1
        if (UDestroyerSunk == 2):
            print("The AI has sunk your destroyer!")
            time.sleep(1)
        
    else: #if the AI misses
        MyBoard[position] = 'O'
    drawUserField() #draws the user's board so that they can shoot next
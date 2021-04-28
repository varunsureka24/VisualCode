import random
import math
import time

#These are the three arrays I use for the various boards
EnemyBoard = [100] #This is necessary to store the enemy ships. I randomize them and then place them in here
MyBoard = [100] #This is necessary for the user's ships. After the user picks a position and direction for the ships, they are stored here
ShotBoard = [100] #this is the array that the user shoots on to. This allows me to keep the enemy board secret

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
RESET = "\u001B[0m" #this resets the color back to white
RED = "\u001B[31m" #this sets the color to red. Used when you or the AI hits a ship
BLUE = "\u001B[34m" #this sets the color to blue. Used when you or the AI misses the ship

def clearField(): #this fills the array with blank characters. This is necessary because it allows me 
                  #to print a space for that spot when I print the boards
                  #additionally, filling the boards here allows me to keep the boards global so that i can use them in other functions
    for i in range(100):
        EnemyBoard.insert(i, ' ')
        MyBoard.insert(i, ' ')
        ShotBoard.insert(i, ' ')

def drawUserField(): # this is the function I use to print the user field
    print("  .a.b.c.d.e.f.g.h.i.j.") # the string at the top that tells you the x coordinates

    for i in range(100): #this is for the values in the array. There are 100 array spots and each one corrisponds to an array index
        if (i % 10 == 0):
            if (i != 0):
                print("")

            for dash in range(23): #this prints the lines between the rows
                print("-", end="")

            print("")

            if ((i//10)+1 == 10): #this for loop allows me to print the numbers that indicate the y coordinates
                print((i//10)+1, "|", end="", sep="")
            else:
                print((i//10)+1, " |", end="", sep="")
        
        marker = MyBoard[i] #this takes the value at each index in the array and stores it as a character
        if (marker == 'X'): #if it is a hit, then the marker is colored red
            print(RED + marker, end="")
        elif (marker == 'O'):- #if it is a miss, the marker is colored blue
            print(BLUE + marker, end="")
        else: 
            print(marker, end="")
        print(RESET + "|", end="") #then it resets the color of the marker to white

    print("")
    for dash in range(23):
        print("-", end="")
    print("")


def drawShotBoard(): #this is the board that the user shoots on. it is destinct from the enemy board because 
                     #i store the values for the enemy ships on the enemy board and I cant have those print out.
    print("  .a.b.c.d.e.f.g.h.i.j.") #this code is extremly similar to the the code above because the grid is designed to look the same.

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
        
        marker = ShotBoard[i] #the main difference is the fact that i use the shot board array here
        if (marker == 'X'):  #if the user hits an enemy ship it will be printed in red
            print(RED + marker, end="")
        elif (marker == 'O'): #if the user misses the enemy, it will be printed in blue
            print(BLUE + marker, end="")
        else:
            print(marker, end="")
        print(RESET + "|", end="") #the color resets here

    print("")
    for dash in range(23):
        print("-", end="")
    print("")

def positionCalc(spot): #this function calculates the position that the user has chosen. 
    x = ord(spot[0].lower()) - 97 #this uses the ord() function which returns the ascii value for the character that you give it. 
                                  #Then i subtract 97 from it because i need 'a' to equal 0 so that a1 is the first index of the array
    y = int(spot[1]) #this converts the second character in the string 'shot' into an integer. It gives me the y value of the spot that they have chosen
    position = ((y-1) * 10) + (x) #this equation converts the x and y values of where the user shot into a number out of 100. That number corresponds to the position of the shot in the array.
    return position #returns the value of the shot.

#-------------------------------------------------# Enemy Ship Functions

def EpositionChecker(position, lengthOfShip, direction, shipCharacter): #this is the primary algorithem for the enemy ships. It checks to see if there is enough space for an enemy ship to be placed
                                        #it takes 4 parameters:
                                            #position is where in the array the ship wants to be placed. This is randomized in the randomizeShips() function bellow.
                                            #lengthOfShip is a constant that is provided in the randomizeShips() function. i.e. the carrier has a lengthOfShip value of 5, the battleship has a value of 4, etc.
                                            #direction is the direction that the ship will point. it is important because it tells the fuction if it should check to the right of the position, if direction = 1, or bellow, if direction = 2
                                            #shipCharacter is the character that will be printed for the ship. It is important because it allows the user and the computer to differentiate which ship is whihc. 
                                            
    for x in range(lengthOfShip): #runs for the length of the ship. It checks only the spots that the ship would fit in
        if (direction == 1): #if direction == 1, then it is printing horizontally
            if ((position % 10) + lengthOfShip > 10): #this if condition checks to see if the ship prints off of the side of the grid. The ship can only print in one row, it cant spill over to the next row
                return False
            if (EnemyBoard[position +  x] != ' '): #this checks to see if the spots next to the ship aren't blank, i.e. there is another ship there
                return False
        else: #if the ship is printing vertically
            if ((math.floor(position / 10)) + lengthOfShip > 10): #this checks to make sure the ship doesn't print out of the grid vertically. Also chekcs to make sure the ship doesn't try to print in indexs that the array doesn't have preventing segmentation faults.
                return False

            if (EnemyBoard[position + (x*10)] != ' '): #this make sures the spots bellow the ship are empty.
                return False
    EshipPlacer(position, lengthOfShip, direction, shipCharacter) #this calls another function which then fills the array with the ship
    return True

def EshipPlacer(position, lengthOfShip, direction, shipCharacter): #this function prints the ship and is called in the function above. 
    for x in range(lengthOfShip): #it runs for the length of the ship
        EnemyBoard[position] = shipCharacter #it prints the character that is associated with each ship
        if (direction == 1): #horizontal
            position +=1 #prints to the right
        else:              #vertical
            position +=10 #prints down


def randomizeShips(): #this function randomizes the ships. 
    tempBool = False
    while(not tempBool): #these while loops guarantee that the ship is placed correctly
        ECarrierPos = random.randint(0,99)
        ECarrierDir = random.randint(1,2)
        tempBool = EpositionChecker(ECarrierPos, 5, ECarrierDir, 'C') #this is where i check to see if the ship can be placed there
    
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
def UpositionChecker(position, lengthOfShip, direction, shipCharacter): #this function checks to see if the user can legally place their ships at the spot that they pick. 
    if (direction == 1): #vertical
        for x in range(lengthOfShip): #it checks the amount of spaces that the ship would take up
            if (MyBoard[position + (x*10)] != ' '): #checks to see if the spots bellow are clear
                return False
    else: #horizontal
        for x in range(lengthOfShip): #it checks the amount of spaces that the ship would take up
            if (MyBoard[position +  x] != ' '): #checks to see if the spots to the right of the ship are clear
                return False
    UshipPlacer(position, lengthOfShip, direction, shipCharacter) #calls another function to fill the array with the ship values
    return True 

def UshipPlacer(position, lengthOfShip, direction, shipCharacter): #this is the function that is called above
    for x in range(lengthOfShip): #it runs for the length of the ship
        if (direction == 1): #vertical
            MyBoard[position + (x*10)] = shipCharacter #fills the array with the ship values vertically
        else: #horizontal
            MyBoard[position + x] = shipCharacter #fills the array with the ship values horizontally


#-------------------------------------------------# Shooting Functions

def UserInput(shot): #this function uses where the user shoots to determine if they can shoot there, and then it also checks to see if you have sunk any of their ships
    position = positionCalc(shot) #calculates the position for where the user shot.

    #these variables have to be declared as global so that I can modify them here.
    #they determine if any of the ships have been sunk
    global ECarrierSunk
    global EBattleshipSunk
    global ECruiserSunk
    global ESubmarineSunk
    global EDestroyerSunk

    if (ShotBoard[position] == 'X' or ShotBoard[position] == 'O'): #if the user has already shot at they position that they picked
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

def AIshoots(): #this function determines where the AI shoots
    position = random.randint(0,99) #picks a random spot between 1 and 99

    #these variables have to be declared as global so that I can modify them here.
    #they determine if any of the ships have been sunk
    global UCarrierSunk 
    global UBattleshipSunk
    global UCruiserSunk
    global USubmarineSunk
    global UDestroyerSunk

    while (MyBoard[position] == 'X' or MyBoard[position] == 'O'): #if the AI shoots in a spot that it has already shot, it will move over to the right and test again
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
import battleship 
import time

battleship.clearField() #initiallizes the arrays
battleship.randomizeShips() #randomizes enemy ships
battleship.drawUserField() #prints the user's board

#these while loops ask the user for a position to place their ship, and then a direction
tempBool = False
while(not tempBool):
    ShipPos = input("Where do you want to place your carrier (5 long)? Enter a start point (enter the column then the row. Example: a1 or f8)")
    ShipDir = input("Enter a direction (\u001B[31m1\u001B[0m is vertical and goes down. \u001B[31m2\u001B[0m is horizontal and goes to the right)")
    tempBool = battleship.UpositionChecker(battleship.positionCalc(ShipPos), 5, int(ShipDir), 'C') #this statement checks to see if the ship can be printed there
battleship.drawUserField()

tempBool = False
while(not tempBool):
    ShipPos = input("Where do you want to place your battleship (4 long)? Enter a start point (enter the column then the row. Example: a1 or f8)")
    ShipDir = input("Enter a direction (\u001B[31m1\u001B[0m is vertical and goes down. \u001B[31m2\u001B[0m is horizontal and goes to the right)")
    tempBool = battleship.UpositionChecker(battleship.positionCalc(ShipPos), 4, int(ShipDir), 'B')
battleship.drawUserField()

tempBool = False
while(not tempBool):
    ShipPos = input("Where do you want to place your carrier (3 long)? Enter a start point (enter the column then the row. Example: a1 or f8)")
    ShipDir = input("Enter a direction (\u001B[31m1\u001B[0m is vertical and goes down. \u001B[31m2\u001B[0m is horizontal and goes to the right)")
    tempBool = battleship.UpositionChecker(battleship.positionCalc(ShipPos), 3, int(ShipDir), 'c')
battleship.drawUserField()

tempBool = False
while(not tempBool):
    ShipPos = input("Where do you want to place your submarine (3 long)? Enter a start point (enter the column then the row. Example: a1 or f8)")
    ShipDir = input("Enter a direction (\u001B[31m1\u001B[0m is vertical and goes down. \u001B[31m2\u001B[0m is horizontal and goes to the right)")
    tempBool = battleship.UpositionChecker(battleship.positionCalc(ShipPos), 3, int(ShipDir), 'S')
battleship.drawUserField()

tempBool = False
while(not tempBool):
    ShipPos = input("Where do you want to place your destroyer (4 long)? Enter a start point (enter the column then the row. Example: a1 or f8)")
    ShipDir = input("Enter a direction (\u001B[31m1\u001B[0m is vertical and goes down. \u001B[31m2\u001B[0m is horizontal and goes to the right)")
    tempBool = battleship.UpositionChecker(battleship.positionCalc(ShipPos), 2, int(ShipDir), 'D')
battleship.drawUserField()

time.sleep(1)
battleship.drawShotBoard() #this draws the board that the user will shoot on.

#two booleans that test to see if the game is over
enemyShipsRemaining = True
myShipsRemaining = True

while (enemyShipsRemaining and myShipsRemaining): #while there are still ships remaining
    EnemyShipCounter = 0
    UserShipCounter = 0

    while(True): #asks the user where they want to shoot and tests to see if they can shoot there
        shot = input("Where do you want to shoot?")
        if (battleship.UserInput(shot)):
            break
    battleship.drawShotBoard() #prints the board where they shot

    #now the AI shoots
    time.sleep(0.5)
    print("AI is shooting")
    for x in range(3):
        print(".")
        time.sleep(1)

    battleship.AIshoots()
    time.sleep(1.5)
    battleship.drawShotBoard()

    #these statements check to see if there are still ships remaining. 
    for x in range(100):
        if (battleship.ShotBoard[x] == 'X'):
            EnemyShipCounter +=1
            if (EnemyShipCounter == 17): #if EnemyShipCounter == 17, then you have sunk all of the enemy ships and the game is over
                enemyShipsRemaining = False
                print("you have won!")

        elif(battleship.MyBoard[x] == 'x'):
            UserShipCounter += 1
            if(UserShipCounter == 17): #if UserShipCounter == 17, then the AI has sunk all of your ships and the game is over
                myShipsRemaining = False
                print("the AI has won!")
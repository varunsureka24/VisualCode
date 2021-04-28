        if ((position % 10) + lengthOfShip > 10): #Prevents the ship from "spilling over" into the next row.
                return False
        if ((math.floor(position / 10)) + lengthOfShip > 10): #prevents the ship from printing outside of the bounds of the array
                return False
########################  Find the treasure map  ########################
print ("Welcome to treasure Island.")
print ("Your mission is to find the treasure.")
side = input ("Left or Right: ")
if side == "right":
    print ("Game Over.")
if side == "left":
    side1 = input ("Swim or Wait: ")
    if side1 == "swim" :
        print ("Game Over.")
    if side1 == "wait" :
        side2 = input ("Which door? Red/Blue/Yellow :")
        if side2 == "red" or side2 == "blue":
            print ("Game over.")
        if side2 == "yellow" :
            print ("You win.")
        else :
            print("You broke the rules of the game.")
    else :
        print("You broke the rules of the game.")
else :
    print ("You broke the rules of the game.")

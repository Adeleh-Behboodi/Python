
import random

comp_choice = random.randint(1,3)
print("Winning Rules of the Rock paper scissor game as follows: \n"
                    + "Rock & paper -> paper wins \n"
                    + "Rock & scissor -> Rock wins \n"
                    + "paper & scissor -> scissor wins \n")
counter = 1
while counter <=5 : # user play 5 times
        comp_choice = random.randint(1, 3)
        choice = int(input("User turn: "))
        counter += 1
        if choice == 1 :
            choice_name = "Rock"
        elif choice == 2:
            choice_name = "Paper"
        elif choice == 3:
            choice_name = "Scissor"
        else :
            choice_name = "Invalid"
            choice = 0
            print ("You broke the rules of the game .")
        print("User choice is: " + choice_name)
        if comp_choice == 1 :
            comp_choice_name = "Rock"
        elif comp_choice == 2:
            comp_choice_name = "Paper"
        else:
            comp_choice_name = "Scissor"
        print("Computer choice is : " + comp_choice_name)
        if comp_choice == choice:
             print(choice_name + " V/s " + comp_choice_name)
        elif ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
             print("paper wins => ")
             result = "Paper"
        elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
             print("Rock wins =>")
             result = "Rock"
        elif choice == 0 :
             print(comp_choice_name + " wins => and You broke the rules of game .")
             result = comp_choice_name
print("\nThanks for playing")
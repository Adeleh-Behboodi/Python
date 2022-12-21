########## guess a number game ##########
print ("""
                                50     ?       1
                        28           10
            12                _     _       ?            44
                     2       ( \---/ )             11
                ?       16    ) . . (               39
________________________,--._(___Y___)_,--._______________________ 
              49        `--'           `--'
                         37         31           ?

""")
import random

random_number = random.randint(1,50)
print (random_number)
print ("You can guess just 5 number . ")
guess_number = int( input ("Guess a number (1,50) : "))
guess_try = 1  # number of guesses
while random_number != guess_number : # until user do not guess correctly
    if guess_number < random_number :
         print ("You guessed the low number ! ")
    elif guess_number > random_number :
         print ("You guessed the high number !")
        # print("We can help you but 1 your choice. Yes/No ? ")
    guess_number = int ( input ("You can guess a number again : "))
    guess_try += 1 # add to number of guesses
    if guess_try == 7:
        print ("You lose.")
        break # exit of while
else : # until the user guessed correctly
    print (f" **********   CONGRATILATION   ********** You win after {guess_try} times ********** ")

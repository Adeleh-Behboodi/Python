########################  computing bill for pizza order  ########################
print ("Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.")
size = input ("size pizza: ") # s (small) m(Medium) l(large)
pepperoni = input ("Do you want add_pepperoni pizza ?  ") # y / n
extra_cheese = input ("Do you want extra_cheese on the pizza ?  ") # y/n
if size == "l" : #large
    amount = 25
    #print(amount)
if size == "m" : #medium
    amount = 20
    #print(amount)
if size == "s" : #small
    amount = 15
    #print (amount)
else :
    amount = 0
if pepperoni=="y" :
    amount = amount + 2
else :
    amount = amount
if extra_cheese=="y" :
    amount =amount+1
else:
    print (" you have simple pizza without extra_cheese .")
amount = str(amount)
print ("Your bill : " + amount)
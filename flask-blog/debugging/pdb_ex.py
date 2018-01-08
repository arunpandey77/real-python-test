import sys
from random import choice
import pdb
random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]
while(True):
    print("To Exit this game type 'exit' ")
    #pdb.set_trace()
    num1 = choice(random2)
    num2 = choice(random1)
    answer = int(input("what is {} times {} ".format(num1,num2)))

    if answer == "exit":
        print("exiting")
        sys.exit()
    elif(answer == num1*num2):
        print("correct")
    else:
        print("Wrong!")

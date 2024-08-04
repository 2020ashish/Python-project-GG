import random
import math
print("Enter a range of value")
n1 =  int(input("Enter first number : "))
n2 =  int(input("Enter Second number : "))

if n1 < n2:
   n1 = n1 + n2 
   n2 = n1 - n2
   n1 = n1 - n2
x =  random.randint(n2,n1)
chances = math.ceil(math.log(n1-n2+1,2))

flag =  False
count = 0
print("\nYou've only ", chances, " chances to guess the integer!\n")
while( count < chances):
    count+=1
    guess =  int(input("Enter guess number : "))
    
    if  guess == x:
        print("Wow ! You guessed the correct number")
        flag = True
        break
    elif (guess > x):
        print("Your guessed too high!")
    else:
        print("Your guessed too less!")
        
if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
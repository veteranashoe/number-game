# ramdom number game

import random
n=int((random.randint(0,100)))

print("You Have 7 Chances to Guess Correctly")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("You Have 6 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("You Have 5 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("You Have 4 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("You Have 3 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("You Have 2 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("You Have 1 Chances Left")
x = int(input("input a number \n > "))
if x>n:
    print("the number is less than " + str(x) + "\n")
if x<n:
    print("the number is more than " + str(x) + "\n")
if x==n:
    print("Congrulations You Guessed the Right Number")

print("This is Your Last Chance")
x = int(input("input a number \n > "))
if x>n:
    print("You Lost The Game Try Again \n")
if x<n:
    print("You Lost The Game Try Again \n")
if x==n:
    print("Congrulations You Guessed the Right Number")
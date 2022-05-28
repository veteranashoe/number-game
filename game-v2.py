import random
n=int((random.randint(0,100)))

print ("\nGuess the correct Random Number \nyou have 7 total chances \nThe Random Number is in between 1-100\n")

c = 6

while c >= 0:
              x = int(input("input a number \n > "))
              if x>n:
                            print("the number is less than " + str(x) + "\n")
                            print("you have " + str(c) + " chances left")
              if x<n:
                            print("the number is more than " + str(x) + "\n")
                            print("you have " + str(c) + " chances left")
              if x==n:
                            print("Congrulations You Guessed the Right Number")
                            c = 0
              elif c == 0 :
                            print("you lost the game. \nThe Number was " + str(n))
                            exit()
              c = c - 1


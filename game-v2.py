import random
n=int((random.randint(0,100)))
print(n)

print ("\nguess the correct random number \nyou have 7 total chances \n")
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
                            print("you lost the game")
                            exit()
              c = c - 1

afaefa
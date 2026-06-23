import random
num=random.randint(1, 50)
secret=num
guess=int(input("Guess The Number: "))
hearts=5
while hearts<=5:
 for j in range (1, 49):
   hearts=hearts-1
if guess == secret:
    print("You Guessed It Correct!")
if guess>1 and guess<=20:
    print("The Number You Entered Is Ice Cold 🧊")
if guess>20 and guess<=30:
    print("The Number You Entered Is Cold 🥶")
if guess>30 and guess<=40:
    print("The Number You Entered Is Warm 🌡️")
if guess>40 and guess<=49:
   print("The Number You Have Entered Is Hot 🔥")
else:
   print("You Have",hearts,"Hearts Left.")
hearts=hearts-1


wallet=int(input("Enter the amount in your wallet: "))
print ("Candy Bar costs 100$")
if wallet>100:
    print("You have enough to buy the candy bar. You will have",wallet-100,"$ left.")
else:  print("You do not have enough to buy the candy bar. You need",100-wallet,"$ more to buy a candy bar")

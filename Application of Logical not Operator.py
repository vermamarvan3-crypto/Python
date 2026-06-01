a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
print(not(a==b))
print(not(a==c))
print(not(b==c))

a1=input("Enter a word: ")
b1=input("Enter another word: ")
if not (a1==b1):
    print(a1,"And",b1,"are not the same word")
else:
    print(a1,"And",b1,"are the same word")

a2=int(input("Enter a number: "))
b2=int(input("Enter another number: "))
if not((a2==1)== (b2==5)):
    print("Hello")

a3=int(input("Enter a number: "))
if not (a3%2==0):
    print(a3,"is an odd number")
else:
    print(a3,"is an even number")

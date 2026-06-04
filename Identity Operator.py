x1=int(input("Enter a number: "))
if(type(x1) is int):
    print("True")
else:
    print("False")
x2=int(input("Enter a number: "))
if(type(x2) is not float):
    print("True")
else:
    print("False")
x3=int(input("Enter a number: "))
y3=int(input("Enter another number: "))
if(x3 is y3):
    print(x3,"And",y3,"have the same identity")
else:
    print(x3,"and",y3,"do not have the same identity")

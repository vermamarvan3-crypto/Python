def sum(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def multi(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
choice=int(input("Enter A Choice: 1,Add 2,Subtract 3,Multiply 4,Divide: "))
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
if choice==1:
    print("Sum Of The Numbers Is",sum(a,b))
elif   choice==2:
    print("Subtraction Of The Numbers Is:",sub(a,b))
elif   choice==3:
    print("Multiplication Of The Numbers Is:",multi(a,b))
elif   choice==4:
    print("Division Of The Numbers Is:",div(a,b))
else:
    print("Invalid Choice")

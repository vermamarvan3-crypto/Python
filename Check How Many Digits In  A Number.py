num=int(input("Enter A Number: "))
count=0
while num>0:
    digit1=num%10
    num//=10
    count+=1
print("The Number Of Digits In The Given Number Is",count)

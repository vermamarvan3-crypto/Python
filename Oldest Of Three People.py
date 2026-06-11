p1=int(input("Enter the age of person 1: "))
p2=int(input("Enter the age of person 2: "))
p3=int(input("Enter the age of person 3: "))
if p1 > p2 and p1 > p3:
    print("Person 1 is the oldest")
elif p2 > p1 and p2 > p3:
    print("Person 2 is the oldest")
elif p3 > p1 and p3 > p2:  
    print("Person 3 is the oldest")

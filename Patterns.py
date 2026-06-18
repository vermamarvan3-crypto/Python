print("Half Pyramid Pattern")
n=int(input("Enter The Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

string=input("Enter a Word: ")
char=input("Enter A Single Character: ")
i=0
count=0
while (i<len(string)):
    if string[i]==char:
        count+=1
    i+=1
print("The Number Of Occurrence Of The Given Character In The Given Word Is",count)


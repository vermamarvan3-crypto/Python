eng=int(input("Enter your score for English: "))
math=int(input("Enter your score for Math: "))
sci=int(input("Enter your score for Science: "))
history=int(input("Enter your score for History: "))
geo=int(input("Enter your score for Geography: "))
total=eng+math+sci+history+geo
average=int(total/5)
validrange=range(0,101)
if average not in validrange:
    print("Invalid Input")
elif average in range(91,101):
    print("Your grade is A1")
elif average in range(81,91):
    print("Your grade is A2")
elif average in range(71,81):
    print("Your grade is B1")
elif average in range(61,71):
    print("Your grade is B2")
elif average in range(51,61):
    print("Your grade is C1")
elif average in range(41,51):
    print("Your grade is C2")
elif average in range(33,41):
    print("Your grade is D")
elif average in range(21,33):
    print("Your grade is E1")
elif average in range(0,21):
    print("Your grade is E2")

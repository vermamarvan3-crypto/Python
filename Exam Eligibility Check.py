a=input("Do you have a medical condition? (Y/N): ")
if a=="Y" or a=="y":
    print("You are not eligible to take the exam.")
else:
    attendance = int(input("Enter your attendance: "))
    if attendance > 75:
        print("You are eligible to take the exam.")
    else:
        print("You are not eligible to take the exam.")

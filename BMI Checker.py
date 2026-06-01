w=int(input("Enter your weight in kg: "))
h=int(input("Enter your height in centimeters: "))
bmi=h*2/w
print("Your BMI is",bmi)
if bmi<18.5:
    print("You are underweight")
else:
    print("You are not underweight")
    if bmi>=25:
        print("You are overweight")
    else:
        print("You are not overweight")

weather=int(input("Enter the temperature in Celsius: "))
if weather>20:
    print("It is warm enough to wear light clothes. If the temprature drops by",weather-20,"Celsius, You should wear heavier Clothes.")
else:
    print("It is not warm enough to wear light clothes. It needs to be",20-weather,"Celsius warmer.")
    if weather<0:
        print("It is freezing. You should wear snow gear.")

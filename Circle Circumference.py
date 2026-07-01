import math
def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumferenc
user_input = input("Enter the radius of the circle: ")
radius_value = float(user_input)
result = calculate_circumference(radius_value)
print(f"The circumference of the circle is: {result:.2f}")

num=int(input("Enter A Number: "))
number = num 
binary_digits = []
for _ in range(number.bit_length()):
    remainder = number % 2         
    binary_digits.append(str(remainder)) 
    number = number // 2            
binary_string = "".join(reversed(binary_digits))

print(binary_string)

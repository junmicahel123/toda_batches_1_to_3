# pseudocode 
# initialization

base_number = 0
exponent_number = 0

# ask user to input two numbers (float)

base_number = float(input("What's the first number?: "))
exponent_number = float(input("What's the second number?: "))

# use the second number as exponent and the first as the base
# base ** exponent
resulting_value = base_number ** exponent_number

# print result

print(f"The result of raising {base_number} to {exponent_number} is -->> {resulting_value}")


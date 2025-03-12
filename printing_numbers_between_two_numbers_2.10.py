# pseudocode 
# initialize number constants
first_number = 0
second_number = 0

# ask user for input numbers

first_number = int(input("Input first number:: "))
second_number = int(input("Input second number:: "))

# use if to make sure
    # if first number is bigger then second
if first_number > second_number:
    first_number, second_number = second_number, first_number
    
# print results
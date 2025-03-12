# pseudocode
# initialize constants 
    # first_number
    # the_rest_of_the_numbers

# ask user for inputs of the 10 numbers
    # user for loop for the 9 other numbers
    # add the numbers to the initialized constant
    # separated from the first number

# minus the first number to the iniatilized constant
# print the results

first_number = 0
the_rest_of_the_numbers = 0


first_number = float(input("Input Number:: "))
 
for the_rest in range(0, 9):
    numbers_2_9_ = float(input("Input Number:: "))
    the_rest_of_the_numbers += numbers_2_9_



difference = first_number - the_rest_of_the_numbers

print(f"The result of difference of the first number minus the rest of the ten numbers \n --> {difference} <--")


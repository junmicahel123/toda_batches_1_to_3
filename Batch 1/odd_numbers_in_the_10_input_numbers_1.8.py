# Pseudocode
# initialization of "total_odd_numbers"

total_odd_numbers = 0

#use for loop to prompt 10 input numbers
# if the number input is odd 
    #add 1 to the total_odd_numbers

for numbers in range(10):
    number_input = float(input(f"Input number {numbers + 1}: "))

    if number_input % 2 != 0:
        total_odd_numbers += 1


#print total_odd_numbers
print(f" The total number of odd in the 10 numbers is -->>  {total_odd_numbers}")
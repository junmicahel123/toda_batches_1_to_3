# pseudocode 
# initialize number constants
# ask user for input numbers
# use if to make sure
    # if first number is bigger then second
# print results

first_number = 0
second_number = 0

first_number = int(input("Input first number:: "))
second_number = int(input("Input second number:: "))

if first_number > second_number:
    first_number, second_number = second_number, first_number


print(f"Numbers between {first_number} and {second_number}:")
for numbers in range(first_number + 1, second_number):
    print(numbers)
    
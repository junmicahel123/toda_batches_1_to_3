# pseudocode
# initialize  number set []

number_set = []

# use while loop for 10 inputs
# use try and except for invalid input checking

# ask user for input numbers
# add number value to set
while len(number_set) < 10:
    try: 
        number = int(input("Enter a number:: "))
        number_set.append(number)
    except ValueError:
        print("Invalid input. restart")
        break
# use min function

lowest_number = min(number_set)

print("The lowest number is", lowest_number)
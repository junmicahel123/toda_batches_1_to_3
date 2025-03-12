# pseudocode
# initialize number listing []
number_list = []
# us for while loop for input numbers
# use try to check invalid inputs
while len(number_list) < 10:
    try:
        numbers = int(input("Input number::"))
        number_list.append(numbers)
    except ValueError:
        print("Invalid input. Restart to try again")

# use sum / len fucntions for average
# print average
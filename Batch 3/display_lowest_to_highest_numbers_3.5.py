# pseudocode 
# initialize number list constant []
number_list = []
# use while loop for number input 10
# use try and except for value checking
# ask for input values
# add to number list

while len(number_list) < 10:
    try:
        number_input = int(input("Enter a number ::"))
        number_list.append(number_input)
    except ValueError:
        print("Invalid input .Restart the program")
        break
# sort numbers
# print the sorted numbers

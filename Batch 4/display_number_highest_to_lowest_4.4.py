# pseudocode 
# initialize number list []
number_list = []
# use while loop for input
# use try for checking invalid inputs

while len(number_list) < 10:
    try:
        numbers = int(input("Input number::"))
        number_list.append(numbers)
    except ValueError:
        print("Invalid input. Restart to try again")
        

# reverse the sort func  for the number list
# print number list
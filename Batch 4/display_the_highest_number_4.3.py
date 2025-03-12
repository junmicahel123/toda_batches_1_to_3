# pseudocode 
# initialize the set number []
number_list = []
# use while loop for input number
while len(number_list) < 10: 
    try:
        number = int(input("Input a number::"))
        number_list.append(number)
    except ValueError:
        print("Invalid input. Restart to try again")
        
# use try loop to check valid inputs
# use max function for number set


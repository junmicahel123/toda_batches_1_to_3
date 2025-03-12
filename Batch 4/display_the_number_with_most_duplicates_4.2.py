# pseudocode
# initialize set []
numbers = []

while len(numbers) < 10:
    try:
        number_input = int(input("Enter number ::"))
        numbers.append(number_input)
    except ValueError:
        print("Invalid input. Restart the program to try again")
        break
    

# use while loop for number inputs 10
# try for checking input
# if numbers 
    # print max number in the set of duplicates
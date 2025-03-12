# pseudocode
# initialize set []
numbers = []
# use while loop for number inputs 10
# try for checking input
while len(numbers) < 10:
    try:
        number_input = int(input("Enter number ::"))
        numbers.append(number_input)
    except ValueError:
        print("Invalid input. Restart the program to try again")
        break



# if numbers 
    # print max number in the set of duplicates

if numbers:
    print("The one with most duplicate is ", max(set(numbers), key=numbers.count))
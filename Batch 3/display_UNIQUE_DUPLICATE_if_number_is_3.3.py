# pseudocode 
# initialize sets number []

number_list = []
count = 0

# use while loop for numbers input
# use try and except to look for invalid inputs
# ask for number
# use if statements to decide wethe unique or duplicate

while count < 10:
    try:
        number = int(input("Enter a number: "))
       
        if number in number_list:
            print("Duplicate")
        else:
            print("Unique")
        #add to set
        count += 1
        number_list.append(number)
    except ValueError:
        print("Invalid input! Stopping.")
        break












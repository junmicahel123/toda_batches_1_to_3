# pseudocode 
# initialize sets number []

number_list = []

# use while loop for numbers input
# use try and except to look for invalid inputs
# ask for number
# use if statements to decide wethe unique or duplicate

while len(number_list) < 10:
    try:
        number = int(input("Enter a number::"))
        if number in number_list:
            print("UNQUE")
        else:
            print("DUPLICATE")
        number_list.append(number)
    except ValueError:
        print("invalid input. TRY AGAIN")
        break
#a add to set

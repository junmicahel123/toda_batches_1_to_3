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
        num = int(input("Enter a number: "))
        number_list.append(num)
        
        
        count += 1
    except ValueError:
        print("Invalid input! Stopping.")
        break

#a add to set
if number_list.count(num) > 0:
    print("Duplicate")
else:
    print("Unique")
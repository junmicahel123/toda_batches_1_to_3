# pseudocode
# initialize 
    # numbers []
    # set ()
    # filtered [] (only one duplicates)

number_list = []
seen = set()
filtered_numbers = []


# use for loop for the inpts
    #  add input to number [] list
    # number not in set ()
         # add to filtered set
for num in range(10):
    numbers = int(input(f"Enter Number {num + 1 }: "))
    number_list.append(numbers)
    if numbers not in seen:
        filtered_numbers.append(numbers)
     

# print result

print("Filtered Numbers are::", filtered_numbers)
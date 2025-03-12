# pseudocode 
# initialize number sets []

numbers_list = []
# use for loop for number input
# add number input to set using append

for number in range(10):
    numbers = int(input("Number input ::"))
    numbers_list.append(numbers)


#  add duplicate set
duplicate_set = []
# if state ment number cout > 1 
if numbers_list.count(numbers) > 1:
    duplicate_set.append(numbers)

    
# add to duplicate set
# print the duplicate set


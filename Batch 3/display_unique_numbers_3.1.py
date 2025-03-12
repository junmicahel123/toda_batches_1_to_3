# pseudocode
# initialize numbers = []
# initialize unique numbers = []
number_list = []
unique_numbers_list = []



# use for loop 
    # for 10 inputs
    # add number input to number list
for numb in range(10):
    numbers = int(input(f"Enter number {numb + 1} ::  "))
    number_list.append(numbers)
# if number.count == 1 
    # add to unique number list = []
for num in number_list:
    if number_list.count(numbers) == 1:
        unique_numbers_list.append(numbers)
# print(unque numbers)

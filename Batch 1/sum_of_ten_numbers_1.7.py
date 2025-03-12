# pseudocode
# initialize the "total_sum" as 0
total_sum = 0

# use "for" loop to ask user to input ten numbers
    # the input numbers will be added to the "total_sum"
for number_input in range(10):
    numbers = float(input(f" Enter the number {number_input + 1}:  "))
    total_sum += numbers

# print the total sum of ten numbers

print(f" The total sum of all ten numbers is -->>{total_sum}")


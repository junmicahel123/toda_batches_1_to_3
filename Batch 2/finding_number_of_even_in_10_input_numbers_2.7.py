# pseudocode
# initiaize constant
    # even_numbers

count_even_numbers = 0


# use for loop to input ten numbers
    # use modulus operation
    # use if conditions
    #       if number % 2 != 1
    # add to even number if true

for number_input in range(10):
    numbers = int(input(f"Input Number {number_input + 1}::  "))

    if numbers % 2 != 1:
        count_even_numbers += 1


# print even_numbers
print(f"The even number count is {count_even_numbers}")


def join_numbers(numbers):
    return ','.join(str(number)
# Applies str to each number and puts
# the new string in the output list
                    for number in numbers)

# Iterates over the elements of numbers
print(join_numbers(range(15)))
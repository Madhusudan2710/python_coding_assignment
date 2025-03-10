def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num  # Add the current number to the running total

    return total

# Test with the sample input
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(f"Sum of {numbers} is: {result}")

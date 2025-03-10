def calculate_average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    
    total = 0 
    count = 0
    for num in numbers:
        total += num  
        count += 1  
    return total / count

# Test with the sample input
numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print(f"Average of {numbers} is: {result}")

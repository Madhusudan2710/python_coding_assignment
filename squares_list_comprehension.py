def generate_squares():
    # List comprehension to generate squares: [expression item =  iterable]
    squares = [i**2 for i in range(1, 11)]
    return squares

# Generate and print the list of squares
result = generate_squares()
print(result)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

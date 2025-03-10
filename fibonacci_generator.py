def get_fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1  # Initialize the first two Fibonacci numbers

    for i in range(n):
        fib_sequence.append(a)  # Append the current Fibonacci number
        a, b = b, a + b  # Calculate the next Fibonacci number

    return fib_sequence

# Test with the sample input
n = int(input("Enter the number of terms: "))
result = get_fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n} terms: {result}") 

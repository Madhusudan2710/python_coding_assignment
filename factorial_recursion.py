def factorial(n):
    # factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# Test with the sample input
num = int( input("Enter a number = "))
result = factorial(num)
print(f"Factorial of {num} is: {result}") 

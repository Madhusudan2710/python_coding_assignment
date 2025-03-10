def is_palindrome(num):
    # To make comparisons easier, convert a number to a string.
    original_num = num
    reversed_num = 0

    # Reverse the number using a while loop
    while num > 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add digit to reversed number
        num = num // 10  # Take the final digit out of the initial number.

    # Check if the original number equals the reversed number
    return original_num == reversed_num

# Test with the sample input
num = 12321
result = is_palindrome(num)
print(f"Is {num} a palindrome? {result}")  # Output: True

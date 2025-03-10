def print_inverted_star_pyramid(height):
    for i in range(height, 0, -1):
        # Print spaces before stars
        spaces = height - i
        print(" " * spaces, end="")
        
        # Print stars (2*i-1 stars for each row)
        stars = 2 * i - 1
        print("*" * stars)

# Print an inverted star pyramid of height n
height = int(input("Enter the height of the inverted star pyramid: "))
print(f"Inverted star pyramid of height {height}:\n")
print_inverted_star_pyramid(height)

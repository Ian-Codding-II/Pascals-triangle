# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to calculate the binomial coefficient (Pascal's Triangle formula)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Function to generate Pascal's Triangle
def pascals_triangle(rows):
    for n in range(rows):
        # Print leading spaces for formatting
        print(" " * (rows - n - 1), end="")
        
        for k in range(n + 1):
            # Print each binomial coefficient in the row
            print(binomial_coefficient(n, k), end=" ")
        
        # Move to the next line after each row
        print()

# Input: number of rows to generate
rows = int(input("Enter the number of rows for Pascal's Triangle: "))
pascals_triangle(rows)
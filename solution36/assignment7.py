def print_triangle_for_formatting(n):
    for i in range(1, n + 1):
        # Print leading spaces to align the triangle
        print(" " * (n - i), end="")
        # Print numbers for each row
        for j in range(1, 2 * i):
            print(j, end=" ")
        print()  # Move to the next line

# Example usage:
print_triangle_for_formatting(3)

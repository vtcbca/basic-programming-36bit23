def print_alphabet_pattern_for(n):
    for i in range(n):
        # Print leading spaces to align the pattern
        print(" " * (n - i - 1), end="")
        
        # Print increasing part (letters from A to the i-th letter)
        for j in range(i + 1):
            print(chr(65 + j), end=" ")

        # Print decreasing part (letters from the (i-1)-th letter down to A)
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end=" ")

        # Move to the next line
        print()

# Example usage:
n = 3
print_alphabet_pattern_for(n)

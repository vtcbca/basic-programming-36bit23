//Calculate the factorial of a given number

def factorial_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
print(factorial_for_loop(5)) 
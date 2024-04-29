"""
This module provides a function to generate the Fibonacci sequence up to the nth term.
"""

def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.

    Args:
        n (int): The number of terms to generate in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to the nth term.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
    return sequence

# Generate the first 10 terms of the Fibonacci sequence
fib_sequence = fibonacci(10)
print(fib_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

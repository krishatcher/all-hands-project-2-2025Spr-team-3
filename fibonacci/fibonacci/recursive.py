"""Recursive approach to calculate a Fibonacci sequence"""


def fibonacci_recursive(n: int) -> int:
    """Generates the Fibonacci sequence up to the nth term using recursion without memoization."""

    # Handle negative inputs
    if n < 0:
        raise ValueError("Input must be a positive integer.")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # do the recursive calculation for the nth number
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

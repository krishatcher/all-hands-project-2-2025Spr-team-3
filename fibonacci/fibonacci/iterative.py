def fibonacci_iterative(n: int) -> int:
    """Generates the Fibonacci sequence up to the nth term using an iterative approach."""

    # Handle negative inputs
    if n < 0:
        raise ValueError("Input must be a positive integer.")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Iterate from 2 to n
    for _ in range(2, n + 1):
        # Update the Fibonacci numbers
        a, b = b, a + b

    # Return the nth Fibonacci number
    return b

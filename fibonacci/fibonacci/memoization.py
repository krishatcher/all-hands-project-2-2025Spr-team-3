"""Calculate the Fibonacci sequence up to a given number, using memoization techniques."""

from typing import Dict


def fibonacci_memoization(n: int)-> int:
    """
    Wrapper function which allows this approach to follow the pattern used by the other approaches
    """
    memo: Dict[int, int] = {}
    return fibonacci_generator(n, memo)


def fibonacci_generator(n: int, memo: Dict[int, int])-> int:
    """Generates the Fibonacci sequence up to the nth term using memoization."""
    # handle negative inputs
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    # intialize a dictionary to store previously computed numbers.
    if memo is None:
        memo = {}

    # if the number has already been calculated, use it
    if n in memo:
        return memo[n]
    # create the base case for handling 1 & 2 fibonacci numbers
    base_case = 2
    if n < base_case:
        return n

    #calculate the fibonacci for nth number
    memo[n] = fibonacci_generator(n - 1, memo) + fibonacci_generator(n - 2, memo)
    # return the appropriate fibonacci number
    return memo[n]

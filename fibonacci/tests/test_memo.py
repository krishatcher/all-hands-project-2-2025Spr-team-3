"""Test suite for the mem_fibonacci function."""

from fibonacci import memoization

# Test case to verify base cases of the Fibonacci sequence
def test_fibonacci_base_cases():
    """Confirm that base cases return the expected Fibonacci values."""
    assert memoization.mem_fibonacci(0, {}) == 1
    assert memoization.mem_fibonacci(1, {}) == 1
    assert memoization.mem_fibonacci(2, {}) == 1

# Test case to check Fibonacci calculations for small values
def test_fibonacci_small_numbers():
    """Confirm that Fibonacci values for small numbers are computed correctly."""
    assert memoization.mem_fibonacci(3, {}) == 2
    assert memoization.mem_fibonacci(4, {}) == 3
    assert memoization.mem_fibonacci(5, {}) == 5
    assert memoization.mem_fibonacci(6, {}) == 8

# Test case to verify Fibonacci calculations for larger values
def test_fibonacci_large_numbers():
    """Confirm that Fibonacci values for larger numbers are computed correctly."""
    memo = {}
    assert memoization.mem_fibonacci(10, memo) == 55
    assert memoization.mem_fibonacci(15, memo) == 610
    assert memoization.mem_fibonacci(20, memo) == 6765

# Test case to verify that negative inputs raise a ValueError
def test_fibonacci_negative_input():
    """Ensure negative inputs raise a ValueError."""
    try:
        memoization.mem_fibonacci(-5, {})
        assert False, "Expected ValueError but no exception was raised."
    except ValueError as e:
        assert str(e) == "Input must be a positive integer."

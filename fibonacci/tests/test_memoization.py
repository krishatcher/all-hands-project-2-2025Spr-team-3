"""Test suite for the mem_fibonacci function."""

from fibonacci.memoization import fibonacci_memoization


# Test case to verify base cases of the Fibonacci sequence
def test_fibonacci_base_cases():
    """Confirm that base cases return the expected Fibonacci values."""
    assert fibonacci_memoization(0, {}) == 0
    assert fibonacci_memoization(1, {}) == 1
    assert fibonacci_memoization(2, {}) == 1

# Test case to check Fibonacci calculations for small values
def test_fibonacci_small_numbers():
    """Confirm that Fibonacci values for small numbers are computed correctly."""
    assert fibonacci_memoization(3, {}) == 2
    assert fibonacci_memoization(4, {}) == 3
    assert fibonacci_memoization(5, {}) == 5
    assert fibonacci_memoization(6, {}) == 8

# Test case to verify Fibonacci calculations for larger values
def test_fibonacci_large_numbers():
    """Confirm that Fibonacci values for larger numbers are computed correctly."""
    memo = {}
    assert fibonacci_memoization(10, memo) == 55
    assert fibonacci_memoization(15, memo) == 610
    assert fibonacci_memoization(20, memo) == 6765

# Test case to verify that negative inputs raise a ValueError
def test_fibonacci_negative_input():
    """Ensure negative inputs raise a ValueError."""
    try:
        fibonacci_memoization(-5, {})
        assert False, "Expected ValueError but no exception was raised."
    except ValueError as e:
        assert str(e) == "Input must be a positive integer."

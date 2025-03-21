"""Test suite for the fibonacci_iterative function."""

import pytest
from fibonacci.iterative import fibonacci_iterative


def test_fibonacci_base_cases():
    """Confirm that base cases return the expected Fibonacci values."""
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(2) == 1


def test_fibonacci_small_numbers():
    """Confirm that Fibonacci values for small numbers are computed correctly."""
    assert fibonacci_iterative(3) == 2
    assert fibonacci_iterative(4) == 3
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(6) == 8


def test_fibonacci_large_numbers():
    """Confirm that Fibonacci values for larger numbers are computed correctly."""
    assert fibonacci_iterative(10) == 55
    assert fibonacci_iterative(15) == 610
    assert fibonacci_iterative(20) == 6765
    assert fibonacci_iterative(30) == 832040
    assert fibonacci_iterative(34) == 5702887


def test_fibonacci_negative_input():
    """Ensure negative inputs raise a ValueError."""
    with pytest.raises(ValueError) as exc_info:
        fibonacci_iterative(-5)
    assert str(exc_info.value) == "Input must be a positive integer."


def test_fibonacci_invalid_input_types():
    """Test the type handling of the iterative implementation of the Fibonacci sequence."""
    with pytest.raises(TypeError):
        fibonacci_iterative(3.5)  # Float input
    with pytest.raises(TypeError):
        fibonacci_iterative("string")  # String input
    with pytest.raises(TypeError):
        fibonacci_iterative(None)  # None input
    with pytest.raises(TypeError):
        fibonacci_iterative([])  # List input
    with pytest.raises(TypeError):
        fibonacci_iterative({})  # Dictionary input

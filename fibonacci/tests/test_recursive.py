
import pytest

from fibonacci.recursive import fibonacci_recursive


def test_negativeinputrecursive():
    """Test the recursive implementation of the Fibonacci sequence."""

    # Test the negative input handling
    try:
        fibonacci_recursive(-5)
        assert False, "Expected ValueError but no exception was raised."
    except ValueError as e:
        assert str(e) == "Input must be a positive integer."


def test_basescases():
    """Test the base cases of the Fibonacci sequence"""

    # Test the base cases
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1


def test_recursivesequences():
    """Test the recursive implementation of the Fibonacci sequence."""

    # Test the recursive calculation
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(10) == 55
    assert fibonacci_recursive(15) == 610
    assert fibonacci_recursive(20) == 6765
    assert fibonacci_recursive(30) == 832040
    assert fibonacci_recursive(34) == 5702887


def test_type_handling():
    """Test the type handling of the recursive implementation of the Fibonacci sequence."""

    # Test the type of inputs and handling it

    with pytest.raises(ValueError):
        fibonacci_recursive(3.5)
    with pytest.raises(TypeError):
        fibonacci_recursive("string")
    with pytest.raises(TypeError):
        fibonacci_recursive(None)
    with pytest.raises(TypeError):
        fibonacci_recursive([])
    with pytest.raises(TypeError):
        fibonacci_recursive({})

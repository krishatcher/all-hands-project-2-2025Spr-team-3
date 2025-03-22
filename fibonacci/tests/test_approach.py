"""Tests for the approach module."""

from fibonacci.approach import GenerationApproach


ITERATIVE_VAL = "iterative"
ITERATIVE_NAME = "ITERATIVE"
MEMOIZATION_VAL = "memoization"
MEMOIZATION_NAME = "MEMOIZATION"
RECURSIVE_VAL = "recursive"
RECURSIVE_NAME = "RECURSIVE"


def test_fibonacci_generation_approach_iterative_name():
    """Confirm that the enum name for `Iterative` is correct."""
    assert GenerationApproach.ITERATIVE.name == ITERATIVE_NAME


def test_fibonacci_generation_approach_iterative_val():
    """Confirm that the enum value for `Iterative` is correct."""
    assert GenerationApproach.ITERATIVE.value == ITERATIVE_VAL


def test_fibonacci_generation_approach_iterative_string():
    """Confirm that the `str` method returns expected for `Iterative`."""
    assert str(GenerationApproach.ITERATIVE) == ITERATIVE_VAL


def test_fibonacci_generation_approach_memoization_name():
    """Confirm that the enum name for `Memoization` is correct."""
    assert GenerationApproach.MEMOIZATION.name == MEMOIZATION_NAME


def test_fibonacci_generation_approach_memoization_val():
    """Confirm that the enum value for `Memoization` is correct."""
    assert GenerationApproach.MEMOIZATION.value == MEMOIZATION_VAL


def test_fibonacci_generation_approach_memoization_string():
    """Confirm that the `str` method returns expected for `Memoization`."""
    assert str(GenerationApproach.MEMOIZATION) == MEMOIZATION_VAL


def test_fibonacci_generation_approach_recursive_name():
    """Confirm that the enum name for `Recursive` is correct."""
    assert GenerationApproach.RECURSIVE.name == RECURSIVE_NAME


def test_fibonacci_generation_approach_recursive_val():
    """Confirm that the enum value for `Recursive` is correct."""
    assert GenerationApproach.RECURSIVE.value == RECURSIVE_VAL


def test_fibonacci_generation_approach_recursive_string():
    """Confirm that the `str` method returns expected for `Recursive`."""
    assert str(GenerationApproach.RECURSIVE) == RECURSIVE_VAL

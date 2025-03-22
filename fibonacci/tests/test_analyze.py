"""Test cases for the analyze module."""

import pytest

from fibonacci.analyze import calculate_average_values

THREE = 3


@pytest.fixture
def input_list_of_floats():
    """Create a test fixture for a list of lists."""
    return [60.6, 803.6, 5.93]


def test_calculate_average_values(input_list_of_floats):
    """Confirm that the return type is correct."""
    result = calculate_average_values(
        input_list_of_floats, len(input_list_of_floats)
    )
    avg_list = []

    for item in input_list_of_floats:
        item_avg = item / len(input_list_of_floats)
        avg_list.append(round(item_avg, 6))

    assert len(result) == THREE
    assert result[0] == avg_list[0]
    assert result[1] == avg_list[1]
    assert result[2] == avg_list[2]

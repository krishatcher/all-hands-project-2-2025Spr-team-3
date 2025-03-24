"""Configuration of the benchmarking tool with an approach."""

from enum import Enum


class GenerationApproach(str, Enum):
    """Enum defining available fibonacci generation approach names"""

    ITERATIVE = "iterative"
    MEMOIZATION = "memoization"
    RECURSIVE = "recursive"

    def __str__(self):
        """Overloaded dunder string method to return the value"""
        return self.value

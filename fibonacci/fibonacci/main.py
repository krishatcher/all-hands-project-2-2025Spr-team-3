"""Implementation of the Benchmarking toolset"""

import timeit
from typing import List

import typer
from rich.console import Console

from fibonacci.approach import GenerationApproach
from fibonacci.analyze import calculate_average_values

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()


@cli.command()
def main(
    quantity: int = typer.Option(100),
    approach: GenerationApproach = GenerationApproach.ITERATIVE,
    runs: int = typer.Option(15),
    repeats: int = typer.Option(5),
):
    """
    Compute the Fibonacci sequence using the specified approach.
    """
    execution_times: List[float] = []

    console.print(
        "==========================================================================="
    )
    console.print(
        "                           Fibonacci Calculation                           "
    )
    console.print(
        "==========================================================================="
    )
    console.print(
        f" Calculating the first {quantity} entries in the Fibonacci sequence."
    )
    console.print(
        f" Performing {repeats} sets of {runs} runs of the '{approach}' calculation approach."
    )
    console.print(
        "---------------------------------------------------------------------------"
    )

    if approach == GenerationApproach.ITERATIVE:
        execution_times = timeit.Timer(
            f"fibonacci_iterative({quantity})",
            setup="from fibonacci.iterative import fibonacci_iterative",
        ).repeat(repeat=repeats, number=runs)
    elif approach == GenerationApproach.RECURSIVE:
        execution_times = timeit.Timer(
            f"fibonacci_recursive({quantity})",
            setup="from fibonacci.recursive import fibonacci_recursive",
        ).repeat(repeat=repeats, number=runs)
    elif approach == GenerationApproach.MEMOIZATION:
        execution_times = timeit.Timer(
            f"fibonacci_memoization({quantity})",
            setup="from fibonacci.memoization import fibonacci_memoization",
        ).repeat(repeat=repeats, number=runs)

    avg_execution_times = calculate_average_values(execution_times, repeats)
    console.print(" Total time (sec) for each set of runs:")
    console.print(execution_times)
    console.print("")
    console.print(" Average times (sec) for each set of runs:")
    console.print(avg_execution_times)
    console.print(
        "==========================================================================="
    )


# Sources:
# geeksforgeeks.org for general information on fibonaccis
# github copoilot for debugging and comment generation

# logic influenced by AEP #2: https://github.com/Allegheny-Computer-Science-202-S2025/computer-science-202-algorithm-engineering-project-2-krishatcher
# help to call timeit successfully: https://stackoverflow.com/questions/2819625/how-to-use-a-callable-as-the-setup-with-timeit-timer

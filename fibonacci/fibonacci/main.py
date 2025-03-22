import typer
from iterative import fibonacci_iterative
from memoized import fibonacci_memoized
from recursive import fibonacci_recursive

# Create a Typer app
app = typer.Typer()

@app.command()
def main(
    n: int = typer.Argument(..., help="The Fibonacci number to compute."),
    # Add an option to specify the approach
    approach: str = typer.Option(
        # Default to the recursive approach
        "iterative",
        # Specify the help message for the option
        help="Choose between 'recursive', 'iterative', or 'memoized'."
    )
):
    """
    Compute the nth Fibonacci number using the specified approach.
    """
    # Select the approach
    if approach == "recursive":
        # Compute the Fibonacci number using the recursive approach
        result = fibonacci_recursive(n)
    elif approach == "iterative":
        # Compute the Fibonacci number using the iterative approach
        result = fibonacci_iterative(n)
    elif approach == "memoized":
        # Compute the Fibonacci number using the memoized approach
        result = fibonacci_memoized(n)
    else:
        typer.echo("Invalid method. Choose between 'recursive', 'iterative', or 'memoized'.")
        # Exit with an error code
        raise typer.Exit(code=1)

    # Display the result
    typer.echo(f"The {n}th Fibonacci number using the {approach} approach is: {result}")

if __name__ == "__main__":
    app()

# Sources:
# geeksforgeeks.org for general information on fibonaccis
# github copoilot for debugging and comment generation

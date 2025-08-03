"""
Robust division calculator module with error handling.
"""


def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with comprehensive error handling.

    Args:
        numerator: The number to be divided
        denominator: The number to divide by

    Returns:
        str: Result message or error message
    """
    try:
        # Convert inputs to float to handle non-numeric inputs
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

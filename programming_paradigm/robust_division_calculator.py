# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting both inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Try performing the division
        result = num / denom
        return f"Result: {result}"

    except ValueError:
        return "Error: Invalid number input."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting both inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Try performing the division
        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
def safe_divide(numerator, denominator):
    """Performs division with error handling."""
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Handle other unexpected errors
        return f"An unexpected error occurred: {e}"

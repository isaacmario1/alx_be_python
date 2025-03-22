# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

#convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

#convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Function for user interaction and temperature conversion
def temperature_conversion():
    temp_input = input("Enter the temperature to convert: ")
    
    # Check if the input is a valid number
    if temp_input.replace('.', '', 1).isdigit() or (temp_input[1:].replace('.', '', 1).isdigit() and temp_input[0] == '-'):
        temp = float(temp_input)
    else:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Ask whether the temperature is in Celsius or Fahrenheit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # Validate the unit input
    if unit == "C":
        # Convert to Fahrenheit
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == "F":
        # Convert to Celsius
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the temperature conversion tool
if __name__ == "__main__":
    temperature_conversion()

import sys

# Constants for temperature conversions
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67
CELSIUS_TO_KELVIN = 273.15

def parse_temperature(input_str):
    """Parse a temperature string into a numeric value and unit."""
    input_str = input_str.strip().upper()
    if not input_str:
        raise ValueError("Input cannot be empty")

    # Split the numeric part and the unit
    for i, char in enumerate(input_str):
        if not char.isdigit() and char != '.':
            number = input_str[:i]
            unit = input_str[i:]
            break
    else:
        raise ValueError("Invalid input format. Please provide a number followed by C, F, or K")

    try:
        value = float(number)
    except ValueError:
        raise ValueError("Invalid numeric value")

    if unit not in ['C', 'F', 'K']:
        raise ValueError("Invalid unit. Use C for Celsius, F for Fahrenheit, or K for Kelvin")

    return value, unit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + CELSIUS_TO_KELVIN

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_celsius(kelvin):
    return kelvin - CELSIUS_TO_KELVIN

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature from one unit to another."""
    if from_unit == to_unit:
        return value

    conversions = {
        'C': {'F': celsius_to_fahrenheit, 'K': celsius_to_kelvin},
        'F': {'C': fahrenheit_to_celsius, 'K': fahrenheit_to_kelvin},
        'K': {'C': kelvin_to_celsius, 'F': kelvin_to_fahrenheit}
    }

    return conversions[from_unit][to_unit](value)

def get_user_input(prompt):
    """Get user input with a prompt."""
    return input(prompt).strip().upper()

def main():
    while True:
        try:
            temp_input = get_user_input("Enter temperature (e.g., 45C): ")
            value, unit = parse_temperature(temp_input)

            # Validate temperature is above absolute zero
            if (unit == 'C' and value < ABSOLUTE_ZERO_C) or \
               (unit == 'F' and value < ABSOLUTE_ZERO_F) or \
               (unit == 'K' and value < 0):
                raise ValueError("Temperature is below absolute zero")

            target_units = [u for u in ['C', 'F', 'K'] if u != unit]
            target = get_user_input(f"Convert to ({'/'.join(target_units)}): ")

            if target not in target_units:
                raise ValueError(f"Invalid target unit. Choose from {', '.join(target_units)}")

            result = convert_temperature(value, unit, target)
            print(f"The conversion result is: {result:.2f}{target}")

        except ValueError as e:
            print(f"Error: {str(e)}")

        if get_user_input("Do you want to continue? (y/n): ") != 'Y':
            break

    print("Thank you for using the temperature converter!")

if __name__ == "__main__":
    main()
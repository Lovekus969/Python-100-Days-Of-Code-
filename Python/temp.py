# Temperature Conversion: Fahrenheit to Celsius

def fahrenheit_to_celsius(f):
    # Formula: (F - 32) * 5/9
    return (f - 32) * 5/9

def main():
    print("Fahrenheit to Celsius Converter")

    # Take input from user
    f = float(input("Enter temperature in Fahrenheit: "))

    # Call conversion function
    c = fahrenheit_to_celsius(f)

    # Show result
    print(f"{f}°F is equal to {c:.2f}°C")

# Run the program
if __name__ == "__main__":
    main()

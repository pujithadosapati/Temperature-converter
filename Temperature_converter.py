# Temperature Converter
# 1. Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# 2. Display Menu

print("\n===== TEMPERATURE CONVERTER =====")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

# 3. Get User Input

choice = input("\nEnter your choice (1-6): ")
try:
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Please select 1-6.")

    else:
        temperature = float(input("Enter temperature: "))

        # 4. Validate Temperature

        if choice in ["1", "3"] and temperature < -273.15:
            print("Invalid Celsius temperature!")

        elif choice in ["2", "5"] and temperature < -459.67:
            print("Invalid Fahrenheit temperature!")

        elif choice in ["4", "6"] and temperature < 0:
            print("Invalid Kelvin temperature!")

        else:
            # 5. Perform Conversion

            if choice == "1":
                result = celsius_to_fahrenheit(temperature)
                unit = "Fahrenheit"

            elif choice == "2":
                result = fahrenheit_to_celsius(temperature)
                unit = "Celsius"

            elif choice == "3":
                result = celsius_to_kelvin(temperature)
                unit = "Kelvin"

            elif choice == "4":
                result = kelvin_to_celsius(temperature)
                unit = "Celsius"

            elif choice == "5":
                result = fahrenheit_to_kelvin(temperature)
                unit = "Kelvin"

            else:
                result = kelvin_to_fahrenheit(temperature)
                unit = "Fahrenheit"

            # 6. Display Result

            print("\n===== CONVERSION RESULT =====")
            print(f"Converted Temperature: {result:.2f} {unit}")

except ValueError:
    print("Invalid input! Please enter a numeric temperature.")

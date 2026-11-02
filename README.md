## Temperature Converter
 ## Project Description
The Temperature Converter is a Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin.
It allows users to select a conversion option, enter a temperature, and get the converted result.
## Objective
Practice Python functions.
Understand arithmetic operations.
Learn conditional statements (if-elif-else).
Handle user input and input validation.
Format decimal outputs neatly.
## Technologies Used
Programming Language: Python
Editor: VS Code / PyCharm
Concepts: Functions, Variables, Conditions, Input Validation, and Arithmetic Operations.
## Features
Convert Celsius to Fahrenheit.
Convert Fahrenheit to Celsius.
Convert Celsius to Kelvin.
Convert Kelvin to Celsius.
Convert Fahrenheit to Kelvin.
Convert Kelvin to Fahrenheit.
Validate physically meaningful temperature values.
Handle invalid numeric inputs.
Display results up to two decimal places.
## Conversion Formulas
Conversion	Formula
Celsius to Fahrenheit	(C × 9/5) + 32
Fahrenheit to Celsius	(F − 32) × 5/9
Celsius to Kelvin	C + 273.15
Kelvin to Celsius	K − 273.15
Fahrenheit to Kelvin	(F − 32) × 5/9 + 273.15
Kelvin to Fahrenheit	(K − 273.15) × 9/5 + 32
## How to Run the Project
Step 1: Install Python on your computer.
Step 2: Download or clone this project.
Step 3: Open the project folder in VS Code.
Step 4: Open the terminal.
Step 5: Run the following command:
bash
python temperature_converter.py
Step 6: Select a conversion option from 1 to 6.
Step 7: Enter the temperature.
Step 8: View the converted result.
## Sample Output
text
===== TEMPERATURE CONVERTER =====
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
Enter your choice (1-6): 1
Enter temperature: 100
===== CONVERSION RESULT =====
Converted Temperature: 212.00 Fahrenheit
## Input Validation
Celsius temperature must not be below -273.15°C.
Fahrenheit temperature must not be below -459.67°F.
Kelvin temperature must not be below 0 K.
Invalid menu choices are rejected.
Non-numeric temperature inputs are handled.
## Learning Outcomes
After completing this project, I learned:
How to define and call Python functions.
How to use return statements.
How to perform mathematical calculations.
How to use conditional statements.
How to validate user inputs.
How to display formatted output.

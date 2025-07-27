FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    result = fahrenheit* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(result)

def convert_to_fahrenheit(celsius):
    result = celsius* CELSIUS_TO_FAHRENHEIT_FACTOR
    print(result)

user_input = float(input("Enter the temperature to convert: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
#Enter the temperature to convert: 100
#Is this temperature in Celsius or Fahrenheit? (C/F): F
#100.0°F is 37.77777777777778°C

if celsius_or_fahrenheit == "f":
    temp = user_input* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{user_input}°F is {temp}°C")
else:
    temp = user_input* CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{user_input}°C is {temp}°F")

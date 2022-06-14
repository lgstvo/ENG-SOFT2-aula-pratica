def convert_fahrenheit_to_celsius(temperature_in_fahrenheit : float):
    temperature_in_celsius = (temperature_in_fahrenheit - 32) * (5/9)
    return temperature_in_celsius

def convert_celsius_to_fahrenheit(temperature_in_celsius : float):
    temperature_in_fahrenheit = (temperature_in_celsius * (9/5)) + 32
    return temperature_in_fahrenheit

def convert_celsius_to_kelvin(temperature_in_celsius : float):
    temperature_in_kelvin = temperature_in_celsius + 273.15
    return temperature_in_kelvin

def convert_kelvin_to_celsius(temperature_in_kelvin : float):
    temperature_in_celsius = temperature_in_kelvin - 273.15
    return temperature_in_celsius

def convert_fahrenheit_to_kelvin(temperature_in_fahrenheit : float):
    temperature_in_celsius = convert_fahrenheit_to_celsius(temperature_in_fahrenheit)
    temperature_in_kelvin = convert_celsius_to_kelvin(temperature_in_celsius)
    return temperature_in_kelvin

def convert_kelvin_to_fahrenheit(temperature_in_kelvin : float):
    temperature_in_celsius = convert_kelvin_to_celsius(temperature_in_kelvin)
    temperature_in_fahrenheit = convert_celsius_to_fahrenheit(temperature_in_celsius)
    return temperature_in_fahrenheit
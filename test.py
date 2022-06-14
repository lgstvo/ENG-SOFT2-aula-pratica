from main import *


def test_convert_fahrenheit_to_celsius():
    temperature_f = 32
    desired_temperature_c = 0

    assert desired_temperature_c == convert_fahrenheit_to_celsius(temperature_f), "Should be 0"

def test_convert_celsius_to_fahrenheit():
    temperature_c = 0
    desired_temperature_f = 32

    assert desired_temperature_f == convert_celsius_to_fahrenheit(temperature_c), "Should be 32"

def test_convert_celsius_to_kelvin():
    temperature_c = 10
    desired_temperature_k = 283.15

    assert desired_temperature_k == convert_celsius_to_kelvin(temperature_c), "Should be 283.15"

def test_convert_kelvin_to_celsius():
    temperature_k = 283.15
    desired_temperature_c = 10

    assert desired_temperature_c == convert_kelvin_to_celsius(temperature_k), "Should be 10"

def test_convert_fahrenheit_to_kelvin():
    temperature_f = 32
    desired_temperature_k = 273.15

    assert desired_temperature_k == convert_fahrenheit_to_kelvin(temperature_f), "Should be 273.15"

def test_convert_kelvin_to_fahrenheit():
    temperature_k = 273.15
    desired_temperature_f = 32

    assert desired_temperature_f == convert_kelvin_to_fahrenheit(temperature_k), "Should be 32"

if __name__ == "__main__":
    test_convert_celsius_to_fahrenheit()
    test_convert_fahrenheit_to_celsius()
    test_convert_celsius_to_kelvin()
    test_convert_kelvin_to_celsius()
    test_convert_fahrenheit_to_kelvin()
    test_convert_kelvin_to_fahrenheit()
    print("ALL OK.")
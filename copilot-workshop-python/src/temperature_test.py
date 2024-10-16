import unittest
from unittest.mock import patch

from temperature import TemperatureConversion, TemperatureUnit

class TestTemperatureConversion(unittest.TestCase):

    def test_convert_temperature(self):
        # Celsius to Fahrenheit
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(0, TemperatureUnit.Celsius, TemperatureUnit.Fahrenheit), 32)
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(100, TemperatureUnit.Celsius, TemperatureUnit.Fahrenheit), 212)
        
        # Fahrenheit to Celsius
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(32, TemperatureUnit.Fahrenheit, TemperatureUnit.Celsius), 0)
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(212, TemperatureUnit.Fahrenheit, TemperatureUnit.Celsius), 100)
        
        # Celsius to Kelvin
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(0, TemperatureUnit.Celsius, TemperatureUnit.Kelvin), 273.15)
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(100, TemperatureUnit.Celsius, TemperatureUnit.Kelvin), 373.15)
        
        # Kelvin to Celsius
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(273.15, TemperatureUnit.Kelvin, TemperatureUnit.Celsius), 0)
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(373.15, TemperatureUnit.Kelvin, TemperatureUnit.Celsius), 100)
        
        # Fahrenheit to Kelvin
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(32, TemperatureUnit.Fahrenheit, TemperatureUnit.Kelvin), 273.15)
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(212, TemperatureUnit.Fahrenheit, TemperatureUnit.Kelvin), 373.15)
        
        # Kelvin to Fahrenheit
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(273.15, TemperatureUnit.Kelvin, TemperatureUnit.Fahrenheit), 32)
        self.assertAlmostEqual(TemperatureConversion.convert_temperature(373.15, TemperatureUnit.Kelvin, TemperatureUnit.Fahrenheit), 212)

    def test_get_temperature_unit_sign(self):
        self.assertEqual(TemperatureConversion.get_temperature_unit_sign(TemperatureUnit.Celsius), "°C")
        self.assertEqual(TemperatureConversion.get_temperature_unit_sign(TemperatureUnit.Fahrenheit), "°F")
        self.assertEqual(TemperatureConversion.get_temperature_unit_sign(TemperatureUnit.Kelvin), "K")

    @patch('builtins.input', side_effect=[25.0])
    def test_get_source_value(self, mock_input):
        self.assertEqual(TemperatureConversion.get_source_value(), 25.0)

    @patch('builtins.input', side_effect=[1])
    def test_get_temperature_unit_celsius(self, mock_input):
        self.assertEqual(TemperatureConversion.get_temperature_unit("source"), TemperatureUnit.Celsius)

    @patch('builtins.input', side_effect=[2])
    def test_get_temperature_unit_fahrenheit(self, mock_input):
        self.assertEqual(TemperatureConversion.get_temperature_unit("source"), TemperatureUnit.Fahrenheit)

    @patch('builtins.input', side_effect=[3])
    def test_get_temperature_unit_kelvin(self, mock_input):
        self.assertEqual(TemperatureConversion.get_temperature_unit("source"), TemperatureUnit.Kelvin)

if __name__ == '__main__':
    unittest.main()
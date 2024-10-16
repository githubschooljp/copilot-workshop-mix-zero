import enum

class TemperatureUnit(enum.Enum):
    Celsius = 1
    Fahrenheit = 2
    Kelvin = 3

class TemperatureConversion:
    @staticmethod
    def startFlow():
        source_value = TemperatureConversion.get_source_value()
        from_unit = TemperatureConversion.get_temperature_unit("source")
        to_unit = TemperatureConversion.get_temperature_unit("target")

        target_value = TemperatureConversion.convert_temperature(source_value, from_unit, to_unit)

        print(f"{source_value:.2f}{TemperatureConversion.get_temperature_unit_sign(from_unit)} is {target_value:.2f}{TemperatureConversion.get_temperature_unit_sign(to_unit)}")
        
    @staticmethod
    def get_temperature_unit_sign(unit):
        unit_signs = {
            TemperatureUnit.Celsius: "°C",
            TemperatureUnit.Fahrenheit: "°F",
            TemperatureUnit.Kelvin: "K"
        }
        return unit_signs[unit]

    @staticmethod
    def get_source_value():
        value = float(input("Enter the value to be converted: "))
        return value

    @staticmethod
    def get_temperature_unit(source_or_target):
        print(f"Select {source_or_target} temperature unit:")
        print("[1] Celsius")
        print("[2] Fahrenheit")
        print("[3] Kelvin")
        choice = int(input("Enter choice: "))

        if choice == 1:
            return TemperatureUnit.Celsius
        elif choice == 2:
            return TemperatureUnit.Fahrenheit
        elif choice == 3:
            return TemperatureUnit.Kelvin
        else:
            return TemperatureUnit.Celsius

    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        # Convert everything to Celsius first
        if from_unit == TemperatureUnit.Fahrenheit:
            value = (value - 32) * 5 / 9
        elif from_unit == TemperatureUnit.Kelvin:
            value -= 273.15

        # Then convert to the target unit
        if to_unit == TemperatureUnit.Fahrenheit:
            value = value * 9 / 5 + 32
        elif to_unit == TemperatureUnit.Kelvin:
            value += 273.15

        return value
import sys
from temperature import TemperatureConversion

class ConversionType:
    Temperature = 1
    Distance = 2

def get_conversion_type():
    conversion_types = [ConversionType.Temperature, ConversionType.Distance]

    while True:
        print("Select type of conversion:")
        print("[1] Temperature")
        choice = int(input("Enter choice: "))

        if 0 < choice <= len(conversion_types):
            return conversion_types[choice - 1]

        print("Invalid choice. Please try again.")

def main():
    conversion_type = get_conversion_type()
    if conversion_type == ConversionType.Temperature:
        TemperatureConversion.startFlow()

if __name__ == "__main__":
    main()
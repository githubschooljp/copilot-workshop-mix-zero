import enum

class DistanceUnit(enum.Enum):
    Meters = 1
    Feet = 2
    Yards = 3

class DistanceConversion:
    @staticmethod
    def get_distance_unit_sign(unit):
        unit_signs = {
            DistanceUnit.Meters: "m",
            DistanceUnit.Feet: "ft",
            DistanceUnit.Yards: "yd"
        }
        return unit_signs[unit]

    @staticmethod
    def get_source_value():
        value = float(input("Enter the value to be converted: "))
        return value

    @staticmethod
    def get_distance_unit(source_or_target):
        print(f"Select {source_or_target} distance unit:")
        print("[1] Meters")
        print("[2] Feet")
        print("[3] Yards")
        choice = int(input("Enter choice: "))

        if choice == 1:
            return DistanceUnit.Meters
        elif choice == 2:
            return DistanceUnit.Feet
        elif choice == 3:
            return DistanceUnit.Yards
        else:
            return DistanceUnit.Meters  # Default to Meters

    @staticmethod
    def convert_distance(value, from_unit, to_unit):
        # Todo implement the actual conversion logic
        return 0

    @staticmethod
    def start_flow():
        source_value = DistanceConversion.get_source_value()
        from_unit = DistanceConversion.get_distance_unit("source")
        to_unit = DistanceConversion.get_distance_unit("target")

        target_value = DistanceConversion.convert_distance(source_value, from_unit, to_unit)

        print(f"{source_value:.2f}{DistanceConversion.get_distance_unit_sign(from_unit)} is {target_value:.2f}{DistanceConversion.get_distance_unit_sign(to_unit)}")

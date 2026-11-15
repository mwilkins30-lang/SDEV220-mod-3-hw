class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\nVehicle Information")
        print("-------------------")
        print(f"Type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Doors: {self.doors}")
        print(f"Roof: {self.roof}")

    def main():
        year = int(input("Enter vehicle year: "))
        try:
            year = int(input("Enter vehicle year: "))
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            return
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        doors = int(input("Enter number of doors (2 or 4): "))
        if doors not in [2, 4]:
            print("Invalid number of doors. Please enter 2 or 4.")
            return
        roof = input("Enter roof type (solid or sunroof): ")
        if roof.lower() not in ["solid", "sunroof"]:
                print("Invalid roof type. Please enter 'solid' or 'sunroof'.")
                return

        my_car = Automobile(year, make, model, doors, roof)
        my_car.display_info()

if __name__ == "__main__":
    Automobile.main()
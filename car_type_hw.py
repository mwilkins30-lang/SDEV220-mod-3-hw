class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def ___init___(self, year, make, model, doors, roof):
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
        year = input("Enter vehicle year: ")
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        doors = int(input("Enter number of doors (2 or 4): "))
        roof = input("Enter roof type (solid or sunroof): ")

        my_car = Automobile(year, make, model, doors, roof)
        my_car.display_info()

if __name__ == "__main__":
    Automobile.main()
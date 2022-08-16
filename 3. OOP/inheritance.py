class Vehicle:
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.name} drives past. Vrooom!")

    def turn(self, direction):
        print(f"The {self.color} {self.name} turns {direction}.")

    def brake(self):
        print(f"The {self.name} breaks down.")

    def manufacturer(self):
        print(f"The {self.name} is manufactured by {self.manufacturer}.")


class Car(Vehicle):
    def __init__(self, name, manufacturer, color, gear_name):
        super().__init__(name, manufacturer, color)
        self.gear_name = gear_name

    def change_gear(self):
        print(f"The {self.name} changes gear into {self.gear_name}.")


if __name__ == '__main__':
    car = Car("Ford", "USA", "red", "Manual")
    car.drive()
    car.change_gear()
    car.turn("right")
    car.brake()
    car.manufacturer()

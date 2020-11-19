class Car:
    """
    A simple attempt to represent a car.
    """
    
    def __init__(self, make, model, year):
        """  
        Initialize attributes to describe a car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """  
        Return a neatly formated name.
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """  
        Showing the car mileage.
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ 
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        """  
        Add the given amount to the odometer rading.
        """
        self.odometer_reading += miles

my_car = Car('audi', 'a4', '2019')
print(my_car.get_descriptive_name())

my_car.update_odometer(50)
my_car.read_odometer()

my_car.increment_odometer(350)
my_car.read_odometer()
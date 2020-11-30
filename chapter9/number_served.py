class Restaurant:
    """  
    A class representing restaurant.
    """

    def __init__(self, name, cuisine_type):
        """  
        Initialize the restaurant.
        """
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """  
        Display a summary of the restaurant.
        """
        summary = f"{self.name} serve wounderful {self.cuisine_type}"
        print()
        print(summary)

    def open_restaurant(self):
        """  
        Message to display that the restaurant is open.
        """
        msg = f"{self.name} is now open, Welcome!"
        print(msg)

    def set_number_served(self, number_served):
        """  
        Allow user to set the number of custom ers that have been served.
        """
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """  
        Alloww user to increment the number of customer served.
        """
        self.number_served += additional_served


restaurant = Restaurant('Blaq Hole','Chinese food')
restaurant.describe_restaurant()

print (f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 550
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(324)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(456)
print(f"Number served: {restaurant.number_served}")


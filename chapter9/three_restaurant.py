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

restaurant = Restaurant('Blaq Hole','Chinese food')
restaurant.describe_restaurant()

sea_salt = Restaurant("Sea Salt", 'seafood')
sea_salt.describe_restaurant()

manifest = Restaurant('manifest', 'thai food')
manifest.describe_restaurant()
class User():
    """  
    Repressent a simple user profile
    """

    def __init__(self, first_name, last_name, username, email, location):
        """ 
        Initialize the user
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempt = 0

    def describe_user(self):
        """  
        Display summary of the user's information.
        """
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """  
        Display a personalized greeting to the user.
        """
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempt(self):
        """  
        Increment the value of login attempts.
        """
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0

john = User('john', 'eric', 'john_eric', 'ericjohn.gmail.com', 'Dar es salaam')
john.describe_user()
john.greet_user()

print("\nMake three login attemps...")
john.increment_login_attempt
john.increment_login_attempt
john.increment_login_attempt
print(f"  Login attemps: {john.login_attempt}")

print("Reserting login attempts...")
john.reset_login_attempts()
print(f"  Login attempts: {john.login_attempt}")
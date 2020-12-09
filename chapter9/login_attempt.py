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

robert = User('robert', 'eric', 'robert_eric', 'ericrobert.gmail.com', 'Dar es salaam')
robert.describe_user()
robert.greet_user()

print("\nMake three login attemps...")
robert.increment_login_attempt
robert.increment_login_attempt
robert.increment_login_attempt
print(f"  Login attemps: {robert.login_attempt}")

print("Reserting login attempts...")
robert.reset_login_attempts()
print(f"  Login attempts: {robert.login_attempt}")hn.login_attempt}")hn.login_attempt}")
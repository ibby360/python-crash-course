class User:
    """  
    Representing simple user profile.
    """

    def __init__(self,first_name, last_name, username, email, location):
        """  
        Initialize the user.
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """  
        Displaying information about the user.
        """
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    """  
    Dispay a personalized greeting to the user.
    """

    def greeting(self):
        print(f"\nWelcome {self.username}")

john = User('john', 'matthes', 'j_matthes', 'j_matthes@example.com', 'elsinki')
john.describe_user()
john.greeting()

abdalah = User('abdalah', 'juma', 'abdalah_juma', 'abjumah@example.com', 'paris')
abdalah.describe_user()
abdalah.greeting()
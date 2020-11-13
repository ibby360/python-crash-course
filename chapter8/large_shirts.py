def make_shirt(size='large',message='I love python'):

    # summarize the shirt that is gonna be made
    print(f"\nI'm gonna make a {size} T-shirt.")
    print(f"Tha's gonna say {message}")

# calling the make_shirt function
make_shirt()
make_shirt(size='medium')
make_shirt(message='Python for life baby!', size='extra-large')
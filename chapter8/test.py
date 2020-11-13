def get_formated_name(first_name,last_name):
    """
    Return a full name, neatly foramted
    """
    full_name = f'{first_name} {last_name}'
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' to quit)")

    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formated_name = get_formated_name(f_name, l_name)
    print(f"Hello, {formated_name}!")
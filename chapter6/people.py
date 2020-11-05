# creating an empty list
people = []

# creating a dictionary to store person details
person = {
    'first_name': 'ibby',
    'last_name': 'blaq',
    'age': '20',
    'city': 'dsm'
}

person = {
    'first_name': 'icon',
    'last_name': 'man',
    'age': '22',
    'city': 'new city'
}

people.append(person)

person = {
    'first_name': 'jack',
    'last_name': 'cactus',
    'age': '20',
    'city': 'bay area'
}
# add the dictionary into the list of people


for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name} age of {age} lives in {city}.")
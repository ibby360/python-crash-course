favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'maulin': ['hawaii', 'iceland'],
    'john': ['mt. verstovia', 'the playground', 'new hampshire']
}

for person, places in favorite_places.items():
    print(f'\nMy friend {person.title()} like:')
    for place in places:
        print(f'\t- {place.title()}')

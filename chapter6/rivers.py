rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f'{river.title()} runs in {country.title()}.')

print('\nThe following rivers are included in data set.')
for river in rivers.keys():
    print(f"-> {river.title()}")

print('\n The folowing countries are included in data set.')
for country in rivers.values():
    print(f'-> {country.title()}')
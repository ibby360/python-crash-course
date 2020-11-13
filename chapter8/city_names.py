def city_country(city,country):
    """ Return the name of the city and its country """
    print(f'"{city.title()}, {country.title()}"')

city_country('santiago','chile')
city_country(city='london', country='england')
city_country('paris',country='france')
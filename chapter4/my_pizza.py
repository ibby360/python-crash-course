favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friends_pizza = favorite_pizzas[:]

favorite_pizzas.append('meat lovers')
friends_pizza.append('pesto')

print('My favourite pizza are:')
for pizza in favorite_pizzas:
    print(f'- {pizza}')

print('\nMy friend favourite pizza are:')
for pizza in friends_pizza:
    print(f'- {pizza}')
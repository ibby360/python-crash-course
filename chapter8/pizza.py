def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings')
    for topping in toppings:
         print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('matapu','ubwabwa','cheeze')
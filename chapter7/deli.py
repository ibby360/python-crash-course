sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwich = []

while sandwich_orders:
    current_sandwhich = sandwich_orders.pop()
    print(f"I'm making {current_sandwhich} sandwich.")
    finished_sandwich.append(current_sandwhich)
print('\n')

for sandwich in finished_sandwich:
    print(f"Done made {sandwich.title()}.")
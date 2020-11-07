sandwich_orders = ['pastrami','veggie', 'grilled cheese','pastrami', 'turkey', 'roast beef','pastrami',]
finished_sandwich = []

print("We are run out of pastrami today")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('\n')

while sandwich_orders:
    current_sandwhich = sandwich_orders.pop()
    print(f"I'm making {current_sandwhich} sandwich.")
    finished_sandwich.append(current_sandwhich)
print('\n')

for sandwich in finished_sandwich:
    print(f"Done made {sandwich.title()}.")
responses = {}

# st a flag to indicate that pulling is active.
polling_active = True

while polling_active:
    # prompt for the person's name and response
    name = input('What is your name? ')
    response = input('Where would you llike to go for vacation? ')
    # store the resonse into dictionary
    responses[name] = response

    # find out if anyone else want to take the poll
    repeat = input("Is there anyone else to take the poll (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
# showing the results.
print("\n***** Polling Results *****")
for name,response in responses.items():
    print(f"{name.title()} would like to take vacation to {response.title()}.")

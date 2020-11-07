prompt = "Want to play a game? "
# prompt += '\nEnter quit to end the program. '

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd like to go to {city.title()}")
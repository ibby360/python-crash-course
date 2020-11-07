prompt = "What Pizza would you like: "
prompt += "\nEnter quit when you done."

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"I'll add that {topping.title()} to your pizza.")
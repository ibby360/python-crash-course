def show_messages(messages):
    """ 
    print all messages
    """
    print("Printing all messages.")
    for message in messages:
        print(message)


def send_messages(message,sent_messages):
    """ 
    Print all message and the move them to sent messages
    """
    print("\nSending all messages.")

    while messages:
        current_messages = messages.pop()
        print(current_messages)

        sent_messages.append(current_messages)

messages = ['Hey, Where are you?','What are you eating for lunch?','There will be no class today.']
show_messages (messages)

sent_messages = []
send_messages(messages[:],sent_messages)

print('\nFinal list')
print(messages)
print(sent_messages)

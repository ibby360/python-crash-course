usernames = []

if usernames:
    for username in usernames:
        if (username == 'admin'):
            print('Hello admin, there is a report status.')
        else:
            print(f'Hello {username}, thanks for logging in again')
else:
    print("We need some users.")

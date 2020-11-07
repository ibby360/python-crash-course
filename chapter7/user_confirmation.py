# start with users that need to be verified.
# and an empty list to holed confirmed users.

unconfermes_users = ['alice','brian','cinde']
confirmed_users = []

# verify each user untill there is no more unconfermed users
# move each user into the list of confirmed users.
while unconfermes_users:
    current_user = unconfermes_users.pop()

    print(f"Verified user: {current_user.title()}")
    confirmed_users.append(current_user)

# display all confirmed users.
print("\nThe following users have been confirmed.")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
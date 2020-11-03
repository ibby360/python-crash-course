current_users = ['melisa', 'levina', 'maisalah', 'tiny', 'admin']
new_users = ['Melisa','Jovin','adam','Maisalah','shabanni']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'Sorry {new_user}, The name is already taken.')
    else:
        print(f'{new_user} still available')
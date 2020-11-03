users = ['melisa', 'levina', 'maisalah', 'tiny', 'admin']

for user in users:
    if 'admin' in user:
        print('Hello admin, would you like to see a status report.')
    else:
        print(f'Hello {user}, thanks for logging in again.')

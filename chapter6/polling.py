favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f'{name.title()}, likes {language.title()} language.')
print('\n')

staffs = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for staff in staffs:
    if staff in favorite_languages.keys():
        print(f'Thank you {staff.title()}, for the response.')
    elif staff not in favorite_languages.keys():
        print(f'Hi {staff.title()}, What is your favaourite language. Respond to the poll please.')
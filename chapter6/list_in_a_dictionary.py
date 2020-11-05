fav_language = {
    'jen': ['python', 'ruby'],
    'edward': ['go', 'ruby'],
    'sarah': ['python', 'c'],
    'phil': ['haskel', 'ruby'],
}

for name, languages in fav_language.items():
    print(f"\n{name.title()}'s favourite language are;")
    for language in languages:
        print(f"\t{language.title()}")

fav_number = {
    'anna': [22, 23],
    'anwar': [34,55],
    'juma': [20,100],
    'karim': [1908,2944],
    'rashford': [198,3456],
}

for name,numbers in fav_number.items():
    print(f"\n{name.title()} likes the follwing numbers.")
    for number in numbers:
        print(f"{number}")

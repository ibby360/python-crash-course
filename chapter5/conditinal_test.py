age = 18
personal_age = int(input("Please enter your age: "))

if (personal_age >= 18):
    print('You are old enought to vote!\n')

    qn = (input("Have you registered to vote? "))
    if qn == 'yes':
        print("You have all rights to vote!")
else:
    print("You can't vote if not registered.")
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Ibrahim', 'Ramadhan',
                             location='Tanzania',
                             age='20',
                             field='IT',
                             education='diploma',
                            gender='male',
                            )
                             
print(user_profile)

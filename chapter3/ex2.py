invited = ['mom','dad','kids']

# print a message for individual
print(f"Hey! {invited[0].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[1].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[2].title()}, I'm having a dinner at my place tonight. You're invited.")
print()

print(f'{invited[2].title()}, Wont make it tonight.')
print()

# replace kids with girlfriend from the list
invited[2] = 'girlfriend'
print(f"Hey! {invited[0].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[1].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[2].title()}, I'm having a dinner at my place tonight. You're invited.")
print()
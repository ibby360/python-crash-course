invited = ['mom','dad','kids']
invited.insert(0,'levina')
invited.insert(2,'aslam')
invited.append('maisalah')
invited[4] = 'girlfriend'


# print a message for individual
print(f"Hey! {invited[0].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[1].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[2].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[3].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[4].title()}, I'm having a dinner at my place tonight. You're invited.")
print(f"Hey! {invited[5].title()}, I'm having a dinner at my place tonight. You're invited.")
print()

print("Bad news my table wont alive on time so I'm gonna just invite two people only. Sorry guys.")
print()

# removing individual from the invitation list 
poped_people = invited.pop(5)
print(f"I'm sorry {poped_people.title()}, can't invite you tonight.")

poped_people = invited.pop(4)
print(f"I'm sorry {poped_people.title()}, can't invite you tonight.")

poped_people = invited.pop(2)
print(f"I'm sorry {poped_people.title()}, can't invite you tonight.")

poped_people = invited.pop(0)
print(f"I'm sorry {poped_people.title()}, can't invite you tonight.")
print()

# send message to only two of remained people
print(f"{invited[1].title()},Good news you are still invited")
print(f"{invited[0].title()},Good news you are still invited")
print()

del invited[0]
del invited[0]
print(invited)
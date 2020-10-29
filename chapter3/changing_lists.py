# adding and removing item from the list
favourite = ['honda', 'ferali', 'lamborghini']

favourite.append('yamaha', 'suzuki', 'ducati') #add new list to an existing list
favourite.insert(2, 'maserati') #insert maserati into a list
favourite_poped = favourite.pop() #list the last item from the list but still lets you use that item later
print(favourite_poped)
favourite.remove('yamaha') #remove an item using its value
del favourite[2] #delete an item from the list by it's index
print(favourite)
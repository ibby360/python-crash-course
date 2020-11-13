def make_album(artist,title,tracks=0):
    """
    Building a dictionary containing informati0n about an album
    """
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# prepare user prompt
title_prompt = ("\nWhat album do you like? ")
artist_prompt = ("Who is the artist? ")
print("Enter 'quit' to quit the program.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break
    
    album = make_album(title,artist)
    print(album)


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

album = make_album('lil way','carter v')
print(album)

album = make_album('august alsiana','this thing called life')
print(album)

album = make_album('future','supper fly')
print(album)

album = make_album('ozuna','nibiru',tracks=15)
print(album)
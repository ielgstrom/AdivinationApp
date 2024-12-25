import webbrowser

import spotipy
import random
def get_random_album(sp):
    # Fetch saved albums from the library
    results = sp.current_user_saved_albums(limit=50,market="ES")  # Fetch up to 50 saved albums

    albums = results['items']
    total_albums = len(albums)
    random_album = albums[random.randrange(total_albums)]
    album_id = random_album['album']['id']
    return album_id


def get_random_song_of_album(sp,album_id):
    results = sp.album_tracks(album_id=album_id, limit=50, offset=random.randrange(20), market="ES")
    tracks = results['items']
    album_tracks = len(results['items'])
    random_song = tracks[random.randrange(album_tracks)-1]
    print(random_song['name'])
    webbrowser.open(random_song['uri'])
    return random_song['name'], random_song['uri']


def play_song(sp, device, track_url):
    sp.start_playback(device_id=device, uris=[track_url])


def get_device_id(sp):
    print(sp.devices()['devices'][0]['id'])


def get_album_art(sp, album_id):
    album_info = sp.album(album_id)
    result_image_url = ''
    if album_info['images'] is not None:
        result_image_url = album_info['images'][0]['url']
    return result_image_url


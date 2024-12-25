import random
from io import BytesIO

import requests
import spotipy
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from keys import *

CLIENT_ID = CLIENT_ID_SPOTIFY
CLIENT_SECRET = CLIENT_SECRET_SPOTIFY
REDIRECT_URI = "http://localhost:8000/callback"

# Set the scope for accessing saved albums
SCOPE = 'user-library-read user-read-playback-state user-modify-playback-state'

# Authenticate with Spotify using OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))


# Function to get saved albums
def get_random_album():
    # Fetch saved albums from the library
    results = sp.current_user_saved_albums(limit=50,market="ES")  # Fetch up to 50 saved albums

    albums = results['items']
    total_albums = len(albums)
    random_album = albums[random.randrange(total_albums)]
    album_id = random_album['album']['id']
    return album_id


def get_random_song_of_album(album_id):
    results = sp.album_tracks(album_id=album_id, limit=50, offset=random.randrange(20), market="ES")
    tracks = results['items']
    album_tracks = len(results['items'])
    random_song = tracks[random.randrange(album_tracks)-1]
    print(random_song['name'])
    webbrowser.open(random_song['uri'])
    return random_song['name'], random_song['uri']


def play_song(device, track_url):
    sp.start_playback(device_id=device, uris=[track_url])


def get_device_id():
    print(sp.devices()['devices'][0]['id'])

def get_album_art(album_id):
    album_info = sp.album(album_id)
    result_image_url= ''
    if album_info['images'] is not None:
        result_image_url = album_info['images'][0]['url']
    return result_image_url


random_album_id = get_random_album()

name, uri = get_random_song_of_album(random_album_id)

play_song(get_device_id(),uri)

print("album_id: " + random_album_id)

album_art_url = get_album_art(random_album_id)
print("album art id: "+ album_art_url)
response = requests.get(album_art_url)
img = Image.open(BytesIO(response.content))
img.show()
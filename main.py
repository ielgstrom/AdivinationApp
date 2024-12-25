import random
from io import BytesIO
import requests
from PIL import Image
from spotipy.oauth2 import SpotifyOAuth
from keys import *
from helpers import *

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
random_album_id = get_random_album(sp)

name, uri = get_random_song_of_album(sp,random_album_id)

play_song(sp, get_device_id(sp), uri)
album_art_url = get_album_art(sp,random_album_id)
response = requests.get(album_art_url)
img = Image.open(BytesIO(response.content))
img.show()
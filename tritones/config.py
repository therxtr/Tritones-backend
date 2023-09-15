import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

client_id = '472ce029dca4423e8ed3a19b8c76ea29'
client_secret = '74f3bc1f0fe9424297c41b5b9fd1897e'

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
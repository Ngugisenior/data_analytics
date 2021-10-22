import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


url = 'https://api.spotify.com/v1/'

def get_play_lists(url):
    url = url+'/playlists/'
    return requests.get(url)
get_play_lists(url)
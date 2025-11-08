from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
USERNAME = str(os.getenv("SUB_USERNAME"))
PASSWORD = str(os.getenv("SUB_PASSWORD"))
VERSION = str(os.getenv("SUB_VERSION"))
FORMAT = str(os.getenv("SUB_FORMAT"))
BASE_URL = str(os.getenv("SUB_BASE_URL"))

default_params = {
    'u' : USERNAME,
    'p' : PASSWORD,
    'v' : VERSION,
    'c' : 'myapp',
    'f' : FORMAT,
}

def make_requests(path, extra_params = {}):
    parameters = default_params | extra_params
    base_url = "http://" + BASE_URL + "/rest/" + str(path)
    response = requests.get(base_url, params = parameters)
    return response

def all_artists():
    artists_json = make_requests('getArtists')
    artists = json.loads(artists_json.text)
    formatted = {}
    for index in artists['subsonic-response']['artists']['index']:
        for item in index['artist']:
            formatted[item['name']] = item['id']
    return formatted

artists = all_artists()

class RequestsLib():
    def get_album(self, name):
        singleartist_json = make_requests('getArtist', {'id' : artists[name]})
        singleartist = singleartist_json.json()
        formatted = {}
        for album in singleartist['subsonic-response']['artist']['album']:
           formatted[album['name']] = album['id']
        return formatted

    def get_songs(self, artist, album_name):
        songs_json = make_requests('getAlbum', {'id' : artist[album_name]})
        songs_py = json.loads(songs_json.text)
        formatted = {}
        for songs in songs_py['subsonic-response']['album']['song']:
            formatted[songs['title']] = songs['id']
        return formatted


    def play_song(self, id):
        r = make_requests("stream", {"id" : id})
        return r.url

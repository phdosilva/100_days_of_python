from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = "2000-08-12"

url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

songs_names = [title.getText().strip() for title in soup.select("div li ul li h3")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://localhost",
        client_id="6c143e4336264a4197282ff2d1064130",
        client_secret="54774831a18a4c1e986a2b4f6c980246",
        show_dialog=True,
        cache_path="token.txt"
    )
)

songs_uris = []
year = date.split("-")[0]
for song in songs_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


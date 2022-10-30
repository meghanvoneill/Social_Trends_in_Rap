import sys
import requests
import lyricsgenius as lg
import urllib
from bs4 import BeautifulSoup



#file = open("data/auto_.txt", "w")

#genius = lg.Genius(' ', skip_non_songs=True,
#                   excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)




# Borrowed from Ekene A. published in Towards Data Science:
#       https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29
def gather_lyric_data_from_genius_api(arr, k):

    url = 'http://api.genius.com'

    search_url = url + "/search"

    ACCESS_TOKEN = ' '

    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }

    params = {}

    result = requests.get('https://api.genius.com/artists/16775', headers=headers)
    print(result)
    print(result.content)

    for name in arr:
        artist_search_url = search_url
        artist_search_url += '?q=' + urllib.parse.quote_plus(name)
        print(artist_search_url)
        result = requests.get(artist_search_url, headers=headers)

        print(result)

    # c = 0
    # for name in arr:
    #     try:
    #         artist = genius.search_artist(name, max_songs=k, sort='popularity')
    #         print('hey')
    #         print(artist)
    #         # songs = artist.songs
    #         # s = [song.lyrics for song in songs]
    #         # file.write("\n \n   <|endoftext|>   \n \n".join(s))
    #         # c += 1
    #         # print(f"Songs grabbed:{len(s)}")
    #     except:
    #         print("Oops!", sys.exc_info()[1], "occurred.")
    #         print(f"some exception at {name}: {c}")


def gather_music_data_from_apple_music():

    url = 'https://api.music.apple.com'

    search_url = url + "/search"

    ACCESS_TOKEN = ' '

    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN,
        'alg': 'ES256',
        'kid': ' '
    }

    params = {}

    claims = {
        'iss': ' ',
        'iat': ' ',
        'exp': ' '
    }

    # SZA : 605800394

    result = requests.get(url, headers=headers, claims=claims)

    return


def gather_artist_data_from_billboard():

    url = "https://www.billboard.com/charts/r-and-b-songs/"

    querystring = {} #{"range": "1-10", "date": "2019-05-11"}

    headers = {}

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title)

    not_artist_strings_known = ['Follow Billboard on instagram', 'Follow Billboard on twitter', 'Follow Billboard on facebook', 'GET ACCESS TODAY', 'Expand more menu', 'Expand pro-tools menu', 'Expand business menu', 'Expand media menu', 'Expand culture menu', 'Expand music menu', 'Expand charts menu', 'Close the menu', 'Login', 'PMC Logo', 'Icon Link', 'Send us a tip', 'Sign Up', 'Embed', 'Share Chart on Embed', 'Facebook', 'Share Chart on Facebook', 'Copy Link', 'Share Chart on Copy Link', 'Twitter', 'Share Chart on Twitter', '×', 'Open menu', 'Click to Expand Search Input', 'Search for:', 'Billboard', 'Español', 'Open menu', 'Search', 'LOGIN', 'Account\n\t\t\t\n\n\n\n\n\n\n\tManage Account\n\n\n\n\n\t\tLog Out', 'Log Out', 'All Charts', 'Menu', 'Close', 'Datepicker', 'Info', 'Share', 'Share this article on Facebook', 'Share this article on Twitter', 'Share this article on Tumblr', '+ additional share options added', 'Share this article on Pinit', 'Share this article on Reddit', 'Share this article on Linkedin', 'Share this article on Whatsapp', 'Share this article on Email', 'Print this article', 'Share this article on Comment', 'Plus Icon', 'This Week', 'Award', 'Last Week', 'Peak Pos.', 'Wks on Chart', 'RIAA Certification:', 'Platinum', 'Platinum x4']
    for num in range(0, 42):
        new_string = str(num)
        not_artist_strings_known.append(new_string)

    artists_found = []

    for child in soup.descendants:

        if child.name == 'span':
            if child.text.strip() not in not_artist_strings_known and len(child.text.strip()) > 0:
                print(child.text)
                artists_found.append(child.text.strip())

    print(artists_found)

    return artists_found


def combine_data_types(k):

    artists = gather_artist_data_from_billboard()

    # gather_lyric_data_from_genius_api(artists, k)

    gather_music_data_from_apple_music(artists)

    return


def main():

    combine_data_types(k=3)

    return


if __name__ == '__main__':
    main()

import sys
import requests
import lyricsgenius as lg
import urllib
from bs4 import BeautifulSoup
from datetime import datetime


# Borrowed from Ekene A. published in Towards Data Science:
#       https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29
def gather_lyric_data_from_genius_api(arr, k):
    url = 'http://api.genius.com'

    search_url = url + '/search'

    ACCESS_TOKEN = ' '

    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }

    params = {}

    result = requests.get('https://api.genius.com/artists/16775', headers=headers)
    print(result)
    print(result.content)

    return result

    # for name in arr:
    #     artist_search_url = search_url
    #     artist_search_url += '?q=' + urllib.parse.quote_plus(name)
    #     print(artist_search_url)
    #
    #     result = requests.get(artist_search_url, headers=headers)
    #     print(result)

    # file = open("data/auto_.txt", "w")
    # genius = lg.Genius(' ', skip_non_songs=True,
    #                   excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
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


def gather_music_data_from_apple_music(artists):
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


def gather_artist_data_from_billboard(date=''):
    """ Scrapes Billboard.com's R&B song charts for the artists with the top 25 songs for a given date,
        or for the current date, if none is given.

        Earliest date available on Billboard.com is '2012-10-20'.
    """

    try:
        date_time = datetime.strptime(date, '%Y-%m-%d').date()
    except:
        print('Error: Improper date format.')
        return []
    min_date = datetime.strptime('2012-10-20', '%Y-%m-%d').date()
    if date_time < min_date:
        print('Error: Cannot accept dates before \'2012-10-20\'')
        return []

    url = 'https://www.billboard.com/charts/r-and-b-songs/'

    if date != '':
        url += date + '/'

    querystring = {}  # {"range": "1-10", "date": "2019-05-11"}

    headers = {}

    response = requests.request('GET', url, headers=headers, params=querystring)

    soup = BeautifulSoup(response.text, 'html.parser')

    not_artist_strings_known = ['Follow Billboard on instagram', 'Follow Billboard on twitter',
                                'Follow Billboard on facebook', 'GET ACCESS TODAY', 'Expand more menu',
                                'Expand pro-tools menu', 'Expand business menu', 'Expand media menu',
                                'Expand culture menu', 'Expand music menu', 'Expand charts menu', 'Close the menu',
                                'Login', 'PMC Logo', 'Icon Link', 'Send us a tip', 'Sign Up', 'Embed',
                                'Share Chart on Embed', 'Facebook', 'Share Chart on Facebook', 'Copy Link',
                                'Share Chart on Copy Link', 'Twitter', 'Share Chart on Twitter', '×', 'Open menu',
                                'Click to Expand Search Input', 'Search for:', 'Billboard', 'Español', 'Open menu',
                                'Search', 'LOGIN', 'Account\n\t\t\t\n\n\n\n\n\n\n\tManage Account\n\n\n\n\n\t\tLog Out',
                                'Log Out', 'All Charts', 'Menu', 'Close', 'Datepicker', 'Info', 'Share',
                                'Share this article on Facebook', 'Share this article on Twitter',
                                'Share this article on Tumblr', '+ additional share options added',
                                'Share this article on Pinit', 'Share this article on Reddit',
                                'Share this article on Linkedin', 'Share this article on Whatsapp',
                                'Share this article on Email', 'Print this article', 'Share this article on Comment',
                                'Plus Icon', 'This Week', 'Award', 'Last Week', 'Peak Pos.', 'Wks on Chart',
                                'RIAA Certification:', 'Platinum', 'Platinum x2', 'Platinum x3', 'Platinum x4',
                                'Platinum x5', 'Platinum x6', 'Platinum x7', 'Platinum x8', 'Platinum x9', '-',
                                'RE-\nENTRY', 'NEW', 'Gold']
    for num in range(0, 42):
        new_string = str(num)
        not_artist_strings_known.append(new_string)

    artists_found = []

    for child in soup.descendants:
        if child.name == 'span':
            if child.text.strip() not in not_artist_strings_known and len(child.text.strip()) > 0:
                artists_found.append(child.text.strip())

    return artists_found


def gather_song_data_from_billboard(date=''):
    """ Scrapes Billboard.com's R&B song charts for the top 25 songs for a given date,
        or for the current date, if none is given.

        Earliest date available on Billboard.com is '2012-10-20'.
    """

    try:
        date_time = datetime.strptime(date, '%Y-%m-%d').date()
    except:
        print('Error: Improper date format.')
        return []
    min_date = datetime.strptime('2012-10-20', '%Y-%m-%d').date()
    if date_time < min_date:
        print('Error: Cannot accept dates before \'2012-10-20\'')
        return []

    url = 'https://www.billboard.com/charts/r-and-b-songs/'

    if date != '':
        url += date + '/'

    querystring = {}  # {"range": "1-10", "date": "2019-05-11"}

    headers = {}

    response = requests.request('GET', url, headers=headers, params=querystring)

    soup = BeautifulSoup(response.text, 'html.parser')

    not_song_strings_known = ['Follow Billboard on instagram', 'Follow Billboard on twitter',
                              'Follow Billboard on facebook', 'GET ACCESS TODAY', 'Expand more menu',
                              'Expand pro-tools menu', 'Expand business menu', 'Expand media menu',
                              'Expand culture menu', 'Expand music menu', 'Expand charts menu', 'Close the menu',
                              'Login', 'PMC Logo', 'Icon Link', 'Send us a tip', 'Sign Up', 'Embed',
                              'Share Chart on Embed', 'Facebook', 'Share Chart on Facebook', 'Copy Link',
                              'Share Chart on Copy Link', 'Twitter', 'Share Chart on Twitter', '×', 'Open menu',
                              'Click to Expand Search Input', 'Search for:', 'Billboard', 'Español', 'Open menu',
                              'Search', 'LOGIN', 'Account\n\t\t\t\n\n\n\n\n\n\n\tManage Account\n\n\n\n\n\t\tLog Out',
                              'Log Out', 'All Charts', 'Menu', 'Close', 'Datepicker', 'Info', 'Share',
                              'Share this article on Facebook', 'Share this article on Twitter',
                              'Share this article on Tumblr', '+ additional share options added',
                              'Share this article on Pinit', 'Share this article on Reddit',
                              'Share this article on Linkedin', 'Share this article on Whatsapp',
                              'Share this article on Email', 'Print this article', 'Share this article on Comment',
                              'Plus Icon', 'This Week', 'Award', 'Last Week', 'Peak Pos.', 'Wks on Chart',
                              'RIAA Certification:', 'Platinum', 'Platinum x4', 'Songwriter(s):', 'Producer(s):',
                              'Imprint/Promotion Label:', 'Gains in Weekly Performance', 'Additional Awards',
                              'Follow Us', 'Have a Tip?', 'The Daily', 'More\n\n\n\n\t\t\t\t\tExpand more menu',
                              'Culture\n\n\n\n\t\t\t\t\tExpand culture menu',
                              'Media\n\n\n\n\t\t\t\t\tExpand media menu',
                              'Business\n\n\n\n\t\t\t\t\tExpand business menu',
                              'Pro Tools\n\n\n\n\t\t\t\t\tExpand pro-tools menu', 'The Daily', 'Have a Tip?', 'Account',
                              'Charts\n\n\n\n\t\t\t\t\tExpand charts menu', 'Music\n\n\n\n\t\t\t\t\tExpand music menu']
    for num in range(0, 42):
        new_string = str(num)
        not_song_strings_known.append(new_string)

    songs_found = []

    for child in soup.descendants:
        if child.name == 'h3':
            if child.text.strip() not in not_song_strings_known and len(child.text.strip()) > 0:
                songs_found.append(child.text.strip())

    return songs_found[2:27]


def combine_data_types(k, date=''):
    """ Takes data from multiple sources and combines them into one data vector per song.
        Sources include Billboard.com, Apple Music, and Genius.com.

        date: '2012-10-20'
    """

    artists = gather_artist_data_from_billboard(date=date)
    print(artists)

    songs = gather_song_data_from_billboard(date=date)
    print(songs)

    songs_and_artists = {songs[i]: artists[i] for i in range(len(songs))}
    print(songs_and_artists)

    # gather_lyric_data_from_genius_api(artists, k)

    # gather_music_data_from_apple_music(artists)

    return


def main():

    # combine_data_types(k=3, date='2012-10-25')

    artists = ['Rhianna']   # ['Beyoncé', 'Rhianna', 'Doja Cat']
    k = 3

    gather_lyric_data_from_genius_api(artists, k)

    return


if __name__ == '__main__':
    main()

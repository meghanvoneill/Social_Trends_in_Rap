import sys
import requests
import lyricsgenius as lg

ACCESS_TOKEN = ' '

file = open("/Users/meghanvoneill/PycharmProjects/Music_Project/Social_Trends_in_Rap/data/auto_.txt", "w")

genius = lg.Genius(' ', skip_non_songs=True,
                   excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
url = 'https://api.genius.com'

search_url = url + "/search"

headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

params = {}

result = requests.get(url, params=params, headers=headers)


# Borrowed from Ekene A. published in Towards Data Science:
#       https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29
def gather_lyric_data_from_genius_api(arr, k):
    c = 0
    for name in arr:
        try:
            artist = genius.search_artist(name, max_songs=k, sort='popularity')
            print('hey')
            print(artist)
            # songs = artist.songs
            # s = [song.lyrics for song in songs]
            # file.write("\n \n   <|endoftext|>   \n \n".join(s))
            # c += 1
            # print(f"Songs grabbed:{len(s)}")
        except:
            print("Oops!", sys.exc_info()[1], "occurred.")
            print(f"some exception at {name}: {c}")


def main():

    artists = ['Armani White', 'Roddy Ricch']
    k = 3

    gather_lyric_data_from_genius_api(artists, k)

    return


if __name__ == '__main__':
    main()

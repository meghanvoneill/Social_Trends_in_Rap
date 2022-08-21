from data_collecting import *


def main():

    arr = ['Beyoncé', 'Rhianna', 'Doja Cat']
    k = 3

    gather_lyric_data_from_genius_api(arr, k)

    return


if __name__ == '__main__':
    main()

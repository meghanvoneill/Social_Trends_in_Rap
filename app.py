from data_collecting import *
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


# def main():
#
#     arr = ['Beyoncé', 'Rhianna', 'Doja Cat']
#     k = 3
#
#     gather_lyric_data_from_genius_api(arr, k)
#
#     return
#
#
# if __name__ == '__main__':
#     main()

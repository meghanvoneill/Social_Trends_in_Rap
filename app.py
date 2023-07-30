from data_collecting import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    artists = ['Rhianna']   # ['Beyoncé', 'Rhianna', 'Doja Cat']
    k = 3

    # result = gather_lyric_data_from_genius_api(artists, k)
    # return str(result)

    return render_template('index.html')


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
if __name__ == '__main__':
    app.run(host="0.0.0.0")

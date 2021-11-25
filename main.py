from flask import Flask, request
import pyshorteners
import pandas as pd
import os.path

app = Flask(__name__)


@app.route('/', methods=['POST'])
def url_shortener():
    original_url = request.form.get('url')
    link = pyshorteners.Shortener()
    shortened_url = link.tinyurl.short(original_url)

    update_url_data_file(original_url, shortened_url)

    return shortened_url


def update_url_data_file(original_url, shortened_url):
    dataframe = pd.DataFrame({'original_url': [original_url], 'shortened_url': [shortened_url]})
    dataframe.to_csv('urlData.csv', mode='a', header=False)


def check_file():
    return os.path.exists('urlData.csv')


if __name__ == '__main__':
    if check_file():
        print('urlData.csv file exists')
    else:
        f = open('urlData.csv', 'w')
        original_url_list = []
        shortened_url_list = []
        url_dict = {'original_URL': original_url_list, 'shortened_URL': shortened_url_list}
        df = pd.DataFrame(url_dict)
        df.to_csv('urlData.csv')
    app.run()

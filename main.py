import hashlib
import os.path

import pandas as pd
from flask import Flask, request
from urllib.parse import urlparse

app = Flask(__name__)


@app.route('/', methods=['POST'])
def url_shortener():
    original_url = request.form.get('url')
    if is_url(original_url):
        hashed_url = hashlib.sha1(original_url.encode("UTF-8")).hexdigest()
        shortened_url = "ic.io/" + hashed_url[:10]

        update_url_data_file(original_url, shortened_url)

        return shortened_url
    else:
        return "Invalid URL \n(Expected URL format : http://www.abc.com)"


def is_url(original_url):
    try:
        result = urlparse(original_url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def update_url_data_file(original_url, shortened_url):
    dataframe = pd.DataFrame({'original_url': [original_url], 'shortened_url': [shortened_url]})
    dataframe.to_csv('urlData.csv', mode='a', header=False)


def check_file(url_data_file):
    return os.path.exists(url_data_file)


if __name__ == '__main__':
    if check_file('urlData.csv'):
        print('urlData.csv file exists')
    else:
        f = open('urlData.csv', 'w')
        original_url_list = []
        shortened_url_list = []
        url_dict = {'original_URL': original_url_list, 'shortened_URL': shortened_url_list}
        df = pd.DataFrame(url_dict)
        df.to_csv('urlData.csv')
    app.run()

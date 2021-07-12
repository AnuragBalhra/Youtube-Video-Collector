import urllib
import requests


def fetch_list_of_video(published_after, keyword, APIKEY, next_page_token):
    base_url = 'https://youtube.googleapis.com/youtube/v3/search?'
    params = {
        'type': 'video',
        'key': APIKEY,
        'order': 'date',
        'publishedAfter': published_after,
        'q': keyword,
        'maxResults': 50,
        'part': 'snippet'
    }
    if next_page_token:
        params['pageToken'] = next_page_token

    url = base_url + urllib.parse.urlencode(
        params, safe='+=/', quote_via=urllib.parse.quote
    )
    resp = requests.get(url)
    return resp

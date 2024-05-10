#!/usr/bin/python3
"""
Prints the first 10 hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)

#!/usr/bin/python3
"""Python module that queries the Reddit API and returns the
number of sunscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Obtains number of subscribers in a parsed
    subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Setting up a custom User-Agent to avoid too many Request errors
    headers = {'User-Agent': 'Google Chrome Version 98.0.4758.102'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        info = response.json()
        number_of_subscribers = info['data']['subscribers']
        return (number_of_subscribers)
    else:
        return 0

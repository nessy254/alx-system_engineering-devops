#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API and
    returns the number of subscribers
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers  = {'User-Agent':"Chrome/98.0.4758.102"}
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        info = response.json()
        subscribers = info['data']['subscribers']

        return (subscribers)
    else:
        return 0




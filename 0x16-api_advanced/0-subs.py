#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of
isubscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Google Chrome Version 98.0.4758.102"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
#!/usr/bin/python3
"""returns the number of subscribers
    https://note.nkmk.me/python-requests-usage/"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")

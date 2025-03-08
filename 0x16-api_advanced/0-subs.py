#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. Returns 0 if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Google Chrome Version 133.0.6943.98'}
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    try:
        return response.json().get('data', {}).get('subscribers', 0)
    except ValueError:
        return 0

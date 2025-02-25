#!/usr/bin/python3
"""
Recursively fetches all hot post titles from a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to get the titles of all hot posts.

    Args:
        subreddit (str): The subreddit name.
        hot_list (list): A list to store the retrieved titles
        (default: empty list).
        after (str): The pagination parameter for recursion (default: None).

    Returns:
        list: A list of hot post titles or None if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Google Chrome Version 133.0.6943.98"
    }
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            return hot_list if hot_list else None

        for post in children:
            hot_list.append(post["data"].get("title", ""))

        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list

    except ValueError:
        return None

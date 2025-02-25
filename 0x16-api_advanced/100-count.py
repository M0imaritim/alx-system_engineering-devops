#!/usr/bin/python3
"""
Recursively fetches hot articles and counts given keywords in titles.
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively queries the Reddit API, parses titles of hot articles,
    and counts occurrences of keywords.

    Args:
        subreddit (str): The subreddit name.
        word_list (list): A list of keywords to count.
        word_count (dict): Dictionary to store word frequencies.
        after (str): The pagination parameter for recursion.

    Returns:
        None: Prints the word counts sorted as per the requirements.
    """
    if not subreddit or not isinstance(subreddit, str):
        return

    if not word_count:
        # Initialize word_count dictionary with case-insensitive words
        word_list = [word.lower() for word in word_list]
        word_count = {word: 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Google Chrome Version 133.0.6943.98"
    }
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children and not after:
            return

        for post in children:
            title = post["data"].get("title", "").lower()
            words = title.split()  # Split title into words

            for word in words:
                cleaned_word = "".join(filter(str.isalpha, word))
                if cleaned_word in word_count:
                    word_count[cleaned_word] += 1

        after = data.get("after")

        if after:
            return count_words(subreddit, word_list, word_count, after)

        sorted_words = sorted(
            [(word, count) for word, count in word_count.items() if count > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_words:
            print(f"{word}: {count}")

    except ValueError:
        return

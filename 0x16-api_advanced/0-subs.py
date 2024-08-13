#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{}/about.json"

    # Define headers, especially the User-Agent
    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If subreddit is invalid or request fails, return 0
        return 0

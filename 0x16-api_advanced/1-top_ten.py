#!/usr/bin/python3
import requests

"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

def top_ten(subreddit):
    # Define the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{}/hot.json?limit=10"

    # Define headers, especially the User-Agent
    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Loop through the first 10 posts and print their titles
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        # If subreddit is invalid or request fails, print None
        print(None)

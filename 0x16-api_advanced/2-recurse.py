#!/usr/bin/python3
import requests

    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """

def recurse(subreddit, hot_list=[], after=None):
    # Define the base URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{}/hot.json"

    # Add the 'after' parameter if it's not None (for pagination)
    params = {'after': after} if after else {}

    # Define headers, especially the User-Agent
    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the list of posts
        posts = data['data']['children']

        # Append the titles of the posts to hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there is another page of results
        after = data['data']['after']

        # If there is another page, recursively call the function
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            # If no more pages, return the full list of titles
            return hot_list
    else:
        # If subreddit is invalid or request fails, return None
        return None

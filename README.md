# Reddit Text To Speech
Used for browsing 'Hot' posts on Reddit which are then played through text to speech.

Just a basic script I threw together. Credentials file should contain credentials 
obtained from reddit.

https://github.com/reddit-archive/reddit/wiki/OAuth2

Config just contained the subreddit name without the /r/ and the limit is the number of 'Hot'
posts to display.

```
{
    "subreddit": "science",
    "limit": 30
}
```

You can press Ctrl C (keyboard interrupt to exit a post that is currently playing)

The entry point is reddit_tts.py and is using Python 3.

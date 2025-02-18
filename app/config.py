import os
from dotenv import load_dotenv

#.env load file
load_dotenv()

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
BASE_URL = "https://api.twitter.com/2"
HEADERS = {
    "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}",
    "User-Agent": "v2RecentSearchPython"
}
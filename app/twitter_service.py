import aiohttp
import json
from app.config import BASE_URL, HEADERS

class TwitterService:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS
        
    async def _send_request(self, url, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers=self.headers, params=params
            ) as response:
                return await response.json()
            
            
    async def search_recent_tweets(self, params: dict) -> dict:
        url = f"{self.base_url}/tweets/search/recent"

        return await self._send_request(url, params)


    async def recent_tweet_counts(self, params: dict) -> dict:
        url = f"{self.base_url}/tweets/counts/recent"

        return await self._send_request(url, params)


    async def retweed_lookup(self, params: dict) -> dict:
        url = f'{self.base_url}/tweets/{params["id"]}/retweeted_by'
        user_fields = params["user_fields"]
        return await self._send_request(url, user_fields)


    async def get_tweets(self, params: dict) -> dict:
        url = f'{self.base_url}/tweets?{params["ids"]}&{params["tweet_fields"]}'

        return await self._send_request(url)


    async def get_users(self, params: dict) -> dict:
        url = (
            f"{self.base_url}/users/by?{params['usernames']}&{params['user_fields']}"
        )

        return await self._send_request(url)


    async def user_mentions(self, params: dict, id: dict) -> dict:
        user_id = id["user_id"]
        url = f"{self.base_url}/users/{user_id}/mentions"

        return await self._send_request(url, params)
import aiohttp
import os
import json

#test icindir 

class Twitter:
    headers = {
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAOR%2BmAEAAAAAzvN%2BIupVT8kX805wNyjR5clBoaU%3D60bBGkLTRZWNSDE9yL2Dsdz9O52rhQz32Nooan6EjW7valYx4q",
        "User-Agent": "v2RecentSearchPython",
    }
    base_url = "https://api.twitter.com/2"

    
    async def create_tweet(self):
        
        payload = {"text": "Hello world!"}
    
    async def recent_search(self, payload: dict) -> dict:
        url = f"{self.base_url}/tweets/search/recent"

        return await self._get_send_request(url, payload)

    async def recent_tweet_counts(self, payload: dict) -> dict:
        url = f"{self.base_url}/tweets/counts/recent"

        return await self._get_send_request(url, payload)

    async def retweed_lookup(self, payload: dict) -> dict:
        url = f'{self.base_url}/tweets/{payload["id"]}/retweeted_by'
        user_fields = payload["user_fields"]
        return await self._get_send_request(url, user_fields)

    async def get_tweets(self, payload: dict) -> dict:
        url = f'{self.base_url}/tweets?{payload["ids"]}&{payload["tweet_fields"]}'

        return await self._get_send_request_without_params(url)

    async def get_users(self, payload: dict) -> dict:
        url = (
            f"{self.base_url}/users/by?{payload['usernames']}&{payload['user_fields']}"
        )

        return await self._get_send_request_without_params(url)

    async def user_mentions(self, payload: dict, id: dict) -> dict:
        #bu sekilde hata vermiyor
        user_id = id["user_id"]
        url = f"{self.base_url}/users/{user_id}/mentions"

        return await self._get_send_request(url, payload)

    async def _get_send_request(self, url, payload):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers=self.headers, params=payload
            ) as response:
                return await response.json()

    async def _get_send_request_without_params(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                return await response.json()

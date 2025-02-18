import pytest
import asyncio
from app.twitter_service import TwitterService

@pytest.mark.asyncio
async def test_search_recent_tweets():
    twitter = TwitterService()
    query = {
                "query": "(from:twitterdev -is:retweet) OR #twitterdev",
                "tweet.fields": "author_id",
    }
    response = await twitter.search_recent_tweets(query)
    
    assert isinstance(response, dict)
    assert "data" in response
    
@pytest.mark.asyncio
async def test_get_users():
    twitter = TwitterService()
    query_user_info = {
            "usernames": "usernames=JhonDoe,TwitterAPI",
            "user_fields": "user.fields=description,created_at",
    }
    response = await twitter.get_users(query_user_info)
    
    assert isinstance(response, dict)
    assert "data" in response
import asyncio
from app.twitter_service import TwitterService


async def main():
    twitter = TwitterService()


    print("🔍 Searching for recent tweets...")
    query = {
            "query": "(from:twitterdev -is:retweet) OR #twitterdev",
            "tweet.fields": "author_id",
        }
    tweets = await twitter.search_recent_tweets(query)
    print(tweets)
    
    
    #################Count
    
    print("\n📊 Fetching tweet counts...")
    query_count = {"query": "from:twitterdev", "granularity": "day"}

    tweet_counts = await twitter.recent_tweet_counts(query_count)
    print(tweet_counts)
    
    
    #################ReTweet Lookup
    
    print("\n📊 Re-tweet lookup...")
    query_re_tweet = {
            "user_fields": "user.fields=created_at,description",
            "id": "User-ID",
        }
    re_tweet_lookup = await twitter.retweed_lookup(query_re_tweet)
    print(re_tweet_lookup)
    
    
    #################User info
    
    print("\n👤 Fetching user info...")
    query_user_info = {
            "usernames": "usernames=JhonDoe,TwitterAPI",
            "user_fields": "user.fields=description,created_at",
        }
    users = await twitter.get_users(query_user_info)
    print(users)

if __name__ == "__main__":
    asyncio.run(main())
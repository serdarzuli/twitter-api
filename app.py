import asyncio
import twitter

app = twitter.Twitter()
query_params = {
            "query": "(from:twitterdev -is:retweet) OR #twitterdev",
            "tweet.fields": "author_id",
        }
result = asyncio.run(app.recent_search(query_params))
#print(result)


query_params1 = {"query": "from:twitterdev", "granularity": "day"}
result2 = asyncio.run(app.recent_tweet_counts(query_params))
#print(result2)


query_params2 = {
            "user_fields": "user.fields=created_at,description",
            "id": "1354143047324299264",
        }
result3 = asyncio.run(app.retweed_lookup(query_params2))
#print(result3)


query_params4 = {
            "tweet_fields": "tweet.fields=lang,author_id",
            "ids": "ids=1278747501642657792,1255542774432063488",
        }
# result4 = asyncio.run(app.get_tweets(query_params4))
# #print(result4)



payload1 = {
            "usernames": "usernames=zuliserdar,TwitterAPI",
            "user_fields": "user.fields=description,created_at",
        }
result5 = asyncio.run(app.get_users(payload1))
print(result5)


payload2 = {'tweet.fields': 'created_at'}
payload3 = {'user_id' : 897438674106949632}
#ayri ayri verdigimizde calisiyor beraber verdigimizde calismiyor
# result6 = asyncio.run(app.user_mentions(payload2,payload3))
# print(result6)
import oauth2
import json
import urllib.parse
from pprint import pprint

keys = ['WRXnyJds71yDayQaXFxPpI2jv', 
'AjpaogRVFUyuZTfvaNgwj08J0pD3n6f1k08BjUUlapnUFca2w4',
'799122088594460672-vzJloX2qozKzEuJhNuyB1oew8rJSEzF', 
'COd1bb65SodeBgD7zPTseuZ9lUBpkeeapROr0MXFprlqz'] 

class twitter:
    def __init__(self, keys):
        self.keys = keys

    def auth_twitter(self):
        consumer = oauth2.Consumer(keys[0], keys[1])
        token = oauth2.Token(keys[2], keys[3])
        client = oauth2.Client(consumer, token)
        return client

    def post_twitter(self, client):
        query = input("Novo tweet: ")
        query_coded = urllib.parse.quote(query, safe='')
        req = client.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_coded, method='POST')
        decoded = req[1].decode()
        obj = json.loads(decoded)
        return obj

res = twitter(keys)
client = res.auth_twitter()
post = res.post_twitter(client)
pprint(post)

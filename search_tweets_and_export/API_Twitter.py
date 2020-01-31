import json
import codecs
import oauth2
import urllib.parse

def consulting_twitter():    
    try:
        consumer_key = 'colar da API'
        consumer_secret = 'colar da API'

        token_key = 'colar da API'
        token_secret = 'colar da API'

        consumer = oauth2.Consumer(consumer_key, consumer_secret)
        token = oauth2.Token(token_key, token_secret)
        client = oauth2.Client(consumer, token)

        print('Pesquisar: ')
        query = input()
        coded_query = urllib.parse.quote(query, safe='')
        req = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + coded_query + '&lang=pt')

        decode = req[1].decode()

        obj = json.loads(decode)
        tweetes = obj['statuses']

        write_json(tweetes)
        write_txt(tweetes)
        write_txt_formated(tweetes)
        print('busca concluida')
    except Exception as e:
        print(e)
    
def write_json(list_json):
    f_json = open('tweets.json','w+')
    json.dump(list_json, f_json)
    f_json.close()

def write_txt(list_txt):
    f_txt = open('tweets.txt','wb')
    json.dump(list_txt, codecs.getwriter('utf-8')(f_txt), ensure_ascii=False)
    f_txt.close()
    
def write_txt_formated(list_txt):
    f_txt = open('tweets_formatado.txt', 'w', encoding='utf-8')
    for twit in list_txt:
        f_txt.write('Usuario: ' + twit['user']['screen_name'] + '\n')
        f_txt.write('Publicação: ' + twit['text'] + '\n')
        f_txt.write('\n') 
    
consulting_twitter()

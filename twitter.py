import oauth2
import json
import urllib.parse

class twitter:
    def __init__(self, configs_auth, configs_req):
        # Construir objetos de configuração 
        self.configs_auth = configs_auth 
        self.configs_req = configs_req 

    def auth_twitter(self):
        try:
            # Autenticar as chaves de consumer
            consumer = oauth2.Consumer(self.configs_auth['consumer_key'], self.configs_auth['consumer_secret'])
            # Autenticar as chaves de token
            token = oauth2.Token(self.configs_auth['token_key'], self.configs_auth['token_secret'])
            # Realizar a autenticação (Consumer/Token)
            client = oauth2.Client(consumer, token)            
            return client
        except Exception as e:
            return e

    def request_twitter(self, client):
        try:
            # Receber entrada do usuario
            query = input("Digite: ")
            # Codificar a query
            query_coded = urllib.parse.quote(query, safe='')
            # Realizar a requisição
            req = client.request(self.configs_req['url_post'] + query_coded + '&lang=pt', method='POST')
            # Decodificar a requisição
            decoded = req[1].decode()
            # Carregar json retornado
            obj = json.loads(decoded)            
            return obj
        except Exception as e:
            return e

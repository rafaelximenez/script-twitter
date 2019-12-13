import oauth2
import json
import urllib.parse
import configparser

class twitter:
    def __init__(self, configs_auth, configs_req):
        # COnstruir objetos de configuração 
        self.configs_auth = configs_auth 
        self.configs_req = configs_req 

    def auth_twitter(self):
        # Autenticar as chaves de consumer
        consumer = oauth2.Consumer(self.configs_auth['consumer_key'], self.configs_auth['consumer_secret'])
        # Autenticar as chaves de token
        token = oauth2.Token(self.configs_auth['token_key'], self.configs_auth['token_secret'])
        # Realizar a autenticação (Consumer/Token)
        client = oauth2.Client(consumer, token)
        return client

    def request_twitter(self, client):
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

if __name__ == "__main__":
    # Biblioteca para ler arquivo de 
    # configuração com chaves e urls para requisição
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Busca sessão auth_configuration e urls no config.ini
    config_auth = config['auth_configuration']
    config_req = config['urls']
    # Instancia a classe passando as configurações
    res = twitter(config_auth, config_req)
    # Faz a autenticação
    client = res.auth_twitter()
    # Realiza a requisição(POST/GET) para a API
    post = res.request_twitter(client)
    # Imprime o resultado
    print(post)

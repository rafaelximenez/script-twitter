import configparser
import twitter

if __name__ == "__main__":
    # Biblioteca para ler arquivo de 
    # configuração com chaves e urls para requisição
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Busca sessão auth_configuration e urls no config.ini
    config_auth = config['auth_configuration']
    config_req = config['urls']
    # Instancia a classe passando as configurações
    res = twitter.twitter(config_auth, config_req)
    # Faz a autenticação
    client = res.auth_twitter()
    # Realiza a requisição(POST/GET) para a API
    post = res.request_twitter(client)
    # Imprime o resultado
    print(post)

# APITwitter
Algoritmo simples que realiza uma busca no twitter e retorna os resultados em JSON e TXT

Para usar a API vá para o site do Twitter: https://twitter.com/ e crie uma conta. Feito isso, vá para o site de desenvolvimento do Twitter: https://developer.twitter.com e faça login. No canto superior direito da tela no menu, clique em "Apps. Na página seguinte, clique em "Create new application".

Preencha-a o formulário da sua aplicação. Ao finalizar será redirecionado para a página de sua aplicação, clique em "Details" em seguinda na aba "keys and tokens".

Os campos "Consumer key", "Consumer secret", "Access token" e "Access token secret" são os que devem ser guardados para utilizar em sua aplicação como autentificação.

Para que este algoritmo funcione corretamente, você precisa ter o python instalado em seu computador e as bibliotecas requests, json, codecs, oauth2, urllib:

##Comandos para instalação##

pip install requests

pip install json

pip install codecs

pip install oauth2

pip install urllib
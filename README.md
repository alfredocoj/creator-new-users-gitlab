# Cria novos usuarios Gitlab

Esse script python cria usuário(s) a partir de um arquivo .xls no Gitlab. Para isso utiliza bibliotecas do python e a API do gitlab.


## Prerequisitos

1. Para começar a usar essa lib é preciso criar um Token com perfil administrativo no gitlab, ver [link](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

2. Criar um arquivo .env com o valor do token, conforme .env.example.

3. Instalação:
```
pip install xlrd

pip install requests

pip install -U python-dotenv
```
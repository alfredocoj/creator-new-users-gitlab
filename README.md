# Cria novos usuarios Gitlab

Esse script python cria usuário(s) a partir de um arquivo .xls no Gitlab. Para isso utiliza bibliotecas do python e a API do gitlab.


## Pré-requisitos

1. Instalação do Python
 
 - Linux
 
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

 - Windows: [https://www.python.org/downloads/](https://www.python.org/downloads/)
 
2. Para começar a usar essa lib é preciso criar um Token com perfil administrativo no gitlab, ver [link](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

3. Criar um arquivo .env com o valor do token criado no passo 2 e password, conforme .env.example.

4. Instalação de libs:

```
pip install xlrd

pip install requests

pip install -U python-dotenv
```

## Execução

```
python script.py
```

# Rerefências

[https://docs.gitlab.com/ee/api/users.html#user-creation](https://docs.gitlab.com/ee/api/users.html#user-creation)

[https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html](https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html)

[https://docs.gitlab.com/ee/api/members.html](https://docs.gitlab.com/ee/api/members.html)

[https://docs.gitlab.com/ee/api/access_requests.html](https://docs.gitlab.com/ee/api/access_requests.html)

[https://github.com/theskumar/python-dotenv](https://github.com/theskumar/python-dotenv)
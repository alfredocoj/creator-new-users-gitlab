# Reading an excel file using Python
import xlrd
import requests
import urllib3
import os
import sys
from dotenv import load_dotenv
from pathlib import Path  # python3 only

## inicializations
load_dotenv()
# OR, the same with increased verbosity
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
headers = {'content-type': 'application/json', 'Private-Token': os.getenv("PRIVATE_TOKEN")}
urllib3.disable_warnings()

# Get .xls file
FILE_XLS = input("Entre com o caminho do arquivo .xls: ")
assert os.path.exists(FILE_XLS), "I did not find the file at, "+str(FILE_XLS)

print(FILE_XLS)
# Give the location of the file
loc = (FILE_XLS)

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

## Get Team/Group
response_groups = requests.get("https://gitlab.mateus/api/v4/groups/", headers=headers, verify=False).json()

for index in range(len(response_groups)):
    groups = {'id': response_groups[index]['id'], 'time': response_groups[index]['name']}
    print(groups)

grupo_id = input("Digite o ID do time: ")

for i in range(sheet.nrows-1):
    organization = sheet.cell_value(i + 1, 0)
    name = sheet.cell_value(i+1, 1)
    email = sheet.cell_value(i + 1, 2)
    public_email = email
    username = email.split("@")
    password = os.getenv("PASSWORD")

    data = {'name': name, 'username': username[0], 'email': email, 'public_email': public_email, 'password': password, 'reset_password': False, 'force_random_password': False, 'organization': organization, 'location': 'São Luís - MA', 'skip_confirmation': True}

    print("Criando usuário: ")
    response = requests.post("https://gitlab.mateus/api/v4/users", json=data, headers=headers, verify=False)
    user = response.json()
    print(user)

    ## Add a member to a group or project
    ## POST /groups/:id/members
    ## 30 = > Perfil Developer
    access_level = 30
    user_perfil = {'user_id': user['id'], 'access_level': access_level}

    response_group = requests.get("https://gitlab.mateus/api/v4/groups/" + grupo_id, json=user_perfil, headers=headers, verify=False)
    print(response_group.json())
    response_add_group = requests.post("https://gitlab.mateus/api/v4/groups/"+grupo_id+"/members", json=user_perfil, headers=headers, verify=False)
    print("Vinculando o usuario ao time: ")
    print(response_add_group.json())

print("Script finalizado!")
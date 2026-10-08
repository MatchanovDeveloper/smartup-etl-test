import json
import base64


ENDPOINTS = {
    'inventory': 'https://smartup.online/b/anor/mxsx/mr/inventory$export',
    'order': 'https://smartup.online/b/trade/txs/tdeal/order$export',
    'return': 'https://smartup.online/b/anor/mxsx/mdeal/return$export',
    'write_off': 'https://smartup.online/b/anor/mxsx/mkw/writeoff$export',
    'return_to_suppliers': 'https://smartup.online/b/anor/mxsx/mkw/return$export',
    'payment_from_clients': 'https://smartup.online/b/trade/txs/tcs/cashin$export',
    'cash_operations': 'https://smartup.online/b/anor/mxsx/mkcs/cash_operation$export',
    'bank_statements': 'https://smartup.online/b/anor/mxsx/mkcs/bank_operation$export',
    'product_group': 'https://smartup.online/b/anor/mxsx/mr/product_group$export',
    'inventory_price': 'https://smartup.online/b/anor/api/v2/mkf/product_price$export',
    'legal_entity': 'https://smartup.online/b/anor/mxsx/mr/legal_person$export',
    'natural_persons': 'https://smartup.online/b/anor/mxsx/mr/natural_person$export',
    'persons_group': 'https://smartup.online/b/anor/mxsx/mr/person_group$export'
}


with open('auth.json', 'r') as file:
    data = json.load(file)

PROJECT_CODE = data['PROJECT_CODE']
FILIAL_ID = data['FILIAL_ID']
username = data['username']
password = data['password']



# db_url
host = data['host']
database = data['Database']
user = data['user']
db_password = data['database_password']


# db_url = f"postgresql://{user}:{db_password}@{host}:5432/{database}"

# db_url = f"postgresql://postgres:mdev3112@localhost:5432/smartup"

db_url = f"postgresql://postgres:mdev3112@host.docker.internal:5432/smartup"

def get_headers():
    token = base64.b64encode(
        f"{username}:{password}".encode()
    ).decode()

    header = {
        "Authorization": f"Basic {token}",
        "project_code": PROJECT_CODE,
        "filial_id": FILIAL_ID
    }

    return header

get_headers()

from client import get_data
from config import ENDPOINTS
import pandas as pd
from load import loader


### EXTRACT

# legal_entity

legal_entity_df = get_data(ENDPOINTS['legal_entity'], 'legal_person')

## TRANSFORM
legal_entity_df = legal_entity_df.loc[
    legal_entity_df['state'] == 'A',
    [
        'person_id',
        'name',
        'main_phone',
        'telegram',
        'address',
        'email'
    ]
]

legal_entity_df['type'] = 'legal_person'

legal_entity_df.dtypes
legal_entity_df['person_id'] = pd.to_numeric(legal_entity_df['person_id'], errors='coerce')



# EXTRACT

# natural_persons

natural_persons_df = get_data(ENDPOINTS['natural_persons'], 'natural_person')

## TRANSFORM
natural_persons_df['name'] = natural_persons_df['first_name'] + ' ' + natural_persons_df['last_name']

natural_persons_df = natural_persons_df.loc[
    natural_persons_df['state'] == 'A',
    [
        'person_id',
        'name',
        'main_phone',
        'telegram',
        'address',
        'email'
    ]
]

natural_persons_df['type'] = 'natural_person'

natural_persons_df = natural_persons_df.drop_duplicates(inplace=False)

natural_persons_df['person_id'].dropna(inplace=True)

natural_persons_df['person_id'] = pd.to_numeric(natural_persons_df['person_id'], errors='coerce')


# Ikkala tablelarni qo'shish

customers_df = pd.concat([legal_entity_df, natural_persons_df])





### LOAD

print('Customers jadvalini Databasega yuklash boshlandi...')
loader(customers_df, 'customers')
print("Customers muvaffaqiyatli Databasega yuklandi!!!")






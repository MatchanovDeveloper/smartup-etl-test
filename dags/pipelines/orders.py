import pandas as pd
from config import ENDPOINTS
from client import get_data
from load import loader
import json

### ETXRACT
orders_df = get_data(ENDPOINTS['order'], 'order')
df = orders_df

### TRANSFORM
df.dtypes

df['filial_id'] = pd.to_numeric(df['filial_id'])
df['deal_id'] = pd.to_numeric(df['deal_id'])
df['delivery_number'] = pd.to_numeric(df['delivery_number'])
df['deal_time'] = pd.to_datetime(df['deal_time'], errors='coerce')
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
df['booked_date'] = pd.to_datetime(df['booked_date'])
df['total_amount'] = pd.to_numeric(df['total_amount'])
df['room_id'] = pd.to_numeric(df['room_id'])
df['sales_manager_id'] = pd.to_numeric(df['sales_manager_id'])

df['filial_id'] = df['filial_id'].dropna(inplace=False)


## Nested ustunlarni olib tashlayman

orders = df.copy()

orders = orders.drop(columns=['order_products', 'order_gifts', 'order_actions', 'order_consignments'])

# df = df.drop_duplicates(inplace=False)

### LOAD

print('Orders table is uploading to the DATABASE')
loader(orders, 'orders')
print("Orders table successfully uploaded to the DATABASE")


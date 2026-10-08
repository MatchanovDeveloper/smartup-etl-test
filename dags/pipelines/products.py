from config import ENDPOINTS
from client import get_data
import pandas as pd
from load import loader


# EXTRACT

def products_etl():

    products_df = get_data(ENDPOINTS['inventory'], 'inventory')

    df = products_df[products_df['state'] == 'A']

    # ==== TRANSFORM ====
    # df = products_df


    # ---typeni o'zgartirdim
    df.dtypes

    df['product_id'] = pd.to_numeric(df['product_id'])
    df['code'] = pd.to_numeric(df['code'], errors='coerce')
    df['weight_netto'] = pd.to_numeric(df['weight_netto'], errors='coerce')
    df['weight_brutto'] = pd.to_numeric(df['weight_brutto'], errors='coerce')
    df['box_quant'] = pd.to_numeric(df['box_quant'], errors='coerce')
    df['measure_code'] = pd.to_numeric(df['measure_code'], errors='coerce')
    df['order_no'] = pd.to_numeric(df['order_no'], errors='coerce')
    df['barcodes'] = pd.to_numeric(df['barcodes'], errors='coerce')

    # keraksiz ustunlarni drop qildim
    df = df.drop(columns=[
        'litr', 
        'producer_code', 
        'article_code', 
        'gtin', 'ikpu', 
        'tnved', 
        'marking_group_code'
        ]
    )

    # df ichidagi nestedlarni alohida listga olaman
    # GROUP ustuni
    rows = []
    for _, row in df.iterrows():
        for g in row['groups']:
            rows.append({
                'product_id': row['product_id'],
                'group_id': g.get('group_id'),
                'group_code': g.get('group_code'),
                'type_id': g.get('type_id'),
                'type_code': g.get('type_code')
            })

    prod_group_df = pd.json_normalize(rows)

    prod_group_df.dtypes

    prod_group_df['group_id'] = pd.to_numeric(prod_group_df['group_id'])
    prod_group_df['group_code'] = pd.to_numeric(prod_group_df['group_code'], errors='coerce')
    prod_group_df['type_id'] = pd.to_numeric(prod_group_df['type_id'], errors='coerce')


    prod_group_df.to_csv('group.csv', index=False)


    # INVENTORY_KINDS

    inv_kinds = []

    for _, i in df.iterrows():
        for k in i['inventory_kinds']:
            inv_kinds.append({
                'product_id': i['product_id'],
                'inventory_kind': k.get('inventory_kind')
            })

    inv_kinds_df = pd.json_normalize(inv_kinds)
    inv_kinds_df.dtypes

    inv_kinds_df.to_csv('inventory_kinds.csv', index=False)

    # SECTOR_CODES
    sector_codes = []

    for _, s in df.iterrows():
        for k in s['sector_codes']:
            sector_codes.append({
                'product_id': s['product_id'],
                'sector_code': k.get('sector_code')
            })


    sector_codes_df = pd.json_normalize(sector_codes)
    sector_codes_df.dtypes

    sector_codes_df.to_csv('sector_codes.csv', index=False)


    # df dagi nested ustunlarni drop qilaman

    df = df.drop(columns= [
        'groups',
        'inventory_kinds',
        'sector_codes'
    ])



    ## LOAD 
    print("Databasega yuklash boshlanyapti...")

    loader(df, 'products')




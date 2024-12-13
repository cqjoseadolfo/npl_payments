import pandas as pd
from datetime import datetime
from querys import get_cuenta_npl
from load import export_dataframe_to_sql
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

current_month_year = datetime.now().strftime("%m.%Y")
source = "payments.xlsx"

df = pd.read_excel(source, sheet_name=current_month_year, header=0, usecols="A,D,E,G,H,J", dtype={'DNI': str})
df = df.dropna(how='all', axis=1).dropna(how='all').reset_index(drop=True)
df.columns = ['FECHA', 'PAGO', 'BANCO', 'CONTRATO', 'DNI', 'CARTERA']
df = df[df['DNI'].str.strip("0") != ""]
df['CONTRATO'] = df['CONTRATO'].apply(lambda x: '{:.0f}'.format(x) if pd.notnull(x) else x)
df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%Y', errors='coerce')
df['PAGO'] = df['PAGO'].round(2)

df['CONTRATO'] = df['CONTRATO'].str.strip()
df['CONTRATO'] = df['CONTRATO'].apply(lambda x: x.zfill(10))
df['DNI'] = df['DNI'].apply(lambda x: x.zfill(8))

df['CUENTA'] = df['CONTRATO'].apply(lambda contrato: get_cuenta_npl(contrato))

export_dataframe_to_sql(df, "NPL_PAYMENTS", schema='cargue')

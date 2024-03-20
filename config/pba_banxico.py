from sie_banxico import SIEBanxico
import pandas as pd

# Reemplaza 'tu_token_aquí' con tu token real
api = SIEBanxico("aa7703bda1c74716bc9ed546adf7c08905c7274e737e353d00668f8eec27e2b3", id_series=['SF311408', 'SF311418'], language='en')

# Obtiene el rango de series de tiempo
data = api.get_timeseries_range(init_date='2000-12-31', end_date='2004-04-01')

# Convierte los datos en un DataFrame de pandas
df = pd.DataFrame(data['bmx']['series'][0]['datos'])

# Imprime las primeras filas del DataFrame
print(df.head())

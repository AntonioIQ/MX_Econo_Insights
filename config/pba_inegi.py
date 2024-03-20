from INEGIpy import Indicadores
import pandas as pd

token = '10ed08d5-0be8-42a4-94b6-d0fd406ff710'
inegi = Indicadores(token)

# Reemplaza '6206972689' con el ID del indicador que deseas consultar
df = inegi.obtener_df(indicadores=['628194'], 
                      nombres=['INPC'], 
                      inicio='2022', 
                      fin='2022')

print(df.head())

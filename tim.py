import pandas as pd
from func import encrypt, fake_num

df_voz = pd.read_excel("input/TIM.xlsx", sheet_name="Extrato Voz", engine="openpyxl")
df_cgi = pd.read_excel("input/TIM.xlsx", sheet_name="Dados de Antena", engine="openpyxl")

for index, row in df_voz.iterrows():
    df_voz.at[index, "Nº ORIGEM"] = fake_num(str(row["Nº ORIGEM"]))
    df_voz.at[index, "Nº DESTINO"] = fake_num(str(row["Nº DESTINO"]))

colunas_desejadas = [
    "HORA BRASÍLIA",
    "Nº ORIGEM",
    "Nº DESTINO",
    "DURAÇÃO",
    "ESTADO",
    "CIDADE",
    "BAIRRO",
    "ENDEREÇO",
]

resultado = pd.merge(df_voz, df_cgi, left_on="PRIMEIRA CGI/ERB", right_on="CGI/ERB")

resultado = resultado[colunas_desejadas].dropna()

print(resultado)

resultado.to_csv("output/tim3.csv", index=False, sep=";")

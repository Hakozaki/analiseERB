import pandas as pd
from func import encrypt, fake_num

df = pd.read_excel("input/oi.xlsx", sheet_name="Planilha1", engine="openpyxl")
df["Nº ORIGEM"] = "68984175495"
df["Nº ORIGEM"] = fake_num("68984175495")

for index, row in df.iterrows():
    df.at[index, "Ligou para"] = fake_num(str(row["Ligou para"]))

colunas_desejadas = [
    "Data",
    "Hora",
    "Nº ORIGEM",
    "Ligou para",
    "Duração",
    "UF ERB",
    "Cidade ERB",
    "Bairro ERB",
    "Endereço ERB",
]

print(df[colunas_desejadas])

df[colunas_desejadas].to_csv("output/oi3.csv", index=False, sep=";")

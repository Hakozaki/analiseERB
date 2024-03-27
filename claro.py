import pandas as pd
import re

import func

df = pd.read_excel("input/claro.xlsx")

df["Data Início"] = (
    df["Data Início"].astype(str).str[0:4]
    + "-"
    + df["Data Início"].astype(str).str[4:6]
    + "-"
    + df["Data Início"].astype(str).str[6:8]
)
df["Hora Início"] = (
    df["Hora Início"].astype(str).str[0:2]
    + ":"
    + df["Hora Início"].astype(str).str[2:4]
    + ":"
    + df["Hora Início"].astype(str).str[4:6]
)

colunas_desejadas = [
    "Número A",
    "Número B",
    "Data Início",
    "Hora Início",
    "Duração",
    "Município ERB RE",
    "Endereço ERB RE",
]
df = df[colunas_desejadas].dropna()

for index, row in df.iterrows():
    df.at[index, "Número A"] = func.fake_num(str(row["Número A"]))
    df.at[index, "Número B"] = func.fake_num(str(row["Número B"]))    

print(df)
df[colunas_desejadas].to_csv("output/claro4.csv", index=False, sep=";")

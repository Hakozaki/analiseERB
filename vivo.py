import pandas as pd
from datetime import datetime
from func import encrypt, fake_num

# from google.colab import drive
df = pd.read_excel(
    "input/vivo.xlsx", sheet_name="erb", engine="openpyxl"
)
df2 = pd.read_excel(
    "input/vivo.xlsx", sheet_name="chamadas", engine="openpyxl"
)
# conversão de data
df2["Data"] = pd.to_datetime(df2["Data"], format="%d/%m/%Y")
df2["Data"] = df2["Data"].dt.strftime("%Y-%m-%d")

# adicionei filtro de colunas na tabela da bilhetagem
# remove os valores NaN e adiciona valores da coluna local destino no local origem e vice-versa
df2["Local Origem"] = df2["Local Origem"].fillna(df2["Local Destino"])
df2["Local Destino"] = df2["Local Destino"].fillna(df2["Local Origem"])
df2 = df2.rename(columns={"Local Origem": "CGI"})
colunas_desejadas = [
    "Data",
    "Hora",
    "Chamador",
    "Chamado",
    "Hora desc",
    "Durac",
    "Status",
    "CGI",
]
df_filtro = df2[colunas_desejadas]

# adicionei filtro de colunas na tabela de endereços
df["ERB COMPLETA"] = (
    df[["CCC", "ERB", "Set"]].astype(str).apply(lambda x: " ".join(x), axis=1)
)
colunas_desejadas2 = ["CGI", "ERB COMPLETA", "UF", "Cidade", "Bairro", "Endereço"]
df_filtro2 = df[colunas_desejadas2]

# datas_pesquisa = ['14/09/2017','21/11/2018']
Datas_pesquisa = ["2018-10-22", "2018-10-23", "2018-10-24", "2018-10-25", "2018-10-26"]
resultado1 = df_filtro[df_filtro["Data"].isin(Datas_pesquisa)]
resultado2 = pd.merge(resultado1, df_filtro2, on="CGI")

# salvando o excel com nome do arquivo
# resultado2.to_excel("75420319912018-22-10a26-10.xlsx", index=False)
for index, row in resultado2.iterrows():
    resultado2.at[index, "Chamador"] = fake_num(str(row["Chamador"]))
    resultado2.at[index, "Chamado"] = fake_num(str(row["Chamado"]))
    
resultado2.to_csv("output/vivo_res2.csv", index=False, sep=";")

# Para datas posteriores a 03/10/2017
Datas_pesquisa = ["2017-12-04", "2017-12-05", "2017-12-06", "2017-12-07", "2017-12-08"]
resultado3 = df_filtro[df_filtro["Data"].isin(Datas_pesquisa)]
resultado4 = pd.merge(
    resultado3, df_filtro2, left_on="CGI", right_on="ERB COMPLETA", how="left"
)

for index, row in resultado4.iterrows():
    resultado4.at[index, "Chamador"] = fake_num(str(row["Chamador"]))
    resultado4.at[index, "Chamado"] = fake_num(str(row["Chamado"]))
# resultado4.to_excel('75420322632017-22-09a30-09.xlsx', index=False)
resultado4.to_csv("output/vivo_res4.csv", index=False, sep=";")

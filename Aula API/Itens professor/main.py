import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import busca_cep as bc




filename = "cbaconquer-f99c87df3d96.json"

scopes = [
"https://spreadsheets.google.com/feeds",
"https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename = filename,
    scopes = scopes
)

client = gspread.authorize(creds)
print(client)


# Ver os dados da planilha
planilha = client.open(
    title = "Projeto",
    folder_id = "1wmgtq30xHcytuM101aRJ6L8kV0UAxr-2"
)

planilha = planilha.get_worksheet_by_id(0)

dados = planilha.get_all_records()

df= pd.DataFrame(dados)
print(df)

# Manipular via API
# nova_linha = ["Geladeira", "2800", "Julia", "30525500"]

#Inserir - Create
# planilha.insert_row(nova_linha, index = 3)

# Deletar
#planilha.delete_rows(2)

#update
# planilha.update_cell(
#     row=3,
#     col= 3,
#     value = "Iago"
# )

# planilha.update_acell(
#     label = "B4",
#     value = "5000"
# )

df["Rua"] = df["Cep"].apply(bc.rua)
df["Estado"] = df["Cep"].apply(bc.estado)
df["Cidade"] = df["Cep"].apply(bc.cidade)
 
# Atualizar o cabeçalho
planilha.update("A1", [df.columns.tolist()])
 
#Atualizar os valores
planilha.update(df.values.tolist(),"A2")








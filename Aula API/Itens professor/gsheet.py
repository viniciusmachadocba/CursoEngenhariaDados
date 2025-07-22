import gspread
from oauth2client.service_account import ServiceAccountCredentials





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
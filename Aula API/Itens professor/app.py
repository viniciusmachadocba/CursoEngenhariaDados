import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import busca_cep as bc
import streamlit as st

st.set_page_config(page_title = "CRUD com Google Sheets", layout = "centered")

st.title("CRUD com Google Sheets + Enriquecimento de CEP")

@st.cache_resource

def conectar_planilha():
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
        ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename = "cbaconquer-f99c87df3d96.json",
    scopes = scopes
    )

    client = gspread.authorize(creds)
    planilha = client.open(
    title = "Projeto",
    folder_id = "1wmgtq30xHcytuM101aRJ6L8kV0UAxr-2"
    )   
    
    return planilha.get_worksheet_by_id(0)

    
planilha = conectar_planilha()

def atualizar_df_da_planilha():
    st.session_state.df = pd.DataFrame(planilha.get_all_records())


#se for a primeira vez executando, carregar os dados da planilha

if "df" not in st.session_state:
    atualizar_df_da_planilha()

df = st.session_state.df
    
# Criar subtitulo e os dados da planilha
st.subheader("⚙️ Planilha Atual")
st.dataframe(df)

#Criar formulario  para adicionar uma nova linha
st.subheader("➕ Adicionar nova linha")

with st.form("adicionar_linha"):
    #campos de entrada para o user preencher
    produto = st.text_input("Produto")
    preco = st.text_input("Preço")
    cliente = st.text_input("Cliente")
    cep = st.text_input("CEP")

    submitted = st.form_submit_button("Adicionar")

    if submitted:
        #Crio a nova linha e coloco na lista
        nova_linha = [produto, preco, cliente, cep]

        # Adcionar a linha na planilha final
        planilha.append_row(nova_linha)

        #Mostrar mensagem de sucesso
        st.success("Linha adicionada com sucesso!")

        #atualizar df
        atualizar_df_da_planilha()

        #atualizar a tela
        st.rerun()




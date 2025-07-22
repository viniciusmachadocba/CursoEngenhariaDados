import streamlit as st
import pandas as pd
from Cepbuscas import GetInfoCep

# Configuração da página
st.set_page_config(
    'Informacoes CEP',
    layout='wide'
)

# Título
st.title('Informações do CEP')

# Entrada do usuário
meu_cep = st.text_input('Digite o seu CEP')

# Função com cache para obter dados do CEP
@st.cache_data
def get_info_cep(cep):
    return GetInfoCep(cep=cep)

# Execução principal
if meu_cep:
    try:
        meu_cep_info = get_info_cep(meu_cep)

        match_type = st.radio(
            'Escolha qual informação deseja trazer',
            ['Rua', 'Bairro', 'Cidade', 'Estado', 'Todas']
        )

        if st.button("Buscar"):
            if match_type == 'Rua':
                st.write(meu_cep_info.get_rua())
            elif match_type == 'Bairro':
                st.write(meu_cep_info.get_bairro())
            elif match_type == 'Cidade':
                st.write(meu_cep_info.get_cidade())
            elif match_type == 'Estado':
                st.write(meu_cep_info.get_estado())
            else:  # Todas
                df = pd.DataFrame.from_dict(meu_cep_info.get_tudo(), 
                                            orient='index')
                df.rename(columns={0: 'Informações'}, inplace=True)
                st.dataframe(df)

    except Exception as e:
        st.error(f"Erro ao buscar informações para o CEP '{meu_cep}': {e}")

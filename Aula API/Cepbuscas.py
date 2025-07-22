import requests
import json
import re


class GetInfoCep:

    """Class to get CEP info
    """
    def __init__(self, cep:str) -> None:
        
        self.cep = self._limpa_cep(cep=str(cep))
        self._resposta = self._requisicao()
        self.__json = self._resposta.json()

    def _limpa_cep(self,cep) ->str:
        return str(re.sub(r'\D',"", cep))
    
    def _requisicao(self) -> requests.Response | None:
        url = f"https://brasilapi.com.br/api/cep/v1/{self.cep}"

        try:
            temp_resposta = requests.get(url)
        
        except Exception as e:
            raise f"Erro na requisicao\n {e}"
        
        if temp_resposta.status_code == 200 :
            return temp_resposta

        else:
            print(temp_resposta.status_code)
            print(temp_resposta.reason)

    def get_rua(self):
        # print(f'{self.__json.get('street', '')}')
        return self.__json.get('street', 'Not found')   
    
    def get_cidade(self):
        # print(f'{self.__json.get('city', '')}')
        return self.__json.get('city', 'Not found')
    
    def get_estado(self):
        # print(f'{self.__json.get('state', '')}')
        return self.__json.get('state', 'Not found')
    
    def get_bairro(self):
        return self.__json.get('neighborhood','Not found')
    
    def get_tudo(self):
        # print(f'{self.__json}')
        return self.__json

if __name__ == "__main__":
    cepinfo = GetInfoCep('04571-000')
    cepinfo.get_rua()
    cepinfo.get_cidade()
    cepinfo.get_estado()
    cepinfo.get_tudo()

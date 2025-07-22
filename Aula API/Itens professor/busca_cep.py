
import requests

def buscar_rua(cep):
   try:
        cep = str(cep).replace("-", "").strip()  
        url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
        response = requests.get(url)  
        if response.status_code == 200:
            return response.json().get("street", "")
   except:
       return ""
   
def buscar_estado(cep):
    try:
            cep = str(cep).replace("-", "").strip()  
            url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
            response = requests.get(url)  
            if response.status_code == 200:
                return response.json().get("state", "")
    except:
        return ""
    
def buscar_cidade(cep):
    try:
            cep = str(cep).replace("-", "").strip()  
            url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
            response = requests.get(url)  
            if response.status_code == 200:
                return response.json().get("city", "")
    except:
        return ""
   


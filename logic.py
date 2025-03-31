import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("A chave de API não foi encontrada. Defina-a no arquivo '.env'.")

# Endpoint da API do Gemini
endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json"
}

def obter_resposta_do_gemini(historico_conversa):
    """
    Envia o histórico da conversa para a API do Gemini e retorna a resposta gerada.

    Parâmetros:
    - historico_conversa (list): Lista de mensagens trocadas na conversa.

    Retorna:
    - str: Resposta gerada pelo modelo ou mensagem de erro.
    """
    data = {
        "contents": historico_conversa,
        "generation_config": {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
            "max_output_tokens": 256
        }
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    else:
        return f"Erro: {response.status_code} - {response.text}"

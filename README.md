# GeminiAI

Projeto de IA feito por alunos da faculdade SATC

## Estrutura do Projeto

- `gui.py`: Interface gráfica utilizando Tkinter.
- `history.py`: Gerenciamento do histórico de conversas.
- `logic.py`: Lógica para interação com a API Gemini.
- `main.py`: Ponto de entrada principal do aplicativo.
- `props.py`: Definições de constantes e configurações.
- `.env.example`: Exemplo de configuração de variáveis de ambiente.
- `requirements.txt`: Lista de dependências do projeto.

## Configuração

1. Clone o repositório:&#8203;:contentReference[oaicite:37]{index=37}
   ```bash
   git clone https://github.com/GabrielMacielZavarize/API-IA.git

2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt

5. Configure as variáveis de ambiente: Renomeie o arquivo .env.example para .env:
    ```bash
    mv .env.example .env

    Edite o arquivo .env e insira sua chave da API no campo correspondente:
    GEMINI_API_KEY=sua_chave_aqui

6. Execute o aplicativo:
    ```bash
    python main.py

Contribuição:
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
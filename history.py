class HistoricoConversa:
    """
    Classe para gerenciar o histórico da conversa.
    """

    def __init__(self):
        self.historico = []

    def adicionar_mensagem_usuario(self, mensagem):
        """
        Adiciona a mensagem do usuário ao histórico.
        """
        self.historico.append({"role": "user", "parts": [{"text": mensagem}]})

    def adicionar_resposta_modelo(self, resposta):
        """
        Adiciona a resposta do modelo ao histórico (garçonete).
        """
        self.historico.append({"role": "model", "parts": [{"text": resposta}]})

    def adicionar_prompt_inicial(self, prompt):
        """
        Adiciona um prompt inicial (oculto ao usuário),
        para orientar o comportamento do modelo.
        """
        # Armazenamos como se fosse mensagem de "user" para a API,
        # pois a API do Gemini não suporta 'system' role. Mas NÃO exibimos no chat.
        self.historico.insert(0, {"role": "user", "parts": [{"text": prompt}]})

    def obter_historico(self):
        """
        Retorna o histórico completo da conversa.
        """
        return self.historico
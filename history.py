class HistoricoConversa:
    """
    Classe para gerenciar o histórico da conversa.
    """

    def __init__(self):
        self.historico = []

    def adicionar_mensagem_usuario(self, mensagem):
        """
        Adiciona a mensagem do usuário ao histórico.

        Parâmetros:
        - mensagem (str): Mensagem enviada pelo usuário.
        """
        self.historico.append({"role": "user", "parts": [{"text": mensagem}]})

    def adicionar_resposta_modelo(self, resposta):
        """
        Adiciona a resposta do modelo ao histórico.

        Parâmetros:
        - resposta (str): Resposta gerada pelo modelo.
        """
        self.historico.append({"role": "model", "parts": [{"text": resposta}]})

    def obter_historico(self):
        """
        Retorna o histórico completo da conversa.

        Retorna:
        - list: Lista de mensagens no histórico.
        """
        return self.historico
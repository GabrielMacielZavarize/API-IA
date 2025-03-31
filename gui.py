import tkinter as tk
from tkinter import scrolledtext

class ChatbotGUI:
    """
    Classe para criar a interface gráfica do chatbot utilizando Tkinter.
    """

    def __init__(self, root, enviar_mensagem_callback):
        """
        Inicializa a interface gráfica.

        Parâmetros:
        - root: Janela principal do Tkinter.
        - enviar_mensagem_callback (func): Função chamada ao enviar uma mensagem.
        """
        self.root = root
        self.root.title("Chatbot do Restaurante")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.mensagem_entry = tk.Entry(root, width=50)
        self.mensagem_entry.grid(row=1, column=0, padx=10, pady=10)
        self.mensagem_entry.bind("<Return>", self._enviar_mensagem_evento)

        self.enviar_button = tk.Button(root, text="Enviar", command=self._enviar_mensagem)
        self.enviar_button.grid(row=1, column=1, padx=10, pady=10)

        self.enviar_mensagem_callback = enviar_mensagem_callback

    def _enviar_mensagem_evento(self, event):
        """
        Manipula o evento de pressionar Enter no campo de entrada.

        Parâmetros:
        - event: Evento do Tkinter.
        """
        self._enviar_mensagem()

    def _enviar_mensagem(self):
        """
        Obtém a mensagem do usuário e chama a função de callback.
        """
        mensagem = self.mensagem_entry.get()
        if mensagem.strip():
            self.mensagem_entry.delete(0, tk.END)
            self.enviar_mensagem_callback(mensagem)

    def exibir_mensagem(self, remetente, mensagem):
        """
        Exibe uma mensagem na área de chat.

        Parâmetros:
        - remetente (str): Nome do remetente da mensagem.
        - mensagem (str): Conteúdo da mensagem.
        """
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{remetente}: {mensagem}\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')
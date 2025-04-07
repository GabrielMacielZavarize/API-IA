import tkinter as tk
from tkinter import scrolledtext, font

class ChatbotGUI:
    """
    Classe para criar uma interface gráfica mais bonita para o chatbot utilizando Tkinter.
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
        self.root.geometry("700x500")  # Define o tamanho da janela
        self.root.configure(bg="#f0f0f0")  # Define uma cor de fundo suave

        # Define uma fonte personalizada para os textos
        self.custom_font = font.Font(family="Helvetica", size=12)

        # Cria um título para a aplicação com uma cor de fundo destacada
        self.title_label = tk.Label(
            root, 
            text="Chatbot do Restaurante", 
            bg="#4a7a8c", 
            fg="white", 
            font=("Helvetica", 16, "bold"), 
            pady=10
        )
        self.title_label.pack(fill=tk.X)

        # Cria a área de chat com uma scrolledtext para exibir as mensagens
        self.chat_area = scrolledtext.ScrolledText(
            root, 
            wrap=tk.WORD, 
            width=80, 
            height=20, 
            state='disabled', 
            font=self.custom_font, 
            bg="white", 
            fg="black", 
            padx=10, 
            pady=10
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Configurar tags para cores diferentes
        self.chat_area.tag_config("cliente", foreground="black")
        self.chat_area.tag_config("garconete", foreground="blue")

        # Cria um frame para agrupar o campo de entrada e o botão de enviar
        self.entry_frame = tk.Frame(root, bg="#f0f0f0")
        self.entry_frame.pack(fill=tk.X, padx=10, pady=10)

        # Campo de entrada para a mensagem do usuário
        self.mensagem_entry = tk.Entry(
            self.entry_frame, 
            font=self.custom_font, 
            width=60
        )
        self.mensagem_entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)
        self.mensagem_entry.bind("<Return>", self._enviar_mensagem_evento)

        # Botão para enviar a mensagem
        self.enviar_button = tk.Button(
            self.entry_frame, 
            text="Enviar", 
            font=self.custom_font, 
            bg="#4a7a8c", 
            fg="white", 
            command=self._enviar_mensagem
        )
        self.enviar_button.pack(side=tk.RIGHT)

        self.enviar_mensagem_callback = enviar_mensagem_callback

    def _enviar_mensagem_evento(self, event):
        """
        Manipula o evento de pressionar Enter no campo de entrada.
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
        Exibe uma mensagem na área de chat, diferenciando o remetente por cor.
        """
        self.chat_area.config(state='normal')
        if remetente.lower() == "garçonete":
            self.chat_area.insert(tk.END, f"{remetente}: {mensagem}\n\n", "garconete")
        else:
            self.chat_area.insert(tk.END, f"{remetente}: {mensagem}\n\n", "cliente")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')
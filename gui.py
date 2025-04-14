import tkinter as tk
from tkinter import ttk

class ChatBubble(tk.Frame):
    """
    Widget que simula um balão de mensagem, com rótulo indicando quem enviou (Cliente ou Garçonete).
    """
    def __init__(self, parent, remetente, message, is_user=True, **kwargs):
        super().__init__(parent, **kwargs)

        # Define cores e alinhamento de acordo com o remetente
        if is_user:
            bg_color = "#DCF8C6"  # Balão verde claro para o Cliente
            anchor = "w"         # Alinha à esquerda
        else:
            bg_color = "#ADD8E6"  # Balão azul claro para a Garçonete
            anchor = "e"         # Alinha à direita

        # Rótulo com o nome do remetente (ex: "Cliente" ou "Garçonete")
        self.remetente_label = tk.Label(
            self,
            text=remetente,
            font=("Helvetica", 9, "bold"),
            fg="gray",
            bg=self["bg"] if "bg" in self.keys() else "#f0f0f0"
        )
        self.remetente_label.pack(side=tk.TOP, anchor=anchor, padx=5)

        # Label que contém o texto da mensagem (o balão)
        self.label = tk.Label(
            self,
            text=message,
            bg=bg_color,
            wraplength=400,
            justify="left",
            font=("Helvetica", 12),
            padx=10,
            pady=5,
            bd=2,
            relief="ridge"
        )
        self.label.pack(side=tk.TOP, anchor=anchor, padx=5)

class ChatFrame(tk.Frame):
    """
    Área de chat rolável, que contém os balões de mensagem.
    """
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(bg="#f0f0f0")

        # Canvas para permitir a rolagem
        self.canvas = tk.Canvas(self, borderwidth=0, background="#f0f0f0")
        self.frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((4, 4), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

    def _on_frame_configure(self, event):
        """Atualiza a área rolável conforme o tamanho do frame interno."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        """Ajusta a largura do frame interno para acompanhar a largura do canvas."""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def add_message(self, remetente, message, is_user=True):
        """
        Adiciona um balão de mensagem à área de chat.
        
        Parâmetros:
            remetente (str): "Cliente" ou "Garçonete".
            message (str): Texto da mensagem.
            is_user (bool): True para mensagem do Cliente (alinhada à esquerda), False para
                            mensagem da Garçonete (alinhada à direita).
        """
        container = tk.Frame(self.frame, bg="#f0f0f0")
        # Alinha o container com base em is_user
        if is_user:
            container.pack(anchor="w", fill="x", pady=5)
        else:
            container.pack(anchor="e", fill="x", pady=5)

        bubble = ChatBubble(container, remetente, message, is_user=is_user, bg="#f0f0f0")
        # Posiciona o balão dentro do container com padding lateral
        if is_user:
            bubble.pack(side="left", padx=(10, 50))
        else:
            bubble.pack(side="right", padx=(50, 10))

class ChatbotGUI:
    """
    Interface gráfica para o chatbot com balões de mensagem ao estilo WhatsApp.
    As mensagens do Cliente ficam alinhadas à esquerda e as da Garçonete à direita,
    cada uma com um rótulo indicando o remetente.
    """
    def __init__(self, root, enviar_mensagem_callback):
        self.root = root
        self.root.title("Chatbot do Restaurante")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill="both", expand=True)

        # Título da aplicação
        self.title_label = ttk.Label(
            self.main_frame,
            text="Chatbot do Restaurante",
            background="#4a7a8c",
            foreground="white",
            font=("Helvetica", 18, "bold"),
            anchor="center"
        )
        self.title_label.pack(fill="x", pady=(0, 10))

        # Área de chat
        self.chat_frame = ChatFrame(self.main_frame, bg="#f0f0f0")
        self.chat_frame.pack(fill="both", expand=True)

        # Frame para entrada de mensagem e botão de envio
        self.entry_frame = ttk.Frame(self.main_frame)
        self.entry_frame.pack(fill="x", pady=(10, 0))

        self.mensagem_entry = ttk.Entry(self.entry_frame, font=("Helvetica", 12))
        self.mensagem_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.mensagem_entry.bind("<Return>", self._enviar_mensagem_evento)

        self.enviar_button = ttk.Button(self.entry_frame, text="Enviar", command=self._enviar_mensagem)
        self.enviar_button.pack(side="right")

        self.enviar_mensagem_callback = enviar_mensagem_callback

    def _enviar_mensagem_evento(self, event):
        self._enviar_mensagem()

    def _enviar_mensagem(self):
        mensagem = self.mensagem_entry.get()
        if mensagem.strip():
            self.mensagem_entry.delete(0, tk.END)
            self.enviar_mensagem_callback(mensagem)

    def exibir_mensagem(self, remetente, mensagem):
        """
        Exibe um balão de mensagem na área de chat com rótulo identificando o remetente.
        Se o remetente for "Garçonete", a mensagem é alinhada à direita; se for "Cliente", à esquerda.
        """
        if remetente.lower() == "cliente":
            is_user = True
        elif remetente.lower() == "garçonete":
            is_user = False
        else:
            is_user = True  # Default para mensagens não classificadas

        self.chat_frame.add_message(remetente, mensagem, is_user=is_user)
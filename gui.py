import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class ChatBubble(tk.Frame):
    """
    Widget que simula um balão de mensagem, com rótulo indicando quem enviou (Cliente ou Garçonete).
    """
    def __init__(self, parent, remetente, message, is_user=True, **kwargs):
        super().__init__(parent, **kwargs)

        # Define cores e alinhamento de acordo com o remetente
        if is_user:
            bg_color = "#DCF8C6"  # Verde claro do WhatsApp para o Cliente
            anchor = "w"
        else:
            bg_color = "#FFFFFF"  # Branco para a Garçonete
            anchor = "e"

        # Rótulo com o nome do remetente
        self.remetente_label = tk.Label(
            self,
            text=remetente,
            font=("Segoe UI", 14, "bold"),
            fg="#075E54",  # Verde escuro do WhatsApp
            bg=self["bg"] if "bg" in self.keys() else "#F0F2F5"  # Cinza claro do WhatsApp
        )
        self.remetente_label.pack(side=tk.TOP, anchor=anchor, padx=5)

        # Label que contém o texto da mensagem
        self.label = tk.Label(
            self,
            text=message,
            bg=bg_color,
            wraplength=800,  # Aumentado para mais texto
            justify="left",
            font=("Segoe UI", 16),  # Fonte maior
            padx=20,
            pady=15,
            bd=0,
            relief="flat"
        )
        self.label.pack(side=tk.TOP, anchor=anchor, padx=5)

class ChatFrame(tk.Frame):
    """
    Área de chat rolável, que contém os balões de mensagem.
    """
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(bg="#F0F2F5")  # Fundo cinza claro do WhatsApp

        # Canvas para permitir a rolagem
        self.canvas = tk.Canvas(self, borderwidth=0, background="#F0F2F5", highlightthickness=0)
        self.frame = tk.Frame(self.canvas, bg="#F0F2F5")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((4, 4), window=self.frame, anchor="nw")

        # Configurar eventos de scroll
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

        self.frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta < 0:  # scroll down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:  # scroll up
            self.canvas.yview_scroll(-1, "units")

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
        container = tk.Frame(self.frame, bg="#F0F2F5")
        # Alinha o container com base em is_user
        if is_user:
            container.pack(anchor="w", fill="x", pady=10)
        else:
            container.pack(anchor="e", fill="x", pady=10)

        bubble = ChatBubble(container, remetente, message, is_user=is_user, bg="#F0F2F5")
        # Posiciona o balão dentro do container com padding lateral
        if is_user:
            bubble.pack(side="left", padx=(20, 100))
        else:
            bubble.pack(side="right", padx=(100, 20))

class ChatbotGUI:
    """
    Interface gráfica para o chatbot com balões de mensagem ao estilo WhatsApp.
    As mensagens do Cliente ficam alinhadas à esquerda e as da Garçonete à direita,
    cada uma com um rótulo indicando o remetente.
    """
    def __init__(self, root, enviar_mensagem_callback):
        self.root = root
        self.root.title("BigFood - Chatbot")
        self.root.geometry("1400x900")
        self.root.configure(bg="#F0F2F5")

        # Configurar estilo
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#F0F2F5")
        
        # Configurar estilo do botão
        style.configure("Custom.TButton",
                       font=("Segoe UI", 16, "bold"),
                       padding=(25, 15),
                       background="#128C7E",
                       foreground="white")
        
        # Configurar estilo do campo de entrada
        style.configure("Custom.TEntry",
                       font=("Segoe UI", 16),
                       padding=15)

        # Frame principal
        self.main_frame = ttk.Frame(root, style="Custom.TFrame", padding="30")
        self.main_frame.pack(fill="both", expand=True)

        # Cabeçalho
        header_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        header_frame.pack(fill="x", pady=(0, 30))

        # Container centralizado para título
        title_container = ttk.Frame(header_frame, style="Custom.TFrame")
        title_container.pack(expand=True, fill="x")

        # Frame para título
        title_frame = ttk.Frame(title_container, style="Custom.TFrame")
        title_frame.pack(expand=True)

        # Título principal com separador
        title_text = "BigFood - Assistente Virtual"
        self.title_label = ttk.Label(
            title_frame,
            text=title_text,
            font=("Segoe UI", 32, "bold"),
            foreground="#075E54",
            background="#F0F2F5"
        )
        self.title_label.pack()

        # Área de chat com borda suave
        chat_container = ttk.Frame(self.main_frame, style="Custom.TFrame")
        chat_container.pack(fill="both", expand=True, pady=(0, 20))
        
        self.chat_frame = ChatFrame(chat_container)
        self.chat_frame.pack(fill="both", expand=True)

        # Frame para entrada de mensagem com sombra
        self.entry_frame = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.entry_frame.pack(fill="x", pady=(20, 0))

        # Container para entrada e botão
        input_container = ttk.Frame(self.entry_frame, style="Custom.TFrame")
        input_container.pack(fill="x", expand=True)

        # Campo de entrada com estilo moderno
        self.mensagem_entry = ttk.Entry(
            input_container,
            font=("Segoe UI", 16),
            style="Custom.TEntry"
        )
        self.mensagem_entry.pack(side="left", fill="x", expand=True, padx=(0, 15))
        self.mensagem_entry.bind("<Return>", self._enviar_mensagem_evento)

        # Botão de enviar com estilo moderno
        self.enviar_button = tk.Button(
            input_container,
            text="Enviar",
            font=("Segoe UI", 16, "bold"),
            bg="#128C7E",
            fg="white",
            padx=25,
            pady=0,
            relief="flat",
            command=self._enviar_mensagem,
            height=1
        )
        self.enviar_button.pack(side="right", fill="y")

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
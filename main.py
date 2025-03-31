import tkinter as tk
from gui import ChatbotGUI
from history import HistoricoConversa
from logic import obter_resposta_do_gemini
from propts import INSTRUCAO_INICIAL

def main():
    # Inicializa o histórico da conversa
    historico = HistoricoConversa()

    def enviar_mensagem(mensagem):
        # Adiciona a mensagem do usuário ao histórico
        historico.adicionar_mensagem_usuario(mensagem)
        # Obtém a resposta do modelo com base no histórico
        resposta = obter_resposta_do_gemini(historico.obter_historico())
        # Adiciona a resposta do modelo ao histórico
        historico.adicionar_resposta_modelo(resposta)
        # Exibe a mensagem do usuário e a resposta na interface gráfica
        gui.exibir_mensagem("Cliente", mensagem)
        gui.exibir_mensagem("Garçonete", resposta)

    # Cria a janela principal do Tkinter
    root = tk.Tk()
    # Inicializa a interface gráfica do chatbot
    gui = ChatbotGUI(root, enviar_mensagem)
    # Exibe a instrução inicial na interface
    gui.exibir_mensagem("Garçonete", INSTRUCAO_INICIAL)
    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
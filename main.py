import tkinter as tk
from gui import ChatbotGUI
from history import HistoricoConversa
from logic import obter_resposta_do_gemini
from propts import (
    PROMPT_GARCONETE,
    PROMPT_CATEGORIAS,
    PROMPT_LANCHES,
    PROMPT_COMBOS,
    PROMPT_ACOMPANHAMENTOS,
    PROMPT_BEBIDAS,
    PROMPT_SOBREMESAS,
    PROMPT_PROMOCOES,
    PROMPT_ENTREGA,
    PROMPT_PAGAMENTO
)

def main():
    # Inicializa o histórico da conversa
    historico = HistoricoConversa()
    
    # Concatena os prompts em uma única string
    prompt_inicial = (
        PROMPT_GARCONETE + "\n\n" +
        PROMPT_CATEGORIAS + "\n\n" +
        PROMPT_LANCHES + "\n\n" +
        PROMPT_COMBOS + "\n\n" +
        PROMPT_ACOMPANHAMENTOS + "\n\n" +
        PROMPT_BEBIDAS + "\n\n" +
        PROMPT_SOBREMESAS + "\n\n" +
        PROMPT_PROMOCOES + "\n\n" +
        PROMPT_ENTREGA + "\n\n" +
        PROMPT_PAGAMENTO
    )
    
    # Adiciona o prompt inicial (oculto)
    historico.adicionar_prompt_inicial(prompt_inicial)

    # Função que será chamada ao enviar uma mensagem
    def enviar_mensagem(mensagem):
        # 1. Adiciona a mensagem do usuário ao histórico
        historico.adicionar_mensagem_usuario(mensagem)
        # 2. Obtém a resposta do modelo com base no histórico
        resposta = obter_resposta_do_gemini(historico.obter_historico())
        # 3. Adiciona a resposta ao histórico
        historico.adicionar_resposta_modelo(resposta)
        # 4. Exibe a mensagem do usuário e a resposta na interface gráfica
        gui.exibir_mensagem("Cliente", mensagem)
        gui.exibir_mensagem("Garçonete", resposta)

    # Cria a janela principal do Tkinter
    root = tk.Tk()
    # Inicializa a interface gráfica do chatbot
    gui = ChatbotGUI(root, enviar_mensagem)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
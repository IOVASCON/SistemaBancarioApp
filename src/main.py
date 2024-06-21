import tkinter as tk
# Importa o módulo tkinter para criar interfaces gráficas

from ui.interface import BancoApp
# Importa a classe BancoApp do módulo interface no pacote ui

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente

    root = tk.Tk()
    # Cria a janela principal da interface gráfica

    app = BancoApp(root)
    # Cria uma instância da classe BancoApp, passando a janela principal como argumento

    root.mainloop()
    # Inicia o loop principal da interface gráfica, que aguarda por eventos (como cliques de botão)

import tkinter as tk
# Importa o módulo tkinter para criar interfaces gráficas
from tkinter import messagebox, simpledialog
# Importa messagebox e simpledialog do tkinter para exibir mensagens e caixas de diálogo
import sqlite3
# Importa o módulo sqlite3 para trabalhar com o banco de dados SQLite
from datetime import datetime
# Importa o módulo datetime para trabalhar com datas e horas

class BancoApp:
    # Define a classe BancoApp

    def __init__(self, root):
        # Método inicializador (construtor) da classe BancoApp
        self.root = root
        # Inicializa o atributo root com a raiz da interface gráfica
        self.root.title("Sistema Bancário")
        # Define o título da janela principal

        self.conn = sqlite3.connect('banco.db')
        # Conecta ao banco de dados SQLite (cria o banco se não existir)
        self.cursor = self.conn.cursor()
        # Cria um cursor para interagir com o banco de dados

        self.frame = tk.Frame(self.root)
        # Cria um frame dentro da janela principal
        self.frame.pack(pady=10)
        # Adiciona o frame à janela principal com um espaçamento vertical de 10 pixels

        self.label = tk.Label(self.frame, text="Bem-vindo ao Sistema Bancário", font=("Arial", 16))
        # Cria um rótulo (label) com o texto de boas-vindas e fonte Arial tamanho 16
        self.label.pack(pady=10)
        # Adiciona o rótulo ao frame com um espaçamento vertical de 10 pixels

        self.button_novo_usuario = tk.Button(self.frame, text="Novo Usuário", command=self.novo_usuario)
        # Cria um botão "Novo Usuário" que chama o método novo_usuario quando clicado
        self.button_novo_usuario.pack(pady=5)
        # Adiciona o botão ao frame com um espaçamento vertical de 5 pixels

        self.button_nova_conta = tk.Button(self.frame, text="Nova Conta", command=self.nova_conta)
        # Cria um botão "Nova Conta" que chama o método nova_conta quando clicado
        self.button_nova_conta.pack(pady=5)
        # Adiciona o botão ao frame com um espaçamento vertical de 5 pixels

        self.button_depositar = tk.Button(self.frame, text="Depositar", command=self.depositar)
        # Cria um botão "Depositar" que chama o método depositar quando clicado
        self.button_depositar.pack(pady=5)
        # Adiciona o botão ao frame com um espaçamento vertical de 5 pixels

        self.button_sacar = tk.Button(self.frame, text="Sacar", command=self.sacar)
        # Cria um botão "Sacar" que chama o método sacar quando clicado
        self.button_sacar.pack(pady=5)
        # Adiciona o botão ao frame com um espaçamento vertical de 5 pixels

        self.button_extrato = tk.Button(self.frame, text="Extrato", command=self.exibir_extrato)
        # Cria um botão "Extrato" que chama o método exibir_extrato quando clicado
        self.button_extrato.pack(pady=5)
        # Adiciona o botão ao frame com um espaçamento vertical de 5 pixels

        self.button_consultar_clientes = tk.Button(self.frame, text="Consultar Clientes", command=self.consultar_clientes)
        # Cria um botão "Consultar Clientes" que chama o método consultar_clientes quando clicado
        self.button_consultar_clientes.pack(pady=5)
        # Adiciona o botão ao frame com um espaçamento vertical de 5 pixels
    
    def novo_usuario(self):
        # Define o método novo_usuario para cadastrar um novo usuário
        nome = simpledialog.askstring("Novo Usuário", "Informe o nome completo:")
        # Abre uma caixa de diálogo para o usuário inserir o nome completo
        data_nascimento = simpledialog.askstring("Novo Usuário", "Informe a data de nascimento (dd-mm-aaaa):")
        # Abre uma caixa de diálogo para o usuário inserir a data de nascimento
        cpf = simpledialog.askstring("Novo Usuário", "Informe o CPF (somente número):")
        # Abre uma caixa de diálogo para o usuário inserir o CPF
        endereco = simpledialog.askstring("Novo Usuário", "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")
        # Abre uma caixa de diálogo para o usuário inserir o endereço

        if nome and data_nascimento and cpf and endereco:
            # Verifica se todos os campos foram preenchidos
            try:
                self.cursor.execute('''INSERT INTO clientes (nome, data_nascimento, cpf, endereco) 
                                       VALUES (?, ?, ?, ?)''', (nome, data_nascimento, cpf, endereco))
                # Insere os dados do novo usuário na tabela clientes do banco de dados
                self.conn.commit()
                # Confirma a transação no banco de dados
                messagebox.showinfo("Novo Usuário", "Usuário criado com sucesso!")
                # Exibe uma mensagem informando que o usuário foi criado com sucesso
            except sqlite3.IntegrityError:
                # Captura exceção de integridade (CPF duplicado)
                messagebox.showerror("Erro", "CPF já cadastrado.")
                # Exibe uma mensagem de erro informando que o CPF já está cadastrado
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            # Exibe uma mensagem de erro informando que todos os campos são obrigatórios
    
    def nova_conta(self):
        # Define o método nova_conta para criar uma nova conta
        cpf = simpledialog.askstring("Nova Conta", "Informe o CPF do cliente:")
        # Abre uma caixa de diálogo para o usuário inserir o CPF do cliente
        cliente = self.filtrar_usuario(cpf)
        # Chama o método filtrar_usuario para verificar se o cliente existe

        if cliente:
            # Verifica se o cliente foi encontrado
            self.cursor.execute('SELECT COUNT(*) FROM contas')
            # Conta o número de contas existentes
            numero_conta = self.cursor.fetchone()[0] + 1
            # Define o número da nova conta como o próximo número disponível
            agencia = simpledialog.askstring("Nova Conta", "Informe a agência:")
            # Abre uma caixa de diálogo para o usuário inserir a agência
            saldo_inicial = simpledialog.askfloat("Nova Conta", "Informe o saldo inicial:")
            # Abre uma caixa de diálogo para o usuário inserir o saldo inicial
            limite = simpledialog.askfloat("Nova Conta", "Informe o limite da conta corrente:")
            # Abre uma caixa de diálogo para o usuário inserir o limite da conta corrente
            limite_saques = simpledialog.askinteger("Nova Conta", "Informe o limite de saques:")
            # Abre uma caixa de diálogo para o usuário inserir o limite de saques

            if agencia and saldo_inicial is not None and limite is not None and limite_saques is not None:
                # Verifica se todos os campos foram preenchidos corretamente
                self.cursor.execute('''INSERT INTO contas (numero, agencia, saldo, limite, limite_saques, cliente_id)
                                       VALUES (?, ?, ?, ?, ?, ?)''', (numero_conta, agencia, saldo_inicial, limite, limite_saques, cliente[0]))
                # Insere os dados da nova conta na tabela contas do banco de dados
                self.conn.commit()
                # Confirma a transação no banco de dados
                messagebox.showinfo("Nova Conta", "Conta criada com sucesso!")
                # Exibe uma mensagem informando que a conta foi criada com sucesso
            else:
                messagebox.showerror("Erro", "Todos os campos da conta são obrigatórios.")
                # Exibe uma mensagem de erro informando que todos os campos da conta são obrigatórios
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")
            # Exibe uma mensagem de erro informando que o usuário não foi encontrado
    
    def depositar(self):
        # Define o método depositar para realizar um depósito
        numero_conta = simpledialog.askinteger("Depositar", "Informe o número da conta:")
        # Abre uma caixa de diálogo para o usuário inserir o número da conta
        valor = simpledialog.askfloat("Depositar", "Informe o valor do depósito:")
        # Abre uma caixa de diálogo para o usuário inserir o valor do depósito

        conta = self.filtrar_conta(numero_conta)
        # Chama o método filtrar_conta para verificar se a conta existe

        if conta:
            # Verifica se a conta foi encontrada
            novo_saldo = conta[3] + valor
            # Calcula o novo saldo após o depósito
            self.cursor.execute('''UPDATE contas SET saldo = ? WHERE id = ?''', (novo_saldo, conta[0]))
            # Atualiza o saldo da conta no banco de dados
            self.cursor.execute('''INSERT INTO transacoes (tipo, valor, data, conta_id)
                                   VALUES (?, ?, ?, ?)''', ("Depósito", valor, datetime.now().strftime("%d-%m-%Y %H:%M:%S"), conta[0]))
            # Insere uma nova transação de depósito na tabela transacoes do banco de dados
            self.conn.commit()
            # Confirma a transação no banco de dados
            messagebox.showinfo("Depositar", "Depósito realizado com sucesso!")
            # Exibe uma mensagem informando que o depósito foi realizado com sucesso
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
            # Exibe uma mensagem de erro informando que a conta não foi encontrada
    
    def sacar(self):
        # Define o método sacar para realizar um saque
        numero_conta = simpledialog.askinteger("Sacar", "Informe o número da conta:")
        # Abre uma caixa de diálogo para o usuário inserir o número da conta
        valor = simpledialog.askfloat("Sacar", "Informe o valor do saque:")
        # Abre uma caixa de diálogo para o usuário inserir o valor do saque

        conta = self.filtrar_conta(numero_conta)
        # Chama o método filtrar_conta para verificar se a conta existe

        if conta:
            # Verifica se a conta foi encontrada
            if conta[3] >= valor:
                # Verifica se o saldo é suficiente para o saque
                novo_saldo = conta[3] - valor
                # Calcula o novo saldo após o saque
                self.cursor.execute('''UPDATE contas SET saldo = ? WHERE id = ?''', (novo_saldo, conta[0]))
                # Atualiza o saldo da conta no banco de dados
                self.cursor.execute('''INSERT INTO transacoes (tipo, valor, data, conta_id)
                                       VALUES (?, ?, ?, ?)''', ("Saque", valor, datetime.now().strftime("%d-%m-%Y %H:%M:%S"), conta[0]))
                # Insere uma nova transação de saque na tabela transacoes do banco de dados
                self.conn.commit()
                # Confirma a transação no banco de dados
                messagebox.showinfo("Sacar", "Saque realizado com sucesso!")
                # Exibe uma mensagem informando que o saque foi realizado com sucesso
            else:
                messagebox.showerror("Erro", "Saldo insuficiente.")
                # Exibe uma mensagem de erro informando que o saldo é insuficiente
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
            # Exibe uma mensagem de erro informando que a conta não foi encontrada
    
    def exibir_extrato(self):
        # Define o método exibir_extrato para mostrar o extrato da conta
        numero_conta = simpledialog.askinteger("Extrato", "Informe o número da conta:")
        # Abre uma caixa de diálogo para o usuário inserir o número da conta

        conta = self.filtrar_conta(numero_conta)
        # Chama o método filtrar_conta para verificar se a conta existe

        if conta:
            # Verifica se a conta foi encontrada
            self.cursor.execute('''SELECT nome FROM clientes WHERE id = ?''', (conta[6],))
            # Seleciona o nome do cliente associado à conta
            cliente = self.cursor.fetchone()[0]
            # Armazena o nome do cliente

            self.cursor.execute('''SELECT tipo, valor, data FROM transacoes WHERE conta_id = ?''', (conta[0],))
            # Seleciona todas as transações associadas à conta
            transacoes = self.cursor.fetchall()
            # Armazena as transações
            saldo_anterior = 0
            # Inicializa o saldo anterior como 0
            extrato = ""
            # Inicializa a variável extrato como uma string vazia
            for t in transacoes:
                # Itera sobre as transações
                extrato += f"{t[2]} - {t[0]}: R${t[1]:.2f}\n"
                # Adiciona a transação ao extrato formatado
                if t[0] == "Depósito":
                    saldo_anterior += t[1]
                    # Atualiza o saldo anterior se for um depósito
                elif t[0] == "Saque":
                    saldo_anterior -= t[1]
                    # Atualiza o saldo anterior se for um saque

            saldo_atual = conta[3]
            # Armazena o saldo atual da conta
            messagebox.showinfo("Extrato", f"CLIENTE: {cliente}\nAgência: {conta[2]}  Número Conta: {numero_conta}\n\nData                      Saldo Anterior\n\n{extrato}\nSaldo Atual: R${saldo_atual:.2f}")
            # Exibe o extrato formatado em uma mensagem
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
            # Exibe uma mensagem de erro informando que a conta não foi encontrada
    
    def consultar_clientes(self):
        # Define o método consultar_clientes para listar todos os clientes
        self.cursor.execute('''SELECT * FROM clientes''')
        # Seleciona todos os clientes da tabela clientes
        clientes = self.cursor.fetchall()
        # Armazena os dados dos clientes

        clientes_info = ""
        # Inicializa a variável clientes_info como uma string vazia
        for cliente in clientes:
            # Itera sobre os clientes
            self.cursor.execute('''SELECT numero, agencia, saldo FROM contas WHERE cliente_id = ?''', (cliente[0],))
            # Seleciona todas as contas associadas ao cliente
            contas = self.cursor.fetchall()
            # Armazena os dados das contas
            contas_info = "\n".join([f"Conta {conta[0]} (Agência: {conta[1]}) - Saldo: R${conta[2]:.2f}" for conta in contas])
            # Formata os dados das contas
            clientes_info += f"Cliente: {cliente[1]} - CPF: {cliente[3]}\n{contas_info}\n\n"
            # Adiciona os dados do cliente e suas contas à variável clientes_info

        if clientes_info:
            # Verifica se há clientes cadastrados
            messagebox.showinfo("Clientes Cadastrados", clientes_info)
            # Exibe as informações dos clientes cadastrados em uma mensagem
        else:
            messagebox.showinfo("Clientes Cadastrados", "Nenhum cliente cadastrado.")
            # Exibe uma mensagem informando que não há clientes cadastrados
    
    def filtrar_usuario(self, cpf):
        # Define o método filtrar_usuario para buscar um cliente pelo CPF
        self.cursor.execute('''SELECT * FROM clientes WHERE cpf = ?''', (cpf,))
        # Seleciona o cliente com o CPF informado
        return self.cursor.fetchone()
        # Retorna os dados do cliente encontrado

    def filtrar_conta(self, numero_conta):
        # Define o método filtrar_conta para buscar uma conta pelo número
        self.cursor.execute('''SELECT * FROM contas WHERE numero = ?''', (numero_conta,))
        # Seleciona a conta com o número informado
        return self.cursor.fetchone()
        # Retorna os dados da conta encontrada

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente
    root = tk.Tk()
    # Cria a janela principal da interface gráfica
    app = BancoApp(root)
    # Cria uma instância da classe BancoApp
    root.mainloop()
    # Inicia o loop principal da interface gráfica

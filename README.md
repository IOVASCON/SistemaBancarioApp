# Sistema Bancário

Este projeto consiste em um sistema bancário para criação e gerenciamento de contas, utilizando uma interface gráfica desenvolvida com Tkinter e um banco de dados SQLite para armazenamento das informações. O sistema permite cadastrar novos usuários, criar contas, realizar depósitos, saques, consultar extratos e visualizar clientes cadastrados.

## Funcionalidades

- **Cadastro de Usuários:** Permite cadastrar novos usuários no sistema.
- **Criação de Contas:** Permite criar contas para os usuários cadastrados.
- **Depósitos:** Permite realizar depósitos nas contas.
- **Saques:** Permite realizar saques das contas, respeitando limites de saldo e saques.
- **Consulta de Extratos:** Permite consultar o extrato de uma conta, incluindo todas as transações realizadas.
- **Consulta de Clientes:** Permite visualizar todos os clientes cadastrados e suas respectivas contas.

## Tecnologias Utilizadas

- **Python 3:** Linguagem de programação utilizada para o desenvolvimento do sistema.
- **Tkinter:** Biblioteca padrão do Python para criação de interfaces gráficas.
- **SQLite:** Banco de dados utilizado para armazenamento das informações.

## Estrutura do Projeto

Sistema_Bancario/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── cliente.py
│   │   ├── conta.py
│   │   ├── transacao.py
│   │   └── historico.py
│   └── ui/
│       └── interface.py
├── tests/
│   ├── **init__.py
│   ├── test_cliente.py
│   ├── test_conta.py
│   ├── test_transacao.py
│   ├── test_historico.py
│   └── test_interface.py
└── .gitignore (se necessário)
└── README.md

## Instalação

    1. Clone o repositório:

    git clone https://github.com/iovascon/Sistema_Bancario.git
    cd Sistema_Bancario

    2. Crie e ative um ambiente virtual:

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows

    3. Instale as dependências:

    pip install -r requirements.txt

    4. Inicialize o banco de dados:

    python src/database.py

    5. Execute a aplicação:

    python src/main.py

## Estrutura dos Arquivos

src/main.py

Arquivo principal que inicia a aplicação e cria a interface gráfica.
src/database.py

Arquivo responsável pela criação e inicialização do banco de dados SQLite.
src/models/cliente.py

Contém as classes Cliente e PessoaFisica.
src/models/conta.py

Contém as classes Conta e ContaCorrente.
src/models/transacao.py

Contém as classes Transacao, Saque e Deposito.
src/models/historico.py

Contém a classe Historico, que gerencia as transações de uma conta.
src/ui/interface.py

Contém a classe BancoApp, que define a interface gráfica e as funcionalidades do sistema.

## Testes

Os testes estão localizados na pasta tests e utilizam o framework unittest do Python. Para executar todos os testes, utilize o comando:

python -m unittest discover tests

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

    Nome: Izairton Oliveira de Vasconcelos
    Email: iovascon@gmail.com

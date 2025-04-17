# 🌱 Sistema de Gestão de Insumos Agrícolas

Este é um sistema em Python para gerenciamento de insumos agrícolas, culturas e fornecedores. Ele permite cadastrar, listar e acompanhar o uso de insumos por cultura, mantendo o controle do estoque de forma automatizada.

## 📂 Estrutura do Projeto

. ├── main.py └── src/ └── connections.py # Responsável pela conexão com o banco de dados

markdown
Copiar
Editar

## 🚀 Funcionalidades

- Cadastrar e listar **fornecedores**
- Cadastrar e listar **insumos** (sementes, fertilizantes, defensivos)
- Cadastrar e listar **culturas** (ex: milho, soja)
- Registrar e listar **insumos utilizados** em culturas
- Controle automático da **quantidade em estoque**

## 🧠 Tecnologias Utilizadas

- Python 3.x
- Pandas
- Banco de Dados relacional (Ex: Oracle, PostgreSQL, etc.)
- CLI (interface via terminal)

## ⚙️ Requisitos

- Python 3.8+
- Instalar dependências (caso necessário):

```bash
pip install pandas
Um banco de dados configurado com as seguintes tabelas:

sql
Copiar
Editar
CREATE TABLE fornecedores (
    id_fornecedor INTEGER PRIMARY KEY,
    nome TEXT
);

CREATE TABLE insumos (
    id_insumo INTEGER PRIMARY KEY,
    nome TEXT,
    tipo TEXT,
    quantidade_estoque REAL,
    custo_unitario REAL,
    id_fornecedor INTEGER REFERENCES fornecedores(id_fornecedor)
);

CREATE TABLE cultura (
    id_culturas INTEGER PRIMARY KEY,
    nome TEXT,
    area_ha REAL
);

CREATE TABLE insumosutilizados (
    id_insumo_utilizado INTEGER PRIMARY KEY,
    id_insumo INTEGER REFERENCES insumos(id_insumo),
    id_cultura INTEGER REFERENCES cultura(id_culturas),
    quantidade_utilizada REAL
);
▶️ Como Executar
Certifique-se de que o banco de dados está rodando e que a conexão está configurada corretamente em src/connections.py.

Execute o script principal:

python main.py
Utilize o menu interativo no terminal para navegar pelas funcionalidades.

🔒 Conexão com o Banco
O arquivo src/connections.py deve conter as funções connect_db() e close_connection() para gerenciar a conexão com o banco de dados:

def connect_db():
    # lógica para conectar ao banco
    return connection, cursor

def close_connection():
    # lógica para fechar a conexão
💡 Melhorias Futuras
Interface Web com Django ou Flask

Validações mais robustas nos inputs

Exportação de relatórios em CSV

Registro de histórico de movimentações de estoque

🧑‍🌾 Autor
Feito com 💚 para facilitar a vida no campo.

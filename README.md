<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto: FarmTech Solutions - Modelo de Banco de Dados

## Nome do grupo: Rumo ao NEXT

## 👨‍🎓 Integrantes:

- Felipe Livino dos Santos (RM 563187)
- Daniel Veiga Rodrigues de Faria (RM 561410)
- Tomas Haru Sakugawa Becker (RM 564147)
- Daniel Tavares de Lima Freitas (RM 562625)
- Gabriel Konno Carrozza (RM 564468)

## 👩‍🏫 Professores:

### Tutor(a)

- Leonardo Ruiz Orabona

### Coordenador(a)

- ANDRÉ GODOI CHIOVATO

## 📜 Descrição

Este é um sistema em Python para gerenciamento de insumos agrícolas, culturas e fornecedores. Ele permite cadastrar, listar e acompanhar o uso de insumos por cultura, mantendo o controle do estoque de forma automatizada.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

  - <b>connections.py</b>: Responsável pela conexão com o banco de dados.

- <b>main.py</b>: Arquivo principal para execução do sistema.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>ddl.sql</b>: Arquivo com o script para a criação das tabelas no banco de dados

## 🔧 Como executar o código

Para executar o código deste projeto, siga os passos abaixo:

1.  _Pré-requisitos:_

    - Certifique-se de ter o _Python 3.8_ ou superior instalado em sua máquina. Você pode verificar a versão do Python executando o comando python --version no seu terminal.
    - É necessário ter um _banco de dados relacional_ instalado e configurado. Este projeto foi pensado para ser compatível com Oracle, mas pode ser adaptado para outros bancos. Certifique-se de ter as credenciais de acesso ao banco de dados.
    - A biblioteca _Pandas_ é utilizada no projeto. Caso não a tenha instalada, você pode instalá-la utilizando o pip:
      bash
      pip install pandas
    - Instale o <a href="https://www.oracle.com/database/sqldeveloper/technologies/download/">Oracle SQL Developer</a>

2.  _Clonar o repositório:_
    bash
    git clone [https://github.com/danitlf/trabalho2-fiap](https://github.com/danitlf/trabalho2-fiap)
    cd trabalho2-fiap

3.  _Configurar a conexão com o banco de dados:_

    - Localize o arquivo connections.py dentro da pasta src.
    - Edite este arquivo com as informações de conexão do seu banco de dados (host, porta, nome do banco de dados, usuário e senha).

4.  _Configurar o banco de dados:_

    - Abra o "Oracle SQL Developer"
    - Conecte com as credencias do seu banco de dados (host, porta, nome do banco de dados, usuário e senha).
    - Abra e copie o conteudo do arquivo ddl.sql
    - Execute o script para que seja criada as tabelas

5.  _Executar o sistema:_
    - Abra o seu terminal na raiz do projeto.
    - Execute o arquivo principal main.py com o comando:
      bash
      python main.py
    - O sistema será executado via linha de comando (CLI), e você poderá interagir com as funcionalidades através do terminal. Siga as instruções que aparecerem na tela para cadastrar fornecedores, insumos, culturas, registrar o uso de insumos e verificar o estoque.

## 🗃 Histórico de lançamentos

- 0.5.0 - Aguardando data
  - Implementação de controle automático da quantidade em estoque.
- 0.4.0 - Aguardando data
  - Adição da funcionalidade de registrar e listar insumos utilizados em culturas.
- 0.3.0 - Aguardando data
  - Implementação das funcionalidades de cadastrar e listar culturas.
- 0.2.0 - Aguardando data
  - Implementação das funcionalidades de cadastrar e listar insumos (sementes, fertilizantes, defensivos).
- 0.1.0 - Aguardando data
  - Implementação das funcionalidades de cadastrar e listar fornecedores.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

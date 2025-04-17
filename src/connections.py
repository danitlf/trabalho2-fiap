import os
import oracledb
import pandas as pd

USER_DB = ""
PASSWORD_DB = ""
DSN_DB = "oracle.fiap.com.br:1521/ORCL"
conn = None
cursor = None

def connect_db():

    try:
        # if conn and cursor:
        #     return conn, cursor
        # Efetua a conexão com o Usuário no servidor
        conn = oracledb.connect(user=USER_DB, password=PASSWORD_DB, dsn=DSN_DB)
        cursor = conn.cursor()
    except Exception as e:
        # Informa o erro
        print("Erro: ", e)
        # Flag para não executar a Aplicação
        conexao = False
    else:
        # Flag para executar a Aplicação
        return conn, cursor

def close_connection():
    try:
        cursor.close()
        conn.close()
    except:
        print("Conexão já fechada!")
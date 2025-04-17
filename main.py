import os
import pandas as pd
from src.connections import connect_db, close_connection

connection, cursor = connect_db()

def get_insumo(id_insumo):
    try:
        cursor.execute("""select quantidade_estoque from insumos
        where id_insumo = (:1)
        """, [id_insumo])

        insumos = cursor.fetchall()

        return insumos[0][0]
    except:
        print("Insumo não existe")
        pass

def update_quantidade_insumo(quantidade_atual, id_insumo):
    try:
        cursor.execute("""update insumos set quantidade_estoque = (:1) where id_insumo = (:2)""", [quantidade_atual, id_insumo])
    except:
        print("Deu ruim, se vira!")

def cadastrar_fornecedor():
    nome = input("Nome do fornecedor: ")
    cursor.execute("INSERT INTO fornecedores (nome) VALUES (:1)", [nome])
    connection.commit()
    print("Fornecedor cadastrado.")

def listar_fornecedores():
    cursor.execute("SELECT f.id_fornecedor, f.nome FROM fornecedores f")
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(f"[{row[0]}] {row[1]}")

def cadastrar_insumo():
    nome = input("Nome do insumo: ")
    tipo = input("Tipo (semente, fertilizante, defensivo): ")
    qtd = float(input("Quantidade em estoque: "))
    custo = float(input("Custo unitário: "))
    listar_fornecedores()
    id_fornecedor = int(input("ID do fornecedor: "))
    cursor.execute("""
        INSERT INTO insumos (nome, tipo, quantidade_estoque, custo_unitario, id_fornecedor)
        VALUES (:1, :2, :3, :4, :5)
    """, [nome, tipo, qtd, custo, id_fornecedor])
    connection.commit()
    print("Insumo cadastrado.")

def listar_insumos():
    cursor.execute("""
        SELECT i.id_insumo, i.nome, i.tipo, i.quantidade_estoque, i.custo_unitario, f.nome 
        FROM insumos i LEFT JOIN fornecedores f ON i.id_fornecedor = f.id_fornecedor
    """)
    for row in cursor.fetchall():
        print(f"[{row[0]}] {row[1]} | Tipo: {row[2]} | Qtde: {row[3]} | Custo: R${row[4]} | Fornecedor: {row[5]}")

def cadastrar_cultura():
    nome = input("Nome da cultura (ex: milho): ")
    area = float(input("Área em hectares: "))
    
    cursor.execute("""
        INSERT INTO cultura (nome, area_ha)
        VALUES (:1, :2)
    """, [nome, area])
    connection.commit()
    print("Cultura cadastrada.")

def listar_culturas():
    cursor.execute("""
        SELECT c.id_culturas, c.nome, c.area_ha
        FROM cultura c
    """)
    for row in cursor.fetchall():
        print(f"[{row[0]}] Cultura: {row[1]} | Área: {row[2]}ha")

def cadastrar_insumo_utilizados():
    listar_insumos()
    id_insumo = int(input("Id do insumo: "))
    quantidade_de_insumo = get_insumo(id_insumo)
    listar_culturas()
    id_cultura = int(input("Id da cultura: "))
    quantidade_utilizada = float(input("Quantidade utilizada: "))
    if quantidade_utilizada <= quantidade_de_insumo:
        quantidade_insumo_restante = quantidade_de_insumo - quantidade_utilizada
        update_quantidade_insumo(quantidade_insumo_restante, id_insumo)
        cursor.execute("""
            INSERT INTO insumosutilizados (id_insumo, id_cultura, quantidade_utilizada)
            VALUES (:1, :2, :3)
        """, [id_insumo, id_cultura, quantidade_utilizada])
        connection.commit()
        print("Utilização do insumo cadastrado.")
    else:
        print("quantidade maior que a do estoque")
        return 

def listar_insumos_utilizados():
    cursor.execute("""
        SELECT i.id_insumo_utilizado, ins.nome, c.nome, i.quantidade_utilizada
        FROM insumosutilizados i LEFT JOIN cultura c ON i.id_cultura = c.id_culturas
        LEFT JOIN insumos ins ON i.id_insumo = ins.id_insumo
    """)
    for row in cursor.fetchall():
        print(f"[{row[0]}] - Insumo: {row[1]} | Cultura: {row[2]} | Quantidade Utilizada: {row[3]}")


def menu():
    while True:
        print("\n===== Gestão de Insumos e Culturas =====")
        print("1. Cadastrar fornecedor")
        print("2. Listar fornecedores")
        print("3. Cadastrar insumo")
        print("4. Listar insumos")
        print("5. Cadastrar cultura")
        print("6. Listar culturas")
        print("7. Cadastrar insumo utilizado")
        print("8. Listar insumos utilizados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_fornecedor()
        elif opcao == "2":
            listar_fornecedores()
        elif opcao == "3":
            cadastrar_insumo()
        elif opcao == "4":
            listar_insumos()
        elif opcao == "5":
            cadastrar_cultura()
        elif opcao == "6":
            listar_culturas()
        elif opcao == "7":
            cadastrar_insumo_utilizados()
        elif opcao == "8":
            listar_insumos_utilizados()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()

close_connection()


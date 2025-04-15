import os
import pandas as pd
from src.connections import connect_db, close_connection

connection, cursor = connect_db()

def cadastrar_fornecedor():
    nome = input("Nome do fornecedor: ")
    cursor.execute("INSERT INTO fornecedores (nome) VALUES (:1)", [nome])
    connection.commit()
    print("Fornecedor cadastrado.")

def listar_fornecedores():
    cursor.execute("SELECT * FROM fornecedores")
    for row in cursor.fetchall():
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
        SELECT c.nome, c.area_ha
        FROM cultura c
    """)
    for row in cursor.fetchall():
        print(f"Cultura: {row[0]} | Área: {row[1]}ha")

def menu():
    while True:
        print("\n===== Gestão de Insumos e Culturas =====")
        print("1. Cadastrar fornecedor")
        print("2. Listar fornecedores")
        print("3. Cadastrar insumo")
        print("4. Listar insumos")
        print("5. Cadastrar cultura")
        print("6. Listar culturas")
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
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

menu()

close_connection()


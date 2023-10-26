import tkinter as tk
from tkinter import ttk
import sqlite3

def criar_tabela_usuario():
    # Conectar ao banco de dados e inserir o novo usuário
    conn = sqlite3.connect('banco_barbara.db')
    cursor = conn.cursor()

    #AUTOINCREMENT - insere o valor sequncialmente de forma automatica
    # NOT NULL - Campo não pode ser vazio

    #Criar a tabela usuario
    cursor.execute('''CREATE TABLE IF NOT EXISTS perfil(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    perfil TEXT 1 is administrador
                    perfil TEXT 2 is vendas)
    ''')

    conn.commit()
    conn.close()
def criar_perfil():
    perfil = perfil_var.get()
    conn = sqlite3.connect('banco_barbara.db')
    cursor = conn.cursor()
    cursor.execute("SELECT perfil FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    perfil = cursor.fetchone()

    conn.close()


    if perfil:
        perfil = perfil[0]
        if perfil == 1:
            # Direcionar para a tela de vendas (ou a lógica desejada)
            abrir_tela_de_vendas()
        elif perfil == 2:
            # Direcionar para o menu de acesso às telas de cadastro
            abrir_menu_de_acesso()
    else:
        # Exibir uma mensagem de erro de login inválido
        erro_login_label.config(text="Usuário ou senha inválidos")


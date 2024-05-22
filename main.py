import os
import oracledb
import conexao
connection = oracledb.connect(
    user = "BD150224424",
    password = 'Qwiji4',    
    dsn = "172.16.12.14/xe")
print("Successfully Connected")
cursor = connection.cursor()
os.system('cls')
# ---------------------------- MENU DE COMANDOS ------------------------------

def mostrar_estoque():
    cursor.execute("SELECT * FROM PRODUTOS")
    for row in cursor:
        #
        cod_prod = row[0]
        nome_prod = row[1]
        desc_prod = row[2]
        CP = row[3]
        CF = row[4]
        CV = row[5]
        IV = row[6]
        ML = row[7]
        #
        desc_prod = conexao.hill_criptografia(desc_prod, conexao.chave_inversa)
        conexao.calculo_print_tabela(cod_prod, nome_prod, desc_prod, CP, CF, CV, IV, ML)

menu = int(input("""
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTOS
[2].ALTERAR PRODUTOS
[3].APAGAR PRODUTOS
[4].LISTAR PRODUTOS
[5].SAIR
=================================================================
                    OPÇÃO: """))
os.system('cls')

while menu != 5:
# ---------------------------- ROTINA DE PRODUTOS -----------------------------
    if menu == 1: #CADASTRAR PRODUTOS
        conexao.cadastrar_produto()
    elif menu == 2: #ALTERAR PRODUTOS
        conexao.alterar_produto()
    elif menu == 3: #DELETAR PRODUTO
        conexao.apagar_produto()
    elif menu == 4: #LISTAR PRODUTOS
        conexao.mostrar_estoque()
    elif menu == 0: #CRIAR TABELA
        conexao.criar_tabela()
    elif menu == -1:
        conexao.deletar_tabela()
    
    menu = int(input("""
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTOS
[2].ALTERAR PRODUTOS
[3].APAGAR PRODUTOS
[4].LISTAR PRODUTOS
[5].SAIR
=================================================================
                    OPÇÃO: """))
    
    os.system('cls')
    # ---------------------------- FIM ROTINA DE PRODUTOS -----------------------------
connection.commit()
cursor.close()
connection.close()
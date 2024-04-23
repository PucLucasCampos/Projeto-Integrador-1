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
menu = int(input("""
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].MOSTRAR PRODUTO/ESTOQUE
[2].CRIAR TABELA
[3].CADASTRAR PRODUTO
[4].DELETAR TABELA
[5].DELETAR PRODUTOS
[0].SAIR
=================================================================
                    OPÇÃO: """))
while menu != 0:
# ---------------------------- ROTINA DE PRODUTOS -----------------------------
    if menu == 1:
        conexao.mostrar_estoque()
    elif menu == 2:
        conexao.criar_tabela()
        print("Tabela Criada com Sucesso")
    elif menu == 3:
        # ---------------------------- CADASTRO DOS PRODUTOS ----------------------------
        cod_prod = int(input('Código do Produto: '))       #CODIGO DO PRODUTO
        nome_prod = str(input('Nome Produto: '))              #NOME DO PRODUTO
        desc_prod = str(input('Descrição do Produto: ')) #DESCRIÇÃO DO PRODUTO

        CP = float(input('Custo do  Produto: '))              #CUSTO PAGO PELO PRODUTO PARA O FORNECEDOR
        ML = float(input('Margem de Lucro sobre a Venda: '))  #MARGEM DE LUCRO SOBRE A VENDA DO PRODUTO
        CF = float(input('Custo Fixo/Administrativo(%): '))    #CUSTO FIXO (ESPAÇO FÍSICO, DESPESAS, FUNCIONÁRIOS...)
        CV = float(input('Comissão de Vendas(%): '))          #COMISSÃO SOBRE A VENDA DO PRODUTO
        IV = float(input('Impostos(%): '))                    #IMPOSTOS SOBRE A VENDA DO PRODUTO
        os.system('cls')
        # conexao.add_produto()
    elif menu == 4:
        conexao.deletar_tabela()
    elif menu == 5:
        conexao.deletar_produto()
    
    menu = int(input("""
=================================================================
                          BEM VINDO AO
                  SISTEMA DE CADASTRO DE PRODUTO!!!
=================================================================
OPÇÕES:
[1].CADASTRAR PRODUTO
[2].ALTERAR PRODUTO
[3].EXCLUIR PRODUTO/ESTOQUE
[4].MOSTRAR PRODUTO/ESTOQUE
[0].SAIR
=================================================================
                    OPÇÃO: """))
connection.commit()
cursor.close()
connection.close()
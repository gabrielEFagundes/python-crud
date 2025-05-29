import mysql.connector
from tabulate import tabulate

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ecommerce',
)

cursor = conexao.cursor()

print('Conexão bem-sucedida!')
escolha = 0

while escolha != 5:
    escolha = int(input('\n===Bem-vindo(a) à MarketFast!==='
                        '\n1- Inserir produto novo'
                        '\n2- Listar produtos'
                        '\n3- Ajustar preço/estoque por ID'
                        '\n4- Remover produtos sem estoque'
                        '\n5- Sair'
                        '\nSua escolha: '))

    if escolha == 1:
        nome = input('\nPor favor, digite o nome do produto: ')
        preco = float(input('Digite o preço: '))
        estoque = int(input('Digite o estoque: '))
        avaliacao = float(input('Digite a avaliação: '))
        categoria = input('Digite a categoria: ')

        comando = f'INSERT INTO produtos (nome, preco, estoque, avaliacao, categoria) VALUES ("{nome}", {preco}, "{estoque}", "{avaliacao}", "{categoria}")'
        cursor.execute(comando)
        conexao.commit()
        print('\nProduto adicionado com êxito!')

    elif escolha == 2:
        listar = int(input('\n1- Filtrar por avaliação > 4,0'
                           '\n2- Filtrar por categoria'
                           '\nSua escolha: '))

        if listar == 1:
            comando = f'SELECT * FROM produtos WHERE avaliacao >= 4,0'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print("\n===========\n")
            print('ID\t\tNome\t\tPreço\t\tEstoque\t\tAvaliação\t\tCategoria')
            print('-----------------------------------------------')
            print(tabulate(resultado, headers="firstrow", tablefmt="fancy_grid"))
            print('\n===========')

        elif listar == 2:
            categoria = input('\nDigite a categoria para pesquisar: ')

            comando = f'SELECT * FROM produtos WHERE categoria = "{categoria}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print("\n===========\n")
            print('ID\t\tNome\t\tPreço\t\tEstoque\t\tAvaliação\t\tCategoria')
            print('-----------------------------------------------')
            print(tabulate(resultado, headers="firstrow", tablefmt="fancy_grid"))
            print('\n===========')

    elif escolha == 3:
        id = int(input('\nDigite o ID do produto: '))
        preco_novo = float(input('Digite o preço atualizado: '))
        estoque_novo = int(input('Digite o estoque atualizado: '))

        comando = f'UPDATE produtos SET preco = "{preco_novo}", estoque = "{estoque_novo}" WHERE id = {id}'
        cursor.execute(comando)
        conexao.commit()
        print('\nProduto atualizado com sucesso!')

    elif escolha == 4:
        confirmacao = int(input(f'Deseja mesmo excluir? (1- sim / 2- não)\n'))

        if confirmacao == 1:
            comando = f'DELETE FROM produtos WHERE estoque = 0'
            cursor.execute(comando)
            conexao.commit()
            print('\nProduto deletado com sucesso!')

        else:
            print('\nOperação cancelada...')

    elif escolha == 5:
        print('\nEncerrando o sistema...')
        break

cursor.close()
conexao.close()
import mysql.connector
from tabulate import tabulate

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='loja',
)

cursor = conexao.cursor()

print('Conexão bem-sucedida!')
escolha = 0

while escolha != 5:
    escolha = int(input('\n===Bem-vindo à loja!==='
                        '\n1- Inserir produto'
                        '\n2- Listar produtos'
                        '\n3- Alterar preço'
                        '\n4- Remover produto'
                        '\n5- Sair'
                        '\nSua escolha: '))

    if escolha == 1:
        nomeProduto = input('\nPor favor, digite o nome do produto: ')
        preco = float(input('Agora digite o preço do produto: '))

        comando = f'INSERT INTO produtos (nomeProduto, preco) VALUES ("{nomeProduto}", {preco})'
        cursor.execute(comando)
        conexao.commit()
        print('\nProduto adicionado com êxito!')

    elif escolha == 2:
        comando = f'SELECT id AS ID, nomeProduto AS Nome, preco AS Preço FROM produtos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print("\n===========\n")
        print('ID\t\tNome\t\tPreço')
        print('-----------------------------')
        print(tabulate(resultado, headers="firstrow", tablefmt="fancy_grid"))
        print('\n===========')

    elif escolha == 3:
        id = int(input('\nDigite o ID do produto: '))
        precoNovo = float(input('Digite agora o novo preço do produto: '))

        comando = f'UPDATE produtos SET preco = {precoNovo} WHERE id = {id}'
        cursor.execute(comando)
        conexao.commit()
        print('\nTabela atualizada com sucesso!')

    elif escolha == 4:
        id = int(input('\nDigite o código ID do produto: '))
        confirmacao = int(input(f'Deseja mesmo excluir o produto do id {id}? (1- sim / 2- não)\n'))

        if confirmacao == 1:
            comando = f'DELETE FROM produtos WHERE id = {id}'
            cursor.execute(comando)
            conexao.commit()
            print('\nProduto deletado com sucesso!')

        else:
            print('\nOperação cancelada...')

    elif escolha == 5:
        print('\nEncerrando o sistema...')
        break;

cursor.close()
conexao.close()
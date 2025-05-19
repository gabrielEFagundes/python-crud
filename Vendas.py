import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'bdyoutube',
)

cursor = conexao.cursor()
#CRUD

print('Conexão bem-sucedida!')

# -- CREATE --
'''
nome_produto = input('Digite o nome do produto: ')
valor = int(input('Digite o valor do produto: '))

comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
# conexao.commit() # Edita o banco de dados
resultado = cursor.fetchall() # Lê o banco de dados
'''

# -- READ --
'''
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
# conexao.commit()
resultado = cursor.fetchall()
print(resultado)
'''

# -- UPDATE --
'''
nome_produto = 'Bolacha'
valor = 8
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
'''

# -- DELETE --
'''
nome_produto = 'Bolacha'
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
'''

cursor.close()
conexao.close()
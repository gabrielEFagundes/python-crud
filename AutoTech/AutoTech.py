import mysql.connector
from tabulate import tabulate

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='autotech',
)

cursor = conexao.cursor()

class AutoTech():
    def create(self, nome, peso, lote, data, setor):
        comando = f'INSERT INTO pecas (nome, peso, lote, data_fabricacao, setor) VALUES ("{nome}", {peso}, {lote}, "{data}", "{setor}")'
        cursor.execute(comando)
        conexao.commit()
        print('\nPeça criada com sucesso!')

    def read(self, forma):
        if forma == 1:
            comando = f'SELECT * FROM pecas WHERE data_fabricacao > "2024-01-01"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(tabulate(resultado))

        elif forma == 2:
            setor = input('\nDigite o setor que você deseja: ')

            comando = f'SELECT * FROM pecas WHERE setor = "{setor}"'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(tabulate(resultado))

    def update(self, id, peso):
        comando = f'UPDATE pecas SET peso = {peso} WHERE id = {id}'
        cursor.execute(comando)
        conexao.commit()
        print('\nPeso da peça atualizada com sucesso!')

    def delete(self, lote):
        confirma = input('\nTem certeza? (y/n): ')

        if confirma == 'y' or confirma == 'Y':
            comando = f'DELETE * FROM pecas WHERE lote = "{lote}"'
            cursor.execute(comando)
            conexao.commit()
            print('\nPeça deletada com sucesso!')

        else:
            print('\nOperação cancelada.')
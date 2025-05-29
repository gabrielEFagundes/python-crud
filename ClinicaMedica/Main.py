import mysql.connector
from tabulate import tabulate

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ClinicaMedica',
)

cursor = conexao.cursor()

print('Conexão bem-sucedida!')
escolha = 0

while escolha != 5:
    escolha = int(input('\n===Bem-vindo(a) à HealthCare Solutions!==='
                        '\n1- Inserir novo paciente'
                        '\n2- Listar paciente'
                        '\n3- Atualizar histórico do paciente'
                        '\n4- Remover registros inativos'
                        '\n5- Sair'
                        '\nSua escolha: '))

    if escolha == 1:
        nome = input('\nPor favor, digite o nome do paciente: ')
        idade = int(input('Digite sua idade: '))
        ultima_consulta = input('Digite a data da sua última consulta: ')
        tipo_sanguineo = input('Digite seu tipo sanguíneo: ')
        historico = input('Observações sobre seu histórico médico: ')

        comando = f'INSERT INTO pacientes (nome, idade, ultima_consulta, tipo_sanguineo, historico) VALUES ("{nome}", {idade}, "{ultima_consulta}", "{tipo_sanguineo}", "{historico}")'
        cursor.execute(comando)
        conexao.commit()
        print('\nPaciente adicionado com êxito!')

    elif escolha == 2:
        comando = f'SELECT * FROM pacientes WHERE ultima_consulta >= CURDATE() - INTERVAL 30 DAY'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print("\n===========\n")
        print('ID\t\tNome\t\tIdade\t\tÚltima Consulta')
        print('-----------------------------------------------')
        print(tabulate(resultado, headers="firstrow", tablefmt="fancy_grid"))
        print('\n===========')

    elif escolha == 3:
        id = int(input('\nDigite o ID do paciente: '))
        historico_novo = input('Digite o histórico atualizado: ')

        comando = f'UPDATE pacientes SET historico = "{historico_novo}" WHERE id = {id}'
        cursor.execute(comando)
        conexao.commit()
        print('\nPaciente atualizado com sucesso!')

    elif escolha == 4:
        confirmacao = int(input(f'Deseja mesmo excluir? (1- sim / 2- não)\n'))

        if confirmacao == 1:
            comando = f'DELETE FROM pacientes WHERE ultima_consulta <= CURDATE() - INTERVAL 730 DAY'
            cursor.execute(comando)
            conexao.commit()
            print('\nPaciente deletado com sucesso!')

        else:
            print('\nOperação cancelada...')

    elif escolha == 5:
        print('\nEncerrando o sistema...')
        break;

cursor.close()
conexao.close()
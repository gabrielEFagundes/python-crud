import mysql.connector
import time

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ConsultaMedica',
)

cursor = conexao.cursor()

print('Conexão bem-sucedida!')
print('Começando o sistema...')
time.sleep(2)

escolha = 0

while escolha != 5:
    escolha = input('\n---Bem-Vindo ao sistema de consultas médicas!---'
          '\n1- Cadastrar'
          '\n2- Atualizar'
          '\n3- Visualizar'
          '\n4- Deletar'
          '\n5- Sair'
          '\nSua escolha: ')

    if escolha == 1:
        cadastro = input('\n\n1- Cadastrar-se'
        '\n2- Cadastrar médico'
        '\n3- Cadastrar consulta')

        if cadastro == 1:
            nome = input('\nDigite seu nome: ')
            data_nasc = input('Digite a sua data de nascimento (AAAA-MM-DD): ')

            comando = f'INSERT INTO paciente (nome, data_nascimento) VALUES ("{nome}", "{data_nasc}")'
            cursor.execute(comando)
            conexao.commit()
            print('\nPaciente cadastrado com sucesso!')

        elif cadastro == 2:
            senha = input('\nDigite a senha de identificação: ')

            if senha == 'admin123':
                print('\nSenha correta!')
                nome = input('\nDigite o nome do médico: ')
                especialidade = input('\nDigite a especialidade do médico: ')

                comando = f'INSERT INTO medico (nome, especialidade) VALUES ("{nome}", "{especialidade}")'
                cursor.execute(comando)
                conexao.commit()
                print('\nMédico cadastrado com sucesso!')

        elif cadastro == 3:
            data = input('\nDigite a data de hoje (AAAA-MM-DD): ')
            horario = input('Digite o horário (HH-MM-SS): ')
            id_paciente_fk = int(input('Digite o ID do paciente: '))
            id_medico_fk = int(input('Digite o ID do médico: '))

            senha = input('Digite a senha de identificação: ')

            if senha == 'admin123':
                print('\nSenha correta!')
                status = input('\nDeseja confirmar a consulta? (Y/N): ')

                if status == 'Y' or status  == 'y':
                    comando = f'INSERT INTO consultas (data, horario, status, id_paciente_fk, id_medico_fk) VALUES ("{data}", "{horario}", "confirmada", {id_paciente_fk}, {id_medico_fk})'
                    cursor.execute(comando)
                    conexao.commit()
                    print('\nConsulta cadastrada e confirmada!')

                else:
                    comando = f'INSERT INTO consultas (data, horario, status, id_paciente_fk, id_medico_fk) VALUES ("{data}", "{horario}", "cancelada", {id_paciente_fk}, {id_medico_fk})'
                    cursor.execute(comando)
                    conexao.commit()
                    print('\nConsulta cadastrada e cancelada!')
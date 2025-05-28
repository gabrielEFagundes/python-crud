import mysql.connector
import time

conexao =   mysql.connector.connect(
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

# cadastrar finalizado

    if escolha == 1:
        cadastro = input('\n\n1- Cadastrar-se'
        '\n2- Cadastrar médico'
        '\n3- Cadastrar consulta'
        '\nSua escolha: ')

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

            else:
                print('\nSenha incorreta!\nTente novamente mais tarde.')

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

            else:
                print('\nSenha incorreta!\nTente novamente mais tarde.')

# atualizar finalizado

    elif escolha == 2:
        update = int(input('\n\n1- Atualizar-se'
        '\n2- Atualizar médico'
        '\n3- Atualizar consulta'
        '\nSua escolha: '))

        if update == 1:
            id_paciente = int(input('\nDigite o ID do paciente: '))
            nome = input('Digite o nome do paciente: ')
            data_nasc = input('Digite a data de nascimento do paciente (AAAA-MM-DD): ')

            comando = f'UPDATE paciente SET nome = "{nome}", data_nasc = "{data_nasc}" WHERE id_paciente = {id_paciente}'
            cursor.execute(comando)
            conexao.commit()
            print('\nPaciente atualizado com sucesso!')

        elif update == 2:
            senha = input('\nDigite a senha de identificação: ')

            if senha == 'admin123':
                id_medico = int(input('\nDigite o ID do médico: '))
                nome = input('Digite o novo nome do médico: ')
                especialidade = input('Digite a nova especialidade do médico: ')

                comando = f'UPDATE medico SET nome = "{nome}", especialidade = "{especialidade}" WHERE id_medico = {id_medico}'
                cursor.execute(comando)
                conexao.commit()
                print('\nMédico atualizado com sucesso!')

            else:
                print('\nSenha incorreta!\nTente novamente mais tarde.')

        elif update == 3:
            senha = input('\nDigite a senha de identificação: ')

            if senha == 'admin123':
                id = int(input('\nDigite o ID da consulta: '))
                data = input('Digite a nova data: ')
                horario = input('Digite o novo horário: ')
                status = input('Confirmada ou Cancelada: ')
                id_paciente_fk = input('Digite o ID do paciente novo (ou do mesmo): ')
                id_medico_fk = input('Digite o ID do médico novo (ou do mesmo): ')

                comando = f'UPDATE consultas SET data = "{data}", horario = "{horario}", status = "{status}", id_paciente_fk = {id_paciente_fk}, id_medico_fk = {id_medico_fk} WHERE id = {id}'
                cursor.execute(comando)
                conexao.commit()
                print('\nConsulta atualizada com sucesso!')

            else:
                print('\nSenha incorreta!\nTente novamente mais tarde.')


cursor.close()
conexao.close()
from AutoTech import AutoTech

loop = True

while(loop):
    escolha = int(input('Bem-vindo ao sistema da AutoTech!'
                        '\n1- Adicionar peça'
                        '\n2- Visualizar peças'
                        '\n3- Atualizar peça'
                        '\n4- Deletar peça'
                        '\nSua escolha: '))

    minhaPeca = AutoTech()

    if escolha == 1:
        minhaPeca.create(input('Digite o nome da peça: '),
                         float(input('Digite o peso da peça: ')),
                         input('Digite o lote da peça: '),
                         input('Digite a data de fabricação da peça: '),
                         input('Digite o setor da peça: '))

    elif escolha == 2:
        minhaPeca.read(int(input('\nComo você deseja visualizar?'
                              '\n1- Tudo fabricado à partir desse ano'
                              '\n2- Filtrar por setor'
                              '\nSua escolha: ')))

    elif escolha == 3:
        minhaPeca.update(int(input('Digite o ID da peça: ')),
                         float(input('Digite o peso da peça: ')))

    elif escolha == 4:
        minhaPeca.delete(input('Digite o lote da peça: '))

    else:
        print('Finalizando sistema...')
        loop = False
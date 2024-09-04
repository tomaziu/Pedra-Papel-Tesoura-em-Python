def jqp(a): # função para dizer oque a maquina jogou, o jogador e se ele ganhou empatou ou perdeu
    from random import randint
    maquina = randint(1, 3)
    if a == 1 and maquina == 1:
        print('\033[1mMAQUINA: PEDRA\nJOGADOR: PEDRA\033[m\n\033[1;33mEMPATE\033[m')
    elif a == 1 and maquina == 2:
        print('\033[1mMAQUINA: PAPEL\nJOGADOR: PEDRA\033[m\n\033[1;31mMAQUINA GANHOU\033[m')
    elif a == 1 and maquina == 3:
        print('\033[1mMAQUINA: TESOURA\nJOGADOR: PEDRA\033[m\n\033[1;32mJOGADOR GANHOU!!\033[m')
    elif a == 2 and maquina == 1:
        print('\033[1mMAQUINA: PEDRA\nJOGADOR: PAPEL\033[m\n\033[1;32mJOGADOR GANHOU!!\033[m')
    elif a == 2 and maquina == 2:
        print('\033[1mMAQUINA: PAPEL\nJOGADOR: PAPEL\033[m\n\033[1;33mEMPATE\033[m')
    elif a == 2 and maquina == 3:
        print('\033[1mMAQUINA: TESOURA\nJOGADOR: PAPEL\033[m\n\033[1;31mMAQUINA GANHOU\033[m')
    elif a == 3 and maquina == 1:
        print('\033[1mMAQUINA: PEDRA\nJOGADOR: TESOURA\033[m\n\033[1;31mMAQUINA GANHOU\033[m')
    elif a == 3 and maquina == 2:
        print('\033[1mMAQUINA: PAPEL\nJOGADOR: TESOURA\033[m\n\033[1;32mJOGADOR GANHOU!!\033[m')
    elif a == 3 and maquina == 3:
        print('\033[1mMAQUINA: TESOURA\nJOGADOR: TESOURA\033[m\n\033[1;33mEMPATE\033[m')


from time import sleep

parada = False # variável para parar loop while
while True:
    print('\033[1m-\033[m' * 30)
    print('\033[1mJOQUEMPÔ\033[m'.center(35))
    print('\033[1m-\033[m' * 30)
    print('[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA')
    
    while True: #loop para tratamento de erro
        try:
            escolha = int(input('\033[1m-->> \033[m')) # jogador escolhe umas das alternativas proposta
            if escolha < 1 or escolha > 3:
                print('\033[1;31mResposta inválida\033[m')
            else:
                break
        except (IndexError, ValueError):
            print('\033[1;31mResposta inválida\033[m')
    
    sleep(0.5) # time para JO... QUEM... PO...
    print('\nJO 🪨')
    sleep(0.5)
    print('QUEM 📜')
    sleep(0.5)
    print('PÔ ✂️\n')
    
    print('-' * 30)
    jqp(escolha) # função é chamada, assim mostrando o resultado do jogado de acordo com a escolha do jogador
    print('-' * 30)
    
    while True: # loop para tratamento de erro
        try:    
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if 'N' in cont: # condição para se jogador escolher 'N', assim parando o progama
                print('\033[1mObrigado por jogar!!\033[m')
                parada = True
                break
            elif 'S' in cont: # condição para se jogador escolher 'S', assim continuando jogo
                break
            else: # se jogador não responder 'S' ou 'N' entra em loop, assim perguntando novamente
                print('\033[1;31mResposta inválida\033[m')
        except IndexError:
            print('\033[1;31mResposta inválida\033[m')
        
    
    if parada == True: # condição para parar loop
        break

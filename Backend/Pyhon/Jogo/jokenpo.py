import random
from time import sleep

def jogar_jokenpo():
    placarj = 0
    placarc = 0
    
    print('Ok, vamos lá...')
    sleep(1)
    opcoes = ('tesoura','papel','pedra')

    while True:
        print('=-'*15)
        sleep(0.3)
        print('''[1] Tesoura
[2] Papel
[3] Pedra''')
        sleep(0.3)
        print('=-'*15)
        jogador = input('Qual é a sua jogada? ')
        if jogador == '1':
            jogador = 'tesoura'
        if jogador == '2':
            jogador = 'papel'
        if jogador == '3':
            jogador = 'pedra'
        while jogador not in opcoes:
            jogador = input('JOGADA INVÁLIDA! Escolha entre 1, 2 ou 3: ')
            if jogador == '1':
                jogador = 'tesoura'
            if jogador == '2':
                jogador = 'papel'
            if jogador == '3':
                jogador = 'pedra'
        computador = random.choice(opcoes)
        print('=-'*15)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!')

        print("=-"*15)
        sleep(0.5)
        print('Você escolheu: {}'.format(jogador))
        sleep(0.3)
        print('Computador escolheu: {}'.format(computador))

        print('=-'*15)
        sleep(0.5)
        if jogador == computador:
            print('Deu empate! Vamos de novo...\n')
            continue
        elif (
            (jogador == 'tesoura' and computador == 'papel') or
            (jogador == 'pedra' and computador == 'tesoura') or
            (jogador == 'papel' and computador == 'pedra')
        ):
            print('Parabéns, você ganhou!')
            placarj += 1

        else:
            print('Que pena, eu ganhei!')
            placarc += 1
        repeat = input('Quer jogar novamente? (S/N) ' ).strip().upper()
        if repeat == 'S':
            print('Ok, vamos de novo...')
            sleep(1)
            continue
        else:
            print('Que pena, te vejo em breve')
            break
    
    print('=-'*15)
    print('''Placar final ficou:
Jogador: {}
Computador: {}'''.format(placarj,placarc))
    print('=-'*15)
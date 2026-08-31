import random
from time import sleep

def jogar_advinhacao():
    placarj = 0
    placarc = 0
    opcoes = ('1','2','3','4','5','6','7','8','9','10')
    print('Ok, vamos lá...')
    sleep(1)
    print('=-'*15)
    
    while True:
        opcoes = ('1','2','3','4','5','6','7','8','9','10')
        computador = random.choice(opcoes)
        jogador = str(input('Escolha um número entre 1 e 10: ')).strip()
        print('=-'*15)
        while jogador not in ('1','2','3','4','5','6','7','8','9','10'):
            opcoes = ('1','2','3','4','5','6','7','8','9','10')
            jogador = str(input('O número só pode ser entre 1 e 10, tente novamente: ')).strip()
            print('=-'*15)
        print('Pensando...')     
        sleep(2)
        print("=-"*15)
        sleep(0.5)
        print('Você escolheu: {}'.format(jogador))
        sleep(0.3)
        print('Computador escolheu: {}'.format(computador))
        print('=-'*15)
        if jogador == computador:
            print('Parabéns, você acertou!')
            print('=-'*15)
            sleep(0.3)
            placarj += 1
        else:
            print('Que pena, eu venci!')
            print('=-'*15)
            sleep(0.3)
            placarc += 1
        repeat = input('Quer jogar novamente? (S/N) ' ).strip().upper()
        if repeat == 'S':
            print('Ok, vamos de novo...')
            sleep(0.3)
            print('=-'*15)
            sleep(1)
            continue
        elif repeat == 'N':
            print('Que pena, te vejo em breve...')
            break
        else:
            while repeat not in ('S','N'):
                repeat = input('Não entendi, tente novamente (S/N): ').strip().upper()
            if repeat == 'S':
                print('Ok, vamos de novo...')
                sleep(0.3)
                print('=-'*15)
                sleep(1)
                continue
            elif repeat == 'N':
                print('Que pena, te vejo em breve...')
                break
    print('=-'*15)
    print('''Placar final ficou:
Jogador: {}
Computador: {}'''.format(placarj,placarc))
    print('=-'*15)
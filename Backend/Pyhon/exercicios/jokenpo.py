import sys, random
resultado = []
print(f'''Olá, seja bem vindo, vamos jogar Jokenpô?
=-=-=-=-=-=-=-=-=-=-=       
[1] Pedra
[2] Papel
[3] Tesoura
[4] Para sair do jogo
=-=-=-=-=-=-=-=-=-=-=''')
while True:
    try:
        jogador = int(input('Digite um número de 1 a 4: '))
    except ValueError:
        print('ERROR')
        continue
    except (KeyboardInterrupt, EOFError):
        print('Encerrando programa...')
        sys.exit()
    if jogador < 1 or jogador > 4:
        print('ERROR')
        continue
    if jogador == 4:
        sys.exit()
    break
computador = random.randint(1,3)
print(computador)
if jogador == 1 and computador == 3:
    print('Você ganhou!')
elif jogador == 2 and computador == 1:
    print('Você ganhou!')
elif jogador == 3 and computador == 2:
    print('Você ganhou!')
elif jogador == computador:
    print('Deu empate!')
else:
    print('Você perdeu!')
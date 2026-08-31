from time import sleep
from advinhe import jogar_advinhacao
from jokenpo import jogar_jokenpo

print('=-'*15)
while True:
    sleep(0.3)
    print('O que vamos jogar hoje?')
    sleep(0.3)
    print('=-'*15)
    sleep(0.3)
    print('''[1] Advinhação
[2] Jokenpô
[3] Sair do programa''')
    sleep(0.3)
    print('=-'*15)
    escolha = str(input('')).strip()
    if escolha == '1':
        jogar_advinhacao()
    elif escolha == '2':
        jogar_jokenpo()
    elif escolha == '3':
        print('Ok, tenha um bom dia!')
        break
    else:
        print('ERROR, tente novamente')
import sys
dinheiro = 3000
saquesf = 0
depositosf = 0
def verificar_arquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except:
        a = open(arquivo, 'wt')
        a.close()
def atribuir_arquivo(arquivo):
    a = open(arquivo, 'r')
    texto = a.read().splitlines()
    return texto
def erros(msg):
    while True:
        try:
            valor1 = msg
        except ValueError:
                print('ERROR')
                continue
        except (KeyboardInterrupt, InterruptedError):
            print('Saindo do progama...')
            sys.exit()
        return valor1
verificar_arquivo('saldo.txt')
dinheiro = atribuir_arquivo('saldo.txt')
while True:
    print('''1- Ver saldo
2 - Depositar
3 - Sacar
4 - Extrato
5 - Sair ''')
    try:
        opçao = int(input('O que você quer fazer? '))
    except ValueError:
        print('ERROR')
        continue
    except (KeyboardInterrupt, InterruptedError):
        print('Saindo do programa...')
        sys.exit()
    if opçao == 1:
        print(f'Seu saldo atual é de: {dinheiro:.2f}')
    elif opçao == 2:
        deposito = erros(msg= float(input('Quanto você quer depositar na sua conta? ')))
        dinheiro += deposito
        depositosf += deposito
    elif opçao == 3:
        while True:
            saque = erros(msg= float(input('Quanto você quer sacar? ')))
            if saque > dinheiro:
                print('ERROR, você não pode sacar mais do que tem na sua conta')
                continue
            dinheiro -= saque
            saquesf += saque
            break
    elif opçao == 4:
        if depositosf > 0 and saquesf > 0:
            print(f'Você já sacou {saquesf} da sua conta, e também depositou {depositosf} na sua conta')
        elif depositosf > 0:
            print(f'Você já depoistou {depositosf} na sua conta')
        elif saquesf > 0:
            print(f'Você já sacou {saquesf} da sua conta')
        else:
            print('Você ainda não movimentou nada na sua conta')
    elif opçao == 5:
        sys.exit()
total = 0
def error(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('ERROR')
        except KeyboardInterrupt:
            print('\nEncerrando programa')
            exit()
produto = 0
print('''Lanchonete
1 - Coxinha R$ 5,00
2 - Pastel R$ 7,00
3 - Café R$ 4,00
4 - Suco R$ 6,00
5 - Sair''')
while True:
    while True:
        produto = error('O que você quer comprar? Digite o número correspondente: ')
        if produto > 5 or produto < 1:
            print('Por favor digite um  número entre 1 e 5')
            continue
        break
    if produto == 5:
        break
    elif produto == 1:
        preço = 5
    elif produto == 2:
        preço = 7
    elif produto == 3:
        preço = 4
    elif produto == 4:
        preço = 6
    while True:
        qtd = error('Quantos você quer? ')
        if qtd <= 0:
            print('Por favor, digite uma quantidade válida')
            continue
        break
    qtd *= preço
    total += qtd
print(f'O total ficou {total} reais')
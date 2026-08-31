while True:   
    try:
        valor1 =  int(input('Digite um valor: '))
    except ValueError:
        print('Por favor, digite um valor válido')
        continue
    except KeyboardInterrupt:
        print('\nPrograma Interrompido, tente novamente')
        continue
    break
while True:
    try:
        valor2 = int(input('Digite mais um valor: '))
    except ValueError:
        print('Por favor, digite um valor válido')
        continue
    except KeyboardInterrupt:
        print('\nPrograma Interrompido, tente novamente')
        continue
    if valor2 < valor1:
        print('Esse valor não pode ser menor que o primeiro valor')
        continue
    break
soma = 0
qtd = 0
for i in range (valor1, valor2 + 1, 1):
    if i % 2 == 0:
        soma += i
        qtd += 1
try:
    print(f'A média dos pares de {valor1} até {valor2} é: {soma/qtd:.0f}')
except ZeroDivisionError:
    print('Não há números pares nesse intervalo')
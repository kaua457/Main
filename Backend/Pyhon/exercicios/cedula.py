while True:
    try:
        valor = int(input('Digite um valor: '))
    except ValueError:
        print('ERROR, digite um valor válido')
        continue
    break
if valor >= 100:
    cont100 = valor// 100
    valor -= cont100 * 100
    print(f'Cédulas de 100 : {cont100}')
if valor >= 50:
    cont50 = valor// 50
    valor -= cont50 * 50
    print(f'Cédulas de 50 : {cont50}')
if valor >= 20:
    cont20 = valor// 20
    valor -= cont20 * 20
    print(f'Cédulas de 20 : {cont20}')
if valor >= 10:
    cont10 = valor// 10
    valor -= cont10 * 10
    print(f'Cédulas de 10 : {cont10}')
if valor >= 1:
    cont1 = valor
    valor -= cont1
    print(f'Cédulas de 1 : {cont1}')
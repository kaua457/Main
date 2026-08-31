#Área para definir os lados

while True:
    triangulo = input('Digite 3 medidas para formar um triângulo: ').strip().split()
    while True:
        while len(triangulo) !=3:
            triangulo = input('Por favor digite exatamente 3 números: ').strip().split()
        try:
            a = float(triangulo[0])
            b = float(triangulo[1])
            c = float(triangulo[2])
        except ValueError:
            triangulo = input('Por favor, digite somente números: ').strip().split()
            continue
        if a == 0 or b == 0 or c == 0:
            triangulo = input('Por favor, digite somente números válidos, 0 não é um número válido: ').strip().split() 
            continue
        if a > b + c or b > a + c or c > a + b:
            triangulo = input('Uma das medidas que você digitou é maior que a soma das outras duas, por favor digite 3 medidas válidas: ').strip().split()
            continue
        break

    #Definição do Triângulo

    if a == b == c:
        print('Este triângulo é equilátero')
    elif c == b or a == c or b == a:
        print('Este triângulo é isósceles')
    else:
        print('Este triângulo é escaleno')
     
    continuar = input('Deseja testar outro triângulo? [S/N] ').upper().strip()
    while True:
        if continuar == 'S':
            break
        elif continuar == 'N':
            exit()
        else:
            continuar = input('Por favor, digite somente [S/N] ').upper().strip()
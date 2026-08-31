import sys
def fatorial(n):
    resultado = n
    if n == 0:
        return 1
    while n > 1:
        n -= 1
        resultado *= n
    return resultado
while True:
    try:
        numero = int(input('Digite um número para ser calculado: '))
    except (ValueError,EOFError):
        print('ERROR')
        continue
    except KeyboardInterrupt:
        print('Encerrando')
        sys.exit()
    if numero < 0:
        print('O número não pode ser menor que 0')
        continue
    break
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')
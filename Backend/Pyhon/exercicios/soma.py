resultado = input('Digite dois números: ').strip().split()
while len(resultado) != 2:
    resultado = input('Por favor, digite exatamente 2 números: ').strip().split()
a = eval(resultado[0])
b = eval(resultado[1])
print(f'O resultado da soma dos dois números é igual a: {a+b}')
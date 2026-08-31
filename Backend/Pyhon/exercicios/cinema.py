import sys
while True:
    try:
        quantidade = int(input('Quantas pessoas? '))
    except ValueError:
        print('ERROR')
        continue
    except (KeyboardInterrupt, EOFError):
        sys.exit('\nEncerrando')
    if quantidade < 0:
        print('Digite uma quantidade válida')
        continue
    if quantidade == 0:
        print('Nenhuma pessoa cadastrada')
        sys.exit()
    break
quantidade1 = 0
idades = 0
ingresso = 0
while quantidade != quantidade1:
    try:
        idade = int(input('Qual a sua idade? '))
    except ValueError:
        print('ERROR')
        continue
    except (KeyboardInterrupt, EOFError):
        sys.exit('\nEncerrando')
    if idade < 0:
        print('Digite uma idade válida')
        continue
    if idade < 3:
        ingresso += 0
    elif idade <= 12:
        ingresso += 15
    else:
        ingresso += 30
    idades += idade
    quantidade1 += 1
media = idades // quantidade
if ingresso == 0:
    print('Ficou por conta da casa')
else:
    print(f'Ingresso para {quantidade} pessoas, o total ficou : {ingresso} reais, e a média das idades é: {media}' )
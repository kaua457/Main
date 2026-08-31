import sys
cadastro = []
total = 0
soma = 0
media = 0
m30 = 0
hamedia = 0
while True:
    try:
        encerramento = input('Deseja cadastrar alguém? [S/N] ').strip().upper()
    except (KeyboardInterrupt, EOFError):
        print('Encerrando programa...')
        sys.exit()
    if encerramento == 'N':
        break
    elif encerramento not in ('S', 'N'):
        print('ERROR')
        continue
    while True:
        try:
            nome = input('Digite seu nome: ').strip()
        except (KeyboardInterrupt, EOFError):
            print('Encerrando programa...')
            sys.exit()
        if not nome.isalpha():
            print('ERROR')
            continue
        break
    while True: 
        try:   
            idade = int(input('Digite sua idade: '))
        except ValueError:
            print('ERROR')
            continue
        except (KeyboardInterrupt, EOFError):
            print('Encerrando programa...')
            sys.exit()
        if idade < 1:
            print('ERROR')
            continue    
        break
    while True: 
        try:   
            sexo = input('Digite qual o seu sexo [M/F] ')
        except (KeyboardInterrupt, EOFError):
            print('Encerrando programa...')
            sys.exit()
        if sexo.upper() not in ('M', 'F'):
            print('ERROR')   
            continue
        break
    cadastro.append({'Nome': nome.capitalize(), 'Idade': idade, 'Sexo': sexo.upper()})
    total += 1
try:    
    for d in cadastro:
        print(f"| Nome: {d['Nome']} | Idade: {d['Idade']} | Sexo: {d['Sexo']} |")
        int(d['Idade'])
        if d['Idade'] < 30 and d['Sexo'] == 'F':
            m30 += 1
        for k, v in d.items():
            if k == 'Idade':
                int(v)
                media += v
    media /= total
except NameError:
    print('Nenhum cadastro registrado')
for d in cadastro:
    int(d['Idade'])
    if d['Idade'] > media and d['Sexo'] == 'M':
        hamedia += 1
print(f'O total de pessoas cadastradas foi: {total}')
print(f'A média das idades das pessoas cadastradas é: {media:.0f}')
print(f'A quantidade de mulheres com menos de 30 anos é: {m30}')
print(f'A quantidade de homens com idade acima da média é: {hamedia}')
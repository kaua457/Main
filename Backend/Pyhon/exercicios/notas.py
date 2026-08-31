def parametro(a,b):
    while True:
        nota = input(f'Digite a nota do {a}: ').strip()
        try:
            nota = float(nota)
        except ValueError:
            print('Valor inválido. Digite um número.')
            continue
        if nota <= b:
            break
        else:
            print('Nota inválida. Digite novamente.')
            continue
    return nota

nome = input('Digite o nome do aluno: ').capitalize().strip()
trabalho = parametro('trabalho', 2)
teste = parametro('teste',3)
prova = parametro('prova',5)
media = trabalho + teste + prova
aluno = dict()
aluno = {'nome':nome, 'media':media}
if media >= 5:
    print(f'{aluno['nome']} foi aprovado com {aluno['media']} na média')
else:
    print(f'{aluno['nome']} foi reprovado com {aluno['media']} na média')
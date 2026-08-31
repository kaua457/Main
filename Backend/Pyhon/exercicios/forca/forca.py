import sys
import random as r
import funçoes as f
f.verificar_arquivo('score.txt')
f.verificar_arquivo('palavras.txt')
texto = f.atribuir('palavras.txt')
registro = f.atribuir('score.txt')
print(registro)
palavras = []
for linha in texto:
    palavras.append(linha)
score = 0
while True:
    erros = 0
    palavra = r.choice(palavras)
    while True:
        print('='*23)
        print('     Jogo da forca')
        print('='*23)
        print('\n1-jogar')
        print('2-Score')
        print('3-Sair\n')
        print('='*23)
        try:
            escolha = int(input('Escolha uma opção: '))
        except (KeyboardInterrupt, EOFError):
            print('Encerrando programa...')
            sys.exit()
        except ValueError:
            print('ERROR')
            continue
        match escolha:
            case 1:
                encontrou = False
                palavra2 = ''
                acertos = []
                tentativas = []
                jogador = input('Quem está jogando? ').strip().capitalize()
                for l, linha in enumerate(registro):
                    jogador1, score1 = linha.split(';')
                    if jogador1 == jogador:
                        encontrou = True
                if not encontrou:
                    score = 0
                    registro.append(f'{jogador};{score}')
                score = 0
                print(palavra)
                break
            case 2:
                encontrou = False
                try:
                    jogador = input('Qual seu nome? ').strip().capitalize()
                except (KeyboardInterrupt, EOFError):
                    print('Encerrando programa...')
                    sys.exit()
                for l, linha in enumerate(registro):
                    jogador1, score1 = linha.split(';')
                    if jogador1 == jogador:
                        encontrou = True
                if encontrou:
                    print(f'Seu score atual é de {score1}')
                elif not encontrou:
                    print('Jogador ainda não registrado, jogue ao menos uma vez para ver seu score')
                continue
            case 3:
                a = open('score.txt','w')
                for l, linha in enumerate(registro):
                    a.write(f'{linha}\n')
                a.close()
                print('Saindo do programa...')
                sys.exit()
            case _:
                print('ERROR')
                continue
    while palavra2 != palavra:
        while True:
            f.desenhar_forca(erros)
            try:
                tentativa = input('Digite uma letra: ').strip()
            except (KeyboardInterrupt, EOFError):
                print('Encerrando programa...')
                sys.exit()
            if len(tentativa) > 1 or len(tentativa) < 1 or not tentativa.isalpha():
                print('ERROR')
            elif tentativa in tentativas:
                print('Você já digitou essa letra')
            elif tentativa in palavra:
                acertos.append(tentativa.lower())
                tentativas.append(tentativa.lower())
            elif tentativa not in palavra:
                erros += 1
                tentativas.append(tentativa.lower())
                print('VOCÊ ERROU')
            break
        if erros >= 7:
            print(f'A palavra era {palavra}, mais sorte na próxima vez')
            break
        palavra2 = ''
        for letra in palavra:
            if letra in acertos:
                palavra2 += letra
            else:
                palavra2 +='_'
        if palavra2 != palavra:
            print(palavra2)
    match erros:
        case 0:
            score += 1000
        case 1:
            score += 900
        case 2:
            score += 800
        case 3:
            score += 700
        case 4:
            score += 600
        case 5:
            score += 500
        case 6:
            score += 300
    for l, linha in enumerate(registro):
        jogador1, score1 = linha.split(';')
        score1 = int(score1)
        if jogador1 == jogador:
            score1 += score
        registro[l] = (f'{jogador1};{score1}')
    print(registro)
    print(f'Parabéns, você acertou! A palavra era {palavra}')
    print(f'Seu score foi de: {score}')
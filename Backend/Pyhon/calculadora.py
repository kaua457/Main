expressao = input('Digite uma expressão: ').strip()
expressao = expressao.replace('x', '*').replace('^', '**')

while True:
    try:
        resultado = eval(expressao)
        resultado = f'{resultado}'.replace('.',',')
        print(f'O resultado deu: {resultado}')
        break
    #Erros
    except SyntaxError:
        expressao = input('Expressão inválida. Digite novamente: ').strip()
        expressao = expressao.replace('x', '*').replace('^', '**')
    except ZeroDivisionError:
        print('Resultado indeterminado')
        break
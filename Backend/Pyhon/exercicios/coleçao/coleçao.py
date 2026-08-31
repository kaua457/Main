import sys
def verificar(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True
def criar(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close
    except:
        print('Erro de criação do arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso')
def cadastrar(arquivo, njogo, nplataforma):
    try:
        a = open(arquivo, 'at')
    except:
        print('Error')
    else:
        a.write(f'{nplataforma}: {njogo}\n')
    finally:
        a.close()
def listar():
    try:
        a = open(arquivo, 'rt')
    except:
        print('Error')
    else:
        print(a.read())
    finally:
        a.close()
arquivo = 'coleçao.txt'
if verificar(arquivo):
    print('Arquivo local encontrado')
else:
    print('Criando arquivo...')
    criar(arquivo)
while True:
    print('''[1] Cadastrar novo jogo
[2] Mostrar coleção
[3] Sair''')
    while True:
        try:
            opçao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Por favor, digite um número de 1 a 3')
            continue
        except (KeyboardInterrupt, EOFError):
            print('Encerrando...')
            sys.exit()
        if opçao > 3 or opçao < 1:
            print('Por favor digite um número entre 1 e 3')
        if opçao == 1:
            njogo = input('Digite o nome do jogo: ').capitalize().strip()
            nplataforma = input('Digite o nome da plataforma do jogo: ').capitalize().strip()
            cadastrar(arquivo, njogo, nplataforma) 
        if opçao == 2:
            listar()
        if opçao == 3:
            sys.exit()
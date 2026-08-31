def verificar_arquivo(arquivo):
    try:
        a = open(arquivo,'rt')
    except:
        a = open(arquivo,'wt+')
        a.close()

def atribuir(arquivo):
    a = open(arquivo, 'r')
    texto = a.read()
    return texto.splitlines()

def desenhar_forca(erros):     
    print("X==:==")
    print("X  :  ")
    if erros >= 1:
        print('X  O  ')
    else:
        print('X')
    linha2 = ""

    if erros == 2:
        linha2 = r"  | "

    elif erros == 3:
        linha2 = r" /| "

    elif erros >= 4:
        linha2 = r" /|\ "

    print(f"X{linha2}")
    linha3 = ""

    if erros == 5:
        linha3 += r" / "
    elif erros >= 6:
        linha3 += r" / \ "

    print(f"X{linha3}")
    print(f"X\n=======")
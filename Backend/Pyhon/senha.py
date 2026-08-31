while True:
    senha = input('Digite uma senha: ').strip()

    #Verificando cada digito da senha
    numero = any(c.isdigit() for c in senha)
    maiuscula = any(c.isupper() for c in senha)
    minuscula = any(c.islower() for c in senha)
    simbolo = any(not c.isalnum() for c in senha)

    #Verificando se a senha é forte ou fraca
    if len(senha) >=8 and numero and maiuscula and minuscula and simbolo:
        print('Senha forte')
        break
    else:
        print('Senha fraca')
        while True:
            continuar = input('Deseja tentar fazer uma senha mais forte? ').upper().strip()
            if continuar == 'S':
                break
            elif continuar == 'N':
                break
            else:
                print('Por favor digite somente [S/N]')
        if continuar == 'N':
            break
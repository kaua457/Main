while True:
    senha = input('Digite uma senha: ').strip()

    #Verificando cada digito da senha
    numero = any(c.isdigit() for c in senha)
    maiuscula = any(c.isupper() for c in senha)
    minuscula = any(c.islower() for c in senha)
    simbolo = any(not c.isalnum() for c in senha)

    #Verificando se a senha é forte ou fraca
    if len(senha) < 8:
        print('A senha precisa ter no mínimo 8 dígitos')
        continue
    elif numero == False:
        print('A senha precisa ter um número')
        continue
    elif maiuscula == False:
        print('A senha precisa ter uma letra maiúscula')
        continue
    elif minuscula == False:
        print('A senha precisa ter uma letra minúsucla')
        continue
    elif simbolo == False:
        print('A senha precisa ter um símbolo')
        continue
    elif '314' not in senha:
        print('A senha precisa ter os primeiros números do número PI')
        continue
    elif '2026' not in senha:
        print('A senha precisa ter o ano em que o Brasil ganhou o Hexa')
        continue
    elif 'A' and 'E' and 'I' and 'O' and 'U' not in senha:
        print('A senha precisa ter todas as vogais maiúsculas')
        continue
    elif '+55' not in senha:
        print('A senha precisa ter o código de telefone do seu país')
        continue
    elif str(len(senha)) not in senha:
        print('A senha precisa ter o número de caracteres da senha')
        continue
    elif len(senha) > 30:
        print('A senha precisa ter no máximo 30 dígitos')
        continue
    break
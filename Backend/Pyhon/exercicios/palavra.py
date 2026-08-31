palavras = ('Zelda', 'Link', 'Urbosa', 'Daruk', 'Ganondorf', 'Mario', 'Luigi')
for p in palavras:
    print(f'\nA palavra {p} tem as seguintes vogais:', end=' ')
    for v in p:
        if v.upper() in 'AEIOU':
            print(v.upper(), end=' ')
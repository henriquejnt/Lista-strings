palavra = 'Papagaio'.upper()

letras_da_palavra_certa = set(palavra)
letras_usadas = set()
erros = 0
while not letras_da_palavra_certa.issubset(letras_usadas):
    print()
    print()
    usuario = input('Digite uma letra: ').upper()
    letras_usadas.add(usuario)
    if usuario in letras_da_palavra_certa:
        print('A palavra é ',end='')
        for letra in palavra:
            if letra in letras_usadas:
                print(f'{letra}', end='')
            else:
                print('_ ',end='')
    else:
        erros += 1
        print(f'-> Você errou pela {erros}° pela vez')
        if erros == 6:
            print('Você perdeu!')
            break
    print()
    print(f"Letras usadas: {letras_usadas}")
print('Você acertou, parabéns !')





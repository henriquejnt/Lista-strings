#Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras
#  embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
#  O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, 
# informando se o usuário ganhou ou perdeu o jogo.

palavra = 'AYRTON SENNA'
lista_palavras_digitadas = []
embaralha = palavra[::-1]
erros = 0
while True:
    print(f'Tente adivinha esse nome embaralhado: {embaralha}')
    palpites = input('Digite seu palpite: ').upper()
    lista_palavras_digitadas.append(palpites)
    if palavra not in lista_palavras_digitadas:
        erros +=1
        print(f'Você errou pela {erros}° vez!') 
        if erros == 6:
            print("Você perdeu!")
            break
    else:
        print(f"Você acertou, {palavra} é a palavra certa!")
        break
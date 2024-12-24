#. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#Altere o programa anterior de modo que a escada seja invertida.
def nome_vertical (n):
    print("=-"*20)
    for palavra in n:
        print(palavra)

def nome_escada(n):
    print("=-"*20)
    lista = list(n)
    contador = 1
    for palavra in range(len(lista)):
        print(lista[:contador])
        contador += 1

def nome_escada_invertida (inverte):
    print("=-"*20)
    lista = list(inverte)
    contador = len(lista)
    for palavra in range(len(lista)):
        print(lista[:contador])
        contador -= 1


nome = input('Digite seu nome: ')
print('Na vertical: ')
nome_vertical(nome)
print('Em escada: ')
nome_escada(nome)
print('Em escada invertida: ')
nome_escada_invertida(nome)

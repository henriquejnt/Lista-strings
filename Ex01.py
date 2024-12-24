string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'
print(f'Tamanho de "{string1}": {len(string1)} caracteres')
print(f'Tamanho de "{string2}": {len(string2)} caracteres')
if len(string1) == len(string2):
    print('As strings tem caracteres iguais')
elif string1 == string2:
    print('Strings com tamanhos iguais.')
elif string1 != string2:
    print('Strings com tamanhos dieferesntes')
else:
    print('Strings com caractteres diferenyes')

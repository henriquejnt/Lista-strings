#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e 
# imprima a data com o nome do mês por extenso.
#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.


data = input('Data de nascimento: ')
dia = (data[:2])
mes = (data[3:5])
ano = (data[6:10])
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
if mes == '01':
    print(f'Você nasceu em {dia} de {meses[0]} de {ano}.')
elif mes == '02':
    print(f'Você nasceu em {dia} de {meses[1]} de {ano}.')
elif mes == '03':
    print(f'Você nasceu em {dia} de {meses[2]} de {ano}.')
elif mes == '04':
    print(f'Você nasceu em {dia} de {meses[3]} de {ano}.')
elif mes == '05':
    print(f'Você nasceu em {dia} de {meses[4]} de {ano}.')
elif mes == '06':
    print(f'Você nasceu em {dia} de {meses[5]} de {ano}.')
elif mes == '07':
    print(f'Você nasceu em {dia} de {meses[6]} de {ano}.')
elif mes == '08':
    print(f'Você nasceu em {dia} de {meses[7]} de {ano}.')
elif mes == '09':
    print(f'Você nasceu em {dia} de {meses[8]} de {ano}.')
elif mes == '10':
    print(f'Você nasceu em {dia} de {meses[9]} de {ano}.')
elif mes == '11':
    print(f'Você nasceu em {dia} de {meses[10]} de {ano}.')
else:
    print('Esse mês não existe !')
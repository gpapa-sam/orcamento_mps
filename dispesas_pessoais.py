ano = [{'salario': {1: 17785.91},
        'nomad': {5: 1000, 8: 1001},
       'condominio': {8: 455},
        'mei': {17: 72}}]

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
         'outubro', 'novembro', 'dezembro']

print(f'mês de {meses[0]}')
print()
print(f'gasto\t\t\t\tdia\t\tvalor(R$)')
for mes in ano:
    for gasto, valor in mes.items():
        #print(gasto, '-', valor)
        for key, value in valor.items():
            #print(gasto, '\t\t\t', key, '\t', value)
            print(f'{gasto:<10} {key:>12} \t {value}')

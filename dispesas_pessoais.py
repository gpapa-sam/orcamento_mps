from csv import DictReader, reader


ano = [[], [], [], [], [], [], [], [], [], [], [],[]]

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
         'outubro', 'novembro', 'dezembro']

"""
print(f'mês de {meses[0]}')
print()
print(f'gasto\t\t\t\tdia\t\tvalor(R$)')
for mes in ano:
    for gasto, valor in mes.items():
        #print(gasto, '-', valor)
        for key, value in valor.items():
            #print(gasto, '\t\t\t', key, '\t', value)
            print(f'{gasto:<10} {key:>12} \t {value}')


with open("orc_23.csv") as arquivo:
    mes = DictReader(arquivo, delimiter=',')
    for dia in mes:

        #print(f"{dia['data']} - {dia['objeto']} - {dia['valor']}")
        print(dia)

"""
with open('orc_23.csv') as arquivo:
    leitor_csv = reader(arquivo)
    #next(leitor_csv)  # Pular o cabeçalho
    for indice, linha in enumerate(leitor_csv):

        m = []
        for i, x in enumerate(linha):

            m.append(linha[i])
            if (i+1) % 3 == 0:
                if indice == 0:
                    #z = list
                    #z.append(m)
                    ano[i//3].append(m)
                    m = []
                    print(ano)
                else:
                    ano[i//3].append(m)
                    m = []



print(ano)
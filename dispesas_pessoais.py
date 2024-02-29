from csv import DictReader, reader, writer


ano = [[], [], [], [], [], [], [], [], [], [], [],[]]

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
         'outubro', 'novembro', 'dezembro']

"""



with open('orc_23.csv') as arquivo:
    leitor_csv = reader(arquivo) # cada linha é uma lista

    for indice, linha in enumerate(leitor_csv):

        m = [] # uma lista temporária
        # aqui faz o loop de cada linha do arquivo que tem 36 argumento(3 por mês) contabilizando um ano
        for i, x in enumerate(linha):

            m.append(linha[i])
            if (i+1) % 3 == 0: #inicio de cada mês ( a cada 3 campos)
                if indice == 0: #somente se for a primeira linha
                    #z = list
                    #z.append(m)
                    ano[i//3].append(m)
                    m = []
                    #print(ano)
                else:
                    ano[i//3].append(m)
                    m = []



print(ano)
print(f'mês de {meses[0]}')
print()
print(f'data\t\t\t{"gasto":<30} valor(R$)')
print()
for gasto in ano[0]:
    print(f'{gasto[0]}\t\t{gasto[1]:<30} {gasto[2]:>15}')
"""
#escrevendo os dados em arquivo csv
with open('janeiro.csv', 'a') as file:
    escritor_csv = writer(file)
    sair = None
    #escritor_csv.writerow(['data', 'gasto', 'valor'])
    while sair != 's':
        data = input('informe a dia do gasto : ') + '/jan.'
        gasto = input('informe a descrição do gasto: ')
        valor = float(input('informe  o valor do gasto: '))
        sair = input('deseja continuar? (s/n): ')
        escritor_csv.writerow([data, gasto, valor])



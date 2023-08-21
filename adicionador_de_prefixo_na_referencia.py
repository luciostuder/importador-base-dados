import csv

# dados de entrada 

print('este programa insere um prefixo em todas as referencias do ficheiro do fornecedor VT')
prefixo = input("indique o prefixo: ")
ficheiro = input("indique o nome do ficheiro (sem '.csv'):")

# processamento


# 1. leitura do ficheiro
f = open(ficheiro + '.csv')
linhas = list(csv.reader(f, delimiter=';'))
f.close()

# 2. atualização das referencias
quantidade_de_linhas = len(linhas) 

for i in range(1, quantidade_de_linhas):
    linhas[i][1] = prefixo + linhas[i][1]

# criação de novo ficheiro com prefixos
f = open(ficheiro + '_com_prefixo.csv', 'w')
for linha in linhas:
    f.write(';'.join(linha))
    f.write('\n')
f.close()
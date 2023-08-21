import csv

f_om = input("indique o nome do ficheiro CSV da OM (sem 'csv'): ")
f_input = input("indique o nome do ficheiro CSV do fornecedor (sem 'csv'): ")

while True:
    try:
        coluna = int(input("indique em que coluna do ficheiro CSV do fornecedor está a referencia (1ª coluna: 1, 2ª coluna: 2, 3ª coluna: 3, ...): "))
        break
    except:
        pass

prefixo = input("Indique o prefixo da referencia: ")

with open(f_om + '.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    
    dic_refs = {}

    for i, line in enumerate(reader):
        if i != 0 and line[2] != '':
            dic_refs[line[2]] = line[0] 


with open(f_input + '.csv') as f:
    reader = csv.reader(f, delimiter=';')
    
    output = []
    for i, line in enumerate(reader):

        if i == 0:
            output.append('handler;' + ';'.join(line))

    
        elif line[coluna-1] in dic_refs:
            
            ref = line[coluna-1][len(prefixo):]

            output.append(f'{dic_refs[ref]};' + ';'.join(line))

with open(f_input + '_filtrado.csv', 'w') as f:
    for l in output:
        f.write(l)
        f.write('\n')
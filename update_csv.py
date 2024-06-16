import csv

with open('Employee_Salaries.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')

# Ler os dados do arquivo
    for linha in arquivo_csv:
        print(linha)
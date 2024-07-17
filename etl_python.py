import csv

def read_csv_case_1(file):
    f = open(file, 'r', encoding='utf-8')

    leitor = csv.reader(f, delimiter=";", lineterminator="\n")

    data = []

    for linha in leitor:
        data.append(linha)

    f.close()

    return data


def read_csv_case_2(file):

    with open(file, 'r', encoding='utf-8') as f:

        data = [linha for linha in csv.reader(f, delimiter=';', lineterminator='\n')]

    return data


def read_data(data):
    for row in data:
        print(row)

# transformar colunas para os tipos corretos:

def tranform_data(data,specific_columns,type):
    lista_index = list()

    for coluna in data[0]:
        if coluna in specific_columns:
            lista_index.append(data[0].index(coluna))

    if type == 'float':
        for linha in range(len(data)):
            for index in lista_index:
                if (linha != 0):
                    data[linha][index] = float(data[linha][index])

    if type == 'int':
        for linha in range(len(data)):
            for index in lista_index:
                if (linha != 0):
                    data[linha][index] = int(data[linha][index])

    return data

def media_notes_students(data,specific_columns_notes,media_column_name):

    index_coluna_notas = [data[0].index(index_coluna) for index_coluna in specific_columns_notes]

    data[0].append(media_column_name)

    for i,linha in enumerate(data):
        if(i >= 1):
            soma = sum([linha[indice] for indice in index_coluna_notas])
            media = soma / len(index_coluna_notas)
            data[i].append(media)

    return data
    

def main():
    file = 'data/alunos.csv'
    specific_columns_float = ['Prova_1', 'Prova_2', 'Prova_3', 'Prova_4']
    specific_columns_int = ['RA', 'Frequencia']
    specific_columns_notes = ['Prova_1', 'Prova_2', 'Prova_3', 'Prova_4']
    media_column_name = 'Média'

    data = read_csv_case_2(file)
    read_data(data)

    data = tranform_data(data,specific_columns_float,'float')
    data = tranform_data(data,specific_columns_int,'int')
    media_notes_students(data,specific_columns_notes,media_column_name)


    read_data(data)



if __name__ == '__main__':
    main()
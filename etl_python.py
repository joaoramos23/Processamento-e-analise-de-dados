import csv
from openpyxl import Workbook

def read_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [linha for linha in csv.reader(f, delimiter=';', lineterminator='\n')]


def print_data(data):
    for row in data:
        print(row)


def transform_data(data, columns):
    col_indices = [data[0].index(col) for col in columns.keys()]

    for row in data[1:]:
        for index in col_indices:
            row[index] = columns[data[0][index]](row[index])

    return data


def add_media_column(data, columns, new_col_name):

    col_indices = [data[0].index(col) for col in columns]
    data[0].append(new_col_name)

    for row in data[1:]:
        media = sum(row[index] for index in col_indices) / len(col_indices)
        row.append(media)

    return data


def add_absences_column(data, columns, new_col_name, max_frequency):

    col_index = data[0].index(columns)
    data[0].append(new_col_name)

    for row in data[1:]:
        absences = max_frequency - row[col_index]
        row.append(absences)

    return data


def add_approval_status(data, media_col, absences_col, new_col_name, max_absences, min_media):

    media_index = data[0].index(media_col)
    absences_index = data[0].index(absences_col)
    data[0].append(new_col_name)

    for row in data[1:]:
        approved = row[media_index] >= min_media and row[absences_index] <= max_absences
        row.append('Aprovado' if approved else 'Reprovado')

    return data

def save_to_xlsx(data, file):
    wb = Workbook()
    ws = wb.active
    
    for row in data:
        ws.append(row)
    
    wb.save(file)


def main():
    file = 'data/alunos.csv'
    output_file = 'alunos_editados.xlsx'
    
    columns_transform = {'Prova_1': float, 'Prova_2': float, 'Prova_3': float, 'Prova_4': float, 'RA': int, 'Frequencia': int}
    columns_notes = ['Prova_1', 'Prova_2', 'Prova_3', 'Prova_4']
    frequency_col = 'Frequencia'
    media_col = 'Média'
    absences_col = 'Faltas'
    approval_col = 'Status Aprovação'
    max_frequency = 20
    max_absences = 5
    min_media = 7

    data = read_csv(file)
    data = transform_data(data, columns_transform)
    data = add_media_column(data, columns_notes, media_col)
    data = add_absences_column(data, frequency_col, absences_col, max_frequency)
    data = add_approval_status(data, media_col, absences_col, approval_col, max_absences, min_media)

    save_to_xlsx(data, output_file)
    print(f"Os dados foram transformados e salvos em {output_file}")

if __name__ == '__main__':
    main()

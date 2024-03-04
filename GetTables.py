import re

import pdfplumber
from PyPDF2 import PdfReader


def extract_table(path):
    pdf = pdfplumber.open(path)

    table = {}
    for page in pdf.pages:
        table[page] = page.extract_tables()

    return table

def table_converter(table):
    table_string = ''
    result = 0.0
    # Итеративно обходим каждую строку в таблице
    for row_num in range(len(table)):
        row = table[row_num]
        print(row[1])

        pattern = r'^(0|\d{1,3}( \d{3})*(,\d{2})?)$'
        goal = row[3]
        if re.match(pattern, str(goal)):
            number_string = goal.replace(" ", "").replace(",", ".")
            x = float(number_string)
            result += x
            print(x)
        # Удаляем разрыв строки из текста с переносом
        cleaned_row = [item.replace('\n', ' ') if item is not None and '\n' in item else 'None' if item is None else item for item in row]
        # Преобразуем таблицу в строку
        table_string+=('|'+'|'.join(cleaned_row)+'|'+'\n')
    # Удаляем последний разрыв строки
    table_string = table_string[:-1]
    return result
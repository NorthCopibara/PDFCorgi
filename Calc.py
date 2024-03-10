import re

import pdfplumber

from FindYesIndexes import find_yes


def extract_table(pdf_path, page_num, table_num):
    pdf = pdfplumber.open(pdf_path)

    table_page = pdf.pages[page_num]

    table = table_page.extract_tables()[table_num]

    return table

def clac_table(file_path, target):
    pdf = pdfplumber.open(file_path)
    table_page = pdf.pages[target.page_id]
    table = table_page.extract_tables()[target.table_id]

    table_string = ''
    result = 0.0

    row_id = -1
    for row_num in range(len(table)):
        row = table[row_num]

        if row_id != -1:
            check_result = find_yes(file_path, target.get_index(row_num - 1))
            if not check_result:
                continue

        if row_id == -1:
            for j in range(len(row)):
                if row[j] == 'Цена, руб.':
                    row_id = j
                    break

        goal = row[row_id]
        pattern = r'^(0|\d{1,3}( \d{3})*(,\d{2})?)$'
        if re.match(pattern, str(goal)):
            number_string = goal.replace(" ", "").replace(",", ".")
            x = float(number_string)
            result += x

    return result
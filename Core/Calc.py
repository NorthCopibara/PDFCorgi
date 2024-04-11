import re

from Core.FindYesIndexes import find_yes

column_name = 'Цена, руб.'
pattern = r'^(0|\d{1,3}( \d{3})*(,\d{2})?)$'

last_row = 0
additional_row = 0

def clac_table(pdf_file, pdf_reader, target):
    global last_row, additional_row
    table_page = pdf_file.pages[target.page_id]
    table = table_page.extract_tables()[target.table_id]

    result: float = 0.0

    row_id = -1
    for row_num in range(len(table)):
        row = table[row_num]

        if row_id != -1:
            if row_num - 1 >= len(target.indexes):
                continue

            check_result = find_yes(pdf_reader, target.get_index(row_num - 1 + additional_row))
            if not check_result:
                continue

        if row_id == -1:
            for j in range(len(row)):
                if row[j] == column_name:
                    row_id = j
                    last_row = j
                    additional_row = 0
                    break
            if row_id == -1:
                row_id = last_row
                additional_row = 1
            else:
                continue

        cell = row[row_id]
        if re.match(pattern, str(cell)):
            result += float(cell.replace(" ", "").replace(",", "."))

    return result
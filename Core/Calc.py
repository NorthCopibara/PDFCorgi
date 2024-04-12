import re

from Core.FindYesIndexes import find_yes

column_name = 'Цена, руб.'
column_name_ros = 'Цена розн., руб.'
pattern = r'^(0|\d{1,3}( \d{3})*(,\d{2})?)$'

last_column_id = 0
additional_column = 0


def clac_table(pdf_file, pdf_reader, target):
    global last_column_id, additional_column
    result: float = 0.0

    if target.page_id >= len(pdf_file.pages):
        print('Page not found {}'.format(target.page_id + 1))

    table_page = pdf_file.pages[target.page_id]

    if target.table_id >= len(table_page.extract_tables()):
        print('Table {} not found on the page {}'.format(target.table_id + 1, target.page_id + 1))
        return result

    table = table_page.extract_tables()[target.table_id]

    column_id = -1
    start_row_id = 0
    for row_num in range(len(table)):
        row = table[row_num]
        if column_id == -1:
            for column_num in range(len(row)):
                if row[column_num] == column_name or row[column_num] == column_name_ros:
                    column_id = column_num
                    last_column_id = column_num
                    additional_column = 0
                    start_row_id = row_num
                    break

        if column_id != -1:
            break

    if column_id == -1:
        column_id = last_column_id
        additional_column = 1

    if column_id == -1:
        return result

    for row_num in range(start_row_id, len(table)):
        row = table[row_num]

        if row_num - 1 - start_row_id >= len(target.indexes):
            continue

        index = target.get_index(row_num - 1 + additional_column - start_row_id)
        if index == -1:
            print('Index {} not found on the row {}, additional_row {}, table {}, page {}'.format(index, row_num - start_row_id,
                                                                                                  additional_column,
                                                                                                  target.table_id + 1,
                                                                                                  target.page_id + 1))
            continue

        check_result = find_yes(pdf_reader, index)
        if not check_result:
            continue

        cell = row[column_id]
        if re.match(pattern, str(cell)):
            result += float(cell.replace(" ", "").replace(",", "."))

    return result

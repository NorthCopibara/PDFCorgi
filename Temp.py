import PyPDF2
import pdfplumber
import re

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject

file_path = "TargetPdf.pdf"
pdf = open(file_path, 'rb')
reader = PdfFileReader(pdf)

info = reader.metadata

def extract_form_value(path):
    with open(path, 'rb') as file:
        if not reader.get_fields():
            return

        print(reader.get_fields())

        form_fields = reader.get_fields()
        field_values = {}

        for field_name, field_data in form_fields.items():
            field_values[field_name] = field_data.get('/V', None)

        return field_values

form_values = extract_form_value(file_path)

'''
for field, value in form_values.items():
    print(f"Field name: {field}, value: {value}")
'''

'''
pdf_file = open(file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

page_texts = []
for i in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(i)
    page_text = page.extractText().strip()

    for line_text in page_text.splitlines():
        text = '1'
        text = line_text
        if text.isdigit():
            page_texts.append(text)

all_text = "\n".join(page_texts)
print(all_text)
pdf_file.close()
'''

def updateCheckboxValues(page, fields):
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in fields:
            if writer_annot.get('/T') == field:
                writer_annot.update({
                    NameObject("/V"): NameObject(fields[field]),
                    NameObject("/AS"): NameObject(fields[field])
                })


def extract_table(pdf_path, page_num, table_num):
    pdf = pdfplumber.open(pdf_path)

    table_page = pdf.pages[page_num]

    form701 = PdfFileReader(file_path)

    page = form701.getPage(6)
    updateCheckboxValues(page, form701.getFields())

    table = table_page.extract_tables()[table_num]

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

table_test = extract_table(file_path, 6, 2)
result = table_converter(table_test)
print('_________')
print(result)
print('_________')

number_string = "-"
# Удалить пробелы и заменить запятую на точку
pattern = r'^(0|\d{1,3}( \d{3})*(,\d{2})?)$'
if re.match(pattern, number_string):
    number_string = number_string.replace(" ", "").replace(",", ".")
    number_float = float(number_string)
    print(number_float)
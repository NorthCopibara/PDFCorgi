from PyPDF2 import PdfFileReader

from ClearCheckboxes import remove_all_checkboxes
from FindYesIndexes import find_yes
from GetTables import extract_table

file_path = "TargetPdf.pdf"
remove_all_checkboxes(file_path, '/Yes')

#result = find_yes(file_path)

#result = extract_table(file_path)

#print(result)

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
print(form_values)

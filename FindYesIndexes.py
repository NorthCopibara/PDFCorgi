import PyPDF2
from PyPDF2 import PdfReader


def find_yes(path):
    try:
        pdfFileObj = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        form_fields = pdfReader.getFields()
        field_values = {}
        if not form_fields:
            return field_values

        for field_name, field_data in form_fields.items():
            field_values[field_name] = field_data.get('/V', "/Yes")
    except FileNotFoundError:
        print("error")

    return field_values
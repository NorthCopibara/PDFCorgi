import PyPDF2
from PyPDF2 import PdfReader


def find_yes(path, id_box):
    try:
        pdfFileObj = open(path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        form_fields = pdfReader.getFields()
        result = False
        if not form_fields:
            return result

        for field_name, field_data in form_fields.items():
            if field_name == 'Check Box ' + str(id_box):
                if field_data.get('/V') == "/Yes":
                    result = True
    except FileNotFoundError:
        print("error")

    return result
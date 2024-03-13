import PyPDF2

check_box_mask = 'Check Box '

def find_yes(path, id_box):
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    form_fields = pdfReader.getFields()
    for field_name, field_data in form_fields.items():
        if field_name == check_box_mask + str(id_box) and field_data.get('/V') == "/Yes":
            return True
    return False
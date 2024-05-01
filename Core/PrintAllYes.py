import PyPDF2

check_box_mask = 'Check Box '

def print_all_yes(path):
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    form_fields = pdfReader.getFields()
    for field_name, field_data in form_fields.items():
        if check_box_mask in field_name and field_data.get('/V') == "/Yes":
            print(field_name.replace(check_box_mask, ""))

    pdfFileObj.close()
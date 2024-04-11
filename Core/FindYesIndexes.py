check_box_mask = 'Check Box '

def find_yes(pdf_reader, id_box):
    form_fields = pdf_reader.getFields()
    for field_name, field_data in form_fields.items():
        if field_name == check_box_mask + str(id_box) and field_data.get('/V') == "/Yes":
            return True
    return False
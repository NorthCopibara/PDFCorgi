
check_box_mask = 'Check Box '

def get_all_yes(pdf_reader):
    result_arr = []
    form_fields = pdf_reader.getFields()
    for field_name, field_data in form_fields.items():
        if check_box_mask in field_name and field_data.get('/V') == "/Yes":
            result_arr.append(field_name.replace(check_box_mask, ""))

    return result_arr


def clac_table(pdf_reader, targets):
    yes_indexes = get_all_yes(pdf_reader)
    result = 0
    for yes_index in yes_indexes:
        for target in targets:
            if yes_index == str(target.index):
                result += target.price

    return result

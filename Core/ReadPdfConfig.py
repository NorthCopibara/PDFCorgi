import csv

from Core.TargetData import Target

def comma_separated_int_list_to_number_list(string):
    return list(map(int, string.split(",")))

def get_pdf_config(config_path):
    rows = []
    targets = []

    with open(config_path, 'r') as csvfile:
        for row in csv.reader(csvfile):
            rows.append(row)

    for row in rows[1:]:
        if row[3] == "-" or row[3] == '':
            target = Target(int(row[0]) - 1, int(row[1]) - 1, comma_separated_int_list_to_number_list(row[2]))
            targets.append(target)
        else:
            indexes = []
            for i in range(int(row[2]), int(row[3]) + 1):
                indexes.append(i)
            target = Target(int(row[0]) - 1, int(row[1]) - 1, indexes)
            targets.append(target)

    return targets
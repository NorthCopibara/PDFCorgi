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
        target = Target(int(row[0]), int(row[1]))
        targets.append(target)

    return targets
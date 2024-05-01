import timeit

import PyPDF2

from Core.Calc import clac_table
from Core.ReadPdfConfig import get_pdf_config
from Resources import Config

target_line = 'Артикул: '
target_line_2 = 'Артикулы: '


def get_info_by_file(path):
    reader = PyPDF2.PdfFileReader(path)

    configs = Config.get_configs()

    lines = reader.pages[0].extractText().split('\n')
    articul = ''
    for text in lines:
        if (target_line in text):
            text.replace(' ', '')
            print(text.replace(target_line, ''))
            articul = text.replace(target_line, '')
            break

        if target_line_2 in text:
            result = text.replace(target_line_2, '')
            result = result.replace(' ', '')
            print(result.replace(';', ''))
            articul = result.replace(';', '')
            break

    if articul != '':
        for config in configs:
            if config.articul == articul:
                return config


def calculate(path_text):
    config = get_info_by_file(path_text)
    targets = get_pdf_config(config.path)

    calc_result = 0.0

    start_time = timeit.default_timer()

    ##---Open---
    path = ''
    if path_text == '':
        return 'Пустой путь'
    else:
        path = path_text
    pdf_obj = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
    ##---Open---

    ##---Operate---
    calc_result = clac_table(pdf_reader, targets)
    ##---Operate---

    ##---Close---
    pdf_obj.close()
    ##---Close---

    end_time = timeit.default_timer()

    ##---DrawResult---
    print("Result: ", calc_result)

    print("Time: ", end_time - start_time)
    ##---DrawResult---

    return calc_result

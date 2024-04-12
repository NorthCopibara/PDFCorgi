import asyncio
import timeit

import PyPDF2
import pdfplumber

from Core.Calc import clac_table
from Core.ReadPdfConfig import get_pdf_config
from Resources.Config import PDF_CONFIG_PATH, PDF_CONFIG_PATH_AVANGARD_4


def calculate(path_text):
    ##TODO: get file path
    targets = get_pdf_config(PDF_CONFIG_PATH_AVANGARD_4)

    calc_result = 0.0

    start_time = timeit.default_timer()

    ##---Open---
    path = ''
    if path_text == '':
        return 'Пустой путь'
    else:
        path = path_text
    pdf_file = pdfplumber.open(path)
    pdf_obj = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
    ##---Open---

    ##---Operate---
    for target in targets:
        calc_result += clac_table(pdf_file, pdf_reader, target)
    ##---Operate---

    ##---Close---
    pdf_file.close()
    pdf_obj.close()
    ##---Close---

    end_time = timeit.default_timer()

    ##---DrawResult---
    ##TODO: view result
    print("Result: ", calc_result)

    print("Time: ", end_time - start_time)
    ##---DrawResult---

    return calc_result

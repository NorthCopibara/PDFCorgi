from Core.Calc import clac_table
from Core.ReadPdfConfig import get_pdf_config
from Resources.Config import MAIN_PATH, PDF_CONFIG_PATH

targets = get_pdf_config(PDF_CONFIG_PATH)

calc_result = 0.0

for target in targets:
    calc_result += clac_table(MAIN_PATH, target)

print(calc_result)
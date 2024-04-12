import PyPDF2

from Resources.Config import MAIN_PATH

path_1 = 'C:\\Users\\PC\\Downloads\\Telegram Desktop\\Motus_2_CS_2024_retail.pdf'
path_2 = 'C:\\Users\\PC\\Downloads\\Telegram Desktop\\Avantgarde_4_2024_retail.pdf'
path_3 = 'C:\\Users\\PC\\PycharmProjects\\PDFCorgi\Resources\\Test.pdf'

target_line = 'Артикул: '
target_line_2 = 'Артикулы: '

with open(path_2, 'rb') as file:
    reader = PyPDF2.PdfFileReader(path_2)

    lines = reader.pages[0].extractText().split('\n')
    for text in lines:
        if (target_line in text):
            text.replace(' ', '')
            print(text.replace(target_line, ''))

        if target_line_2 in text:
            result = text.replace(target_line_2, '')
            result = result.replace(' ', '')
            print(result.replace(';', ''))

from turtle import fd

from tkinter import filedialog as fd
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

from PyQt6 import uic

from Main import CalculateSumm
from Save.SaveLoadLastFilePath import LoadPath, SavePath


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('CalcUI.ui', self)

        self.path_text.setText(LoadPath())
        if self.path_text.text() != '':
            config = CalculateSumm.get_info_by_file(self.path_text.text())

            self.model_text.setText(str(config.name))
            self.price_text.setText(str(config.price) + ' руб.')
            self.calc_but.blockSignals(False)
        else:
            self.calc_but.blockSignals(True)

        self.setWindowTitle('Pdf')
        self.calc_but.clicked.connect(self.calc)
        self.path_but.clicked.connect(self.find_folder_path)

    def calc(self):
        result = CalculateSumm.calculate(self.path_text.text())
        self.dop_result_text.setText(str(result) + ' руб.')
        config = CalculateSumm.get_info_by_file(self.path_text.text())
        self.all_result_text.setText(str(result + config.price) + ' руб.')

    def find_folder_path(self):
        filetypes = (('pfd files', '*.pdf'), ('All files', '*.*'))
        f = fd.askopenfilename(filetypes=filetypes, initialdir="D:/Downloads")
        self.path_text.setText(f.title())
        SavePath(f.title())

        config = CalculateSumm.get_info_by_file(f.title())

        if config.price != '':
            self.model_text.setText(str(config.name))
            self.price_text.setText(str(config.price) + ' руб.')

            print(config.path)
            print(config.price)
            print(config.articul)

            self.calc_but.blockSignals(False)
        else:
            self.calc_but.blockSignals(True)




app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(600, 230)
window.show()

app.exec()

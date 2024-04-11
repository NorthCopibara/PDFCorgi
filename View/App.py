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

        self.setWindowTitle('Pdf')
        self.calc_but.clicked.connect(self.calc)
        self.path_but.clicked.connect(self.find_folder_path)

    def calc(self):
        result = CalculateSumm.calculate(self.path_text.text())
        self.result_text.setText('Результат: {0}'.format(1333151656549111111111))

    def find_folder_path(self):
        filetypes = (('pfd files', '*.pdf'), ('All files', '*.*'))
        f = fd.askopenfilename(filetypes=filetypes, initialdir="D:/Downloads")
        self.path_text.setText(f.title())
        SavePath(f.title())

app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(320, 200)
window.show()

app.exec()
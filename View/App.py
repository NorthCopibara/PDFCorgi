

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys

from PyQt6 import uic

import Config
from Calculations import CalculateSumm
#from Save.SaveLoadLastFilePath import LoadPath, SavePath

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi(Config.UI_PATH, self)

        #self.path_text.setText(LoadPath())
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
        file_name = QFileDialog.getOpenFileName(self, "Find pdf", None, "Pdf (*.pdf)")[0]
        if not file_name:
            return

        self.path_text.setText(file_name)
        #SavePath(file_name)

        config = CalculateSumm.get_info_by_file(file_name)

        if not config:
            print('Config not found')
            return

        if config.price != '':
            self.model_text.setText(str(config.name))
            self.price_text.setText(str(config.price) + ' руб.')

            print(config.path)
            print(config.price)
            print(config.articul)

            self.calc_but.blockSignals(False)
        else:
            self.calc_but.blockSignals(True)


def app_main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(600, 230)
    window.show()
    sys.exit(app.exec())

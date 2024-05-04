from PyQt5.QtWidgets import QFileDialog

def get_file_path():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    if dialog.exec():
        return dialog.selectedFiles()[0]

file_path = get_file_path()

print(file_path)
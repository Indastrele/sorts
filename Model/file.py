from PySide6 import QtWidgets


class File:
    def __init__(self, path):
        self.ref = path

    def read_from(self):
        try:
            with open(self.ref, "r") as f:
                return f.read().split()
        except FileNotFoundError:
            err = QtWidgets.QMessageBox()
            err.warning(err, "Сообщение об ошибке", "Файл не существует", QtWidgets.QMessageBox.StandardButton.Close)

    @staticmethod
    def write_to(path, arr):
        with open(path, "w") as f:
            f.write(' '.join([str(i) for i in arr]))

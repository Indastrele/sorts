from PySide6 import QtWidgets


class File:
    def __init__(self, ):
        self.__ref = str()

    def read(self):
        self.__ref, ok = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), "Open Directory", "",
                                                               "Text Files (*.txt)")
        try:
            with open(self.__ref, "r") as f:
                return f.read().split()
        except FileNotFoundError:
            err = QtWidgets.QMessageBox()
            err.warning(err, "Сообщение об ошибке", "Не удалось открыть файл",
                        QtWidgets.QMessageBox.StandardButton.Close)
            return ""

    @staticmethod
    def write_to(arr):
        save, ok = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QMainWindow(), "Open Directory", "",
                                                         "Text Files (*.txt)")
        with open(save, "w") as f:
            f.write(' '.join([str(i) for i in arr]))

    def get_ref(self):
        return self.__ref

    def set_ref(self, ref):
        self.__ref = ref

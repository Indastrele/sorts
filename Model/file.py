from PySide6 import QtWidgets
import docx2txt


class File:
    def __init__(self, ):
        self.__ref = str()

    # reading information from file
    def read(self):
        self.__ref, ok = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), "Open Directory", "",
                                                               "Text Files (*.txt *.docx)")
        if self.__ref == "":
            return "Сообщение об ошибке", "Не удалось открыть файл"
        if self.__ref[-4:] == ".txt":
            try:
                with open(self.__ref, "r") as f:
                    return f.read().split()
            except FileNotFoundError:
                return "Сообщение об ошибке", "Не удалось открыть файл"
        elif self.__ref[-5:] == ".docx":
            return docx2txt.process(self.__ref).split()

    # save array to file
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

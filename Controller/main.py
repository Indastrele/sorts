"""
Program is made by Stanislau Yudzin from group 10701322
BNTU 2023
"""


from View import (Ui_main_window, Ui_greetings)  # import interface made with PySide6 (PyQt6)
from Model import (Array, File)  # logic of program
from PySide6 import (QtWidgets)  # library for Qt6 in python
import sys  # library for getting arguments of the command line


# App class
class App(QtWidgets.QMainWindow, Ui_main_window):
    # constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__array = Array()
        self.__file = File()
        self.sort_button.clicked.connect(self.__sort)
        self.generate_button.clicked.connect(self.__generated_array)
        self.open_action.triggered.connect(self.__open)
        self.save_button.clicked.connect(self.__save)
        self.save_action.triggered.connect(self.__save)

    def __generated_array(self):
        left = self.left_border_text_edit.toPlainText()
        right = self.right_border_text_edit.toPlainText()
        size = self.array_size_text_edit.toPlainText()
        self.__array.generate(left, right, size)
        self.unsorted_array_text_edit.setText(' '.join(self.__array.get_string()))

    def __sort(self):
        err = QtWidgets.QMessageBox()
        left = 0
        right = self.__array.get_size() - 1
        if right < 0:
            err.warning(err, "Отсутствует массив",
                        "Для начала необходимо либо загрузить массив, либо его сгенерировать",
                        QtWidgets.QMessageBox.StandardButton.Close, QtWidgets.QMessageBox.StandardButton.Close)
            return
        if self.merge_sort_radiobutton.isChecked():
            self.__array.merge_sort(left, right, self.ascending_order.isChecked(), self.descending_order.isChecked())
        elif self.heap_sort_radiobutton.isChecked():
            err.warning(err, "Здесь пока пусто", "Разработчик собирается добавить сюда функционал",
                        QtWidgets.QMessageBox.StandardButton.Close, QtWidgets.QMessageBox.StandardButton.Close)
            return
        self.sorted_array_text_edit.setText(' '.join(self.__array.get_string()))

    def __open(self):  # open file and read array from it
        arr = self.__file.read_from()
        if arr == "":
            return
        self.__array.set_array(arr)
        self.unsorted_array_text_edit.setText(' '.join(self.__array.get_string()))

    def __save(self):  # write array to .txt file
        self.__file.write_to(self.__array.get_array())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

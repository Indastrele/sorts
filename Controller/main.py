"""
Program is made by Stanislau Yudzin from group 10701322
BNTU 2023
"""


from View import interface  # import interface made with PySide6 (PyQt6)
from Model import (sorts, array_generator)  # logic of program
from PySide6 import (QtWidgets)  # library for Qt6 in python
import sys  # library for getting arguments of the command line


# App class
class App(QtWidgets.QMainWindow, interface.Ui_main_window):
    # constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__array = list()
        self.sort_button.clicked.connect(self.__sort)
        self.generate_button.clicked.connect(self.__generated_array)

    def __generated_array(self):
        error = QtWidgets.QMessageBox()
        if len(self.left_border_text_edit.toPlainText()) == 0 or len(self.right_border_text_edit.toPlainText()) == 0:
            error.setText("No input.")
            error.setWindowTitle("Error")
            error.exec()
            return

        if self.left_border_text_edit.toPlainText().isdigit() and self.right_border_text_edit.toPlainText().isdigit():
            left_border = int(self.left_border_text_edit.toPlainText())
            right_border = int(self.right_border_text_edit.toPlainText())
        elif self.left_border_text_edit.toPlainText().isalpha() and self.right_border_text_edit.toPlainText().isalpha():
            if len(self.left_border_text_edit.toPlainText()) > 1 or len(self.right_border_text_edit.toPlainText()) > 1:
                error.setText("Input is string, not char.")
                error.setWindowTitle("Error")
                error.exec()
            left_border = ord(self.left_border_text_edit.toPlainText())
            right_border = ord(self.right_border_text_edit.toPlainText())
        elif not self.left_border_text_edit.toPlainText().isalpha()\
                and not self.right_border_text_edit.toPlainText().isalpha():
            left_border = float(self.left_border_text_edit.toPlainText())
            right_border = float(self.right_border_text_edit.toPlainText())
        else:
            error.warning(error, "Сообщение об ошибке", "Данные должны быть одного типа", QtWidgets.QMessageBox.
                          StandardButton.Close)

        size = 10
        if len(self.array_size_text_edit.toPlainText()) != 0:
            size = int(self.array_size_text_edit.toPlainText())

        if str(left_border).isdigit():
            array = array_generator.generate(left_border, right_border, size)
        else:
            array = array_generator.float_generate(left_border, right_border, size)

        if self.left_border_text_edit.toPlainText().isalpha() or self.right_border_text_edit.toPlainText().isalpha():
            self.__array = list()
            for i in range(0, size):
                self.__array.append(chr(array[i]))
        else:
            self.__array = array

        self.array_text_edit.setText('')
        self.__array_output()

    def __sort(self):
        if str(self.__array[0]).isalpha():
            self.__array = sorts.merge_sort_strings(self.__array, 0, len(self.__array) - 1)
        else:
            self.__array = sorts.merge_sort_nums(self.__array, 0, len(self.__array) - 1)
        self.__array_output()

    def __array_output(self):
        if self.array_text_edit.toPlainText() != '':
            self.array_text_edit.setText(self.array_text_edit.toPlainText() + '\n')
        self.array_text_edit.setText(self.array_text_edit.toPlainText() + ' '.join([str(i) for i in self.__array]))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

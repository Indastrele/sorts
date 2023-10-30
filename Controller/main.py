"""
Program is made by Stanislau Yudzin from group 10710322
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
        if len(self.left_border_text_edit.toPlainText()) == 0 or len(self.right_border_text_edit.toPlainText()) == 0:
            error = QtWidgets.QMessageBox()
            error.setText("No input")
            error.setWindowTitle("Error")
            error.exec()
            return

        left_border = int(self.left_border_text_edit.toPlainText())
        right_border = int(self.right_border_text_edit.toPlainText())
        size = 10
        if len(self.array_size_text_edit.toPlainText()) != 0:
            size = int(self.array_size_text_edit.toPlainText())
        self.__array = array_generator.generate(left_border, right_border, size)
        self.array_text_edit.setText(' '.join([str(i) for i in self.__array]))

    def __sort(self):
        if str(self.__array[0]).isdigit():
            self.__array = sorts.merge_sort_nums(self.__array, 0, len(self.__array))
            self.array_text_edit.setText(self.array_text_edit.toPlainText() + f"\n{self.__array}")
        else:
            self.__array = sorts.merge_sort_strings(self.__array, 0, len(self.__array))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

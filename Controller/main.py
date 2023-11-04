"""
Program is made by Stanislau Yudzin from group 10701322
BNTU 2023
"""


from View import (main_window, start_window)  # import interface made with PySide6 (PyQt6)
from Model import (array, file)  # logic of program
from PySide6 import (QtWidgets)  # library for Qt6 in python
import sys  # library for getting arguments of the command line


# App class
class App(QtWidgets.QMainWindow, main_window.Ui_main_window):
    # constructor
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__array = array.Array()
        self.sort_button.clicked.connect(self.__sort)
        self.generate_button.clicked.connect(self.__generated_array)

    def __generated_array(self):
        left = self.left_border_text_edit.toPlainText()
        right = self.right_border_text_edit.toPlainText()
        size = self.array_size_text_edit.toPlainText()
        self.__array.generate(left, right, size)
        self.unsorted_array_text_edit.setText(' '.join(self.__array.get_string()))

    def __sort(self):
        left = 0
        right = self.__array.get_size() - 1
        self.__array.merge_sort(left, right)
        self.sorted_array_text_edit.setText(' '.join(self.__array.get_string()))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

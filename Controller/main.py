"""
Program is made by Stanislau Yudzin from group 10701322
BNTU 2023
"""


from windows import (StartWindow)  # import interface made with PySide6 (PyQt6)
from PySide6 import (QtWidgets)  # library for Qt6 in python
import sys  # library for getting arguments of the command line


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

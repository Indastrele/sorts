from PySide6 import (QtWidgets)
from View import (Ui_greetings, Ui_about, Ui_main_window)
from Model import (Array, File)


class StartWindow(QtWidgets.QMainWindow, Ui_greetings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__file = File()
        self.__main_window = App()
        self.__about = Author()
        self.open_file_button.clicked.connect(self.__open_file)
        self.continue_button.clicked.connect(self.__app_exec)
        self.about_button.clicked.connect(self.__open_about)

    def __app_exec(self):
        self.__main_window.show()
        self.close()

    def __open_file(self):
        self.__main_window.open()
        self.__app_exec()

    def __open_about(self):
        self.__about.show()


# App class
class App(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        self._setupUi(self)
        self.__array = Array()
        self.__file = File()
        self.__author = Author()
        self.sort_button.clicked.connect(self.__sort)
        self.generate_button.clicked.connect(self.__generated_array)
        self.open_action.triggered.connect(self.open)
        self.save_button.clicked.connect(self.__save)
        self.save_action.triggered.connect(self.__save)
        self.open_about_action.triggered.connect(self.__open_about)
        self.compare_button.clicked.connect(self.__compare)

    def __generated_array(self):
        left = self.left_border_line_edit.text()
        right = self.right_border_line_edit.text()
        size = self.size_line_edit.text()
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
            self.__array.heap_sort(self.ascending_order.isChecked(), self.descending_order.isChecked())
        self.sorted_array_text_edit.setText(' '.join(self.__array.get_string()))
        self.speed_text_edit.setText(f"{self.__array.get_sort_time():.6f} sec")

    # comparison between merge sort and heap sort with same array
    def __compare(self):
        temporary_array = list()
        array_is_empty = self.__array.is_empty()
        if not array_is_empty:
            temporary_array = self.__array.get_array()
        time = self.__array.compare()
        result = QtWidgets.QMessageBox()
        result.information(self, "Результаты", f"Сортировка слиянием:\nПо возрастанию {time[0]:.6f} с\n" +
                           f"По убыванию {time[1]:.6f} с\n\n" +
                           f"Пирамидальная сортировка\nПо возрастанию {time[2]:.6f} с\n" +
                           f"По убыванию {time[3]:.6f} с",
                           QtWidgets.QMessageBox.StandardButton.Close
                           )
        if not array_is_empty:
            self.__array.set_array(temporary_array)
        else:
            self.__array = Array()

    def open(self):  # open file and read array from it
        arr = self.__file.read()
        if arr == "":
            return
        self.__array.set_array(arr)
        self.unsorted_array_text_edit.setText(' '.join(self.__array.get_string()))

    def __save(self):  # write array to .txt file
        self.__file.write_to(self.__array.get_array())

    def __open_about(self):
        self.__author.show()


class Author(QtWidgets.QDialog, Ui_about):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

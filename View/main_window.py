# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def _setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(652, 578)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        main_window.setFont(font)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet("background-color: rgb(153, 176, 128);")
        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.generate_label.setGeometry(QtCore.QRect(220, 10, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.generate_label.setFont(font)
        self.generate_label.setStyleSheet("color: rgb(250, 248, 237);")
        self.generate_label.setObjectName("generate_label")
        self.from_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.from_label.setGeometry(QtCore.QRect(100, 50, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.from_label.setFont(font)
        self.from_label.setStyleSheet("color: rgb(250, 248, 237);")
        self.from_label.setObjectName("from_label")
        self.to_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(240, 50, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.to_label.setFont(font)
        self.to_label.setStyleSheet("color: rgb(250, 248, 237);")
        self.to_label.setObjectName("to_label")
        self.array_size_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.array_size_label.setGeometry(QtCore.QRect(380, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.array_size_label.setFont(font)
        self.array_size_label.setStyleSheet("color: rgb(250, 248, 237);")
        self.array_size_label.setObjectName("array_size_label")
        self.generate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(250, 80, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.generate_button.setFont(font)
        self.generate_button.setAutoFillBackground(False)
        self.generate_button.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.generate_button.setObjectName("generate_button")
        self.unsorted_array_text_edit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.unsorted_array_text_edit.setGeometry(QtCore.QRect(20, 170, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.unsorted_array_text_edit.setFont(font)
        self.unsorted_array_text_edit.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.unsorted_array_text_edit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.unsorted_array_text_edit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.unsorted_array_text_edit.setLineWidth(1)
        self.unsorted_array_text_edit.setReadOnly(True)
        self.unsorted_array_text_edit.setObjectName("unsorted_array_text_edit")
        self.sorted_array_text_edit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.sorted_array_text_edit.setGeometry(QtCore.QRect(20, 320, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.sorted_array_text_edit.setFont(font)
        self.sorted_array_text_edit.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.sorted_array_text_edit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sorted_array_text_edit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.sorted_array_text_edit.setLineWidth(1)
        self.sorted_array_text_edit.setReadOnly(True)
        self.sorted_array_text_edit.setObjectName("sorted_array_text_edit")
        self.sort_choice_group_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.sort_choice_group_box.setGeometry(QtCore.QRect(380, 170, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.sort_choice_group_box.setFont(font)
        self.sort_choice_group_box.setAutoFillBackground(False)
        self.sort_choice_group_box.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.sort_choice_group_box.setObjectName("sort_choice_group_box")
        self.merge_sort_radiobutton = QtWidgets.QRadioButton(parent=self.sort_choice_group_box)
        self.merge_sort_radiobutton.setGeometry(QtCore.QRect(10, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.merge_sort_radiobutton.setFont(font)
        self.merge_sort_radiobutton.setAutoFillBackground(False)
        self.merge_sort_radiobutton.setStyleSheet("color: rgb(250, 248, 237);\n"
"background-color: rgb(216, 162, 108);")
        self.merge_sort_radiobutton.setChecked(True)
        self.merge_sort_radiobutton.setObjectName("merge_sort_radiobutton")
        self.heap_sort_radiobutton = QtWidgets.QRadioButton(parent=self.sort_choice_group_box)
        self.heap_sort_radiobutton.setGeometry(QtCore.QRect(10, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.heap_sort_radiobutton.setFont(font)
        self.heap_sort_radiobutton.setAutoFillBackground(False)
        self.heap_sort_radiobutton.setStyleSheet("color: rgb(250, 248, 237);\n"
"background-color: rgb(216, 162, 108);")
        self.heap_sort_radiobutton.setObjectName("heap_sort_radiobutton")
        self.unsorted_array_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.unsorted_array_label.setGeometry(QtCore.QRect(140, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.unsorted_array_label.setFont(font)
        self.unsorted_array_label.setStyleSheet("color: rgb(250, 248, 237);")
        self.unsorted_array_label.setObjectName("unsorted_array_label")
        self.sorted_array_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.sorted_array_label.setGeometry(QtCore.QRect(60, 290, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.sorted_array_label.setFont(font)
        self.sorted_array_label.setStyleSheet("color: rgb(250, 248, 237);")
        self.sorted_array_label.setObjectName("sorted_array_label")
        self.sort_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sort_button.setGeometry(QtCore.QRect(420, 410, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.sort_button.setFont(font)
        self.sort_button.setAutoFillBackground(False)
        self.sort_button.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.sort_button.setObjectName("sort_button")
        self.speed_text_edit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.speed_text_edit.setGeometry(QtCore.QRect(20, 440, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.speed_text_edit.setFont(font)
        self.speed_text_edit.setAutoFillBackground(True)
        self.speed_text_edit.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.speed_text_edit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.speed_text_edit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.speed_text_edit.setLineWidth(1)
        self.speed_text_edit.setReadOnly(True)
        self.speed_text_edit.setObjectName("speed_text_edit")
        self.criteria_group_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.criteria_group_box.setGeometry(QtCore.QRect(380, 290, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.criteria_group_box.setFont(font)
        self.criteria_group_box.setAutoFillBackground(False)
        self.criteria_group_box.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.criteria_group_box.setObjectName("criteria_group_box")
        self.ascending_order = QtWidgets.QRadioButton(parent=self.criteria_group_box)
        self.ascending_order.setGeometry(QtCore.QRect(10, 40, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.ascending_order.setFont(font)
        self.ascending_order.setAutoFillBackground(False)
        self.ascending_order.setStyleSheet("color: rgb(250, 248, 237);\n"
"background-color: rgb(216, 162, 108);")
        self.ascending_order.setChecked(True)
        self.ascending_order.setObjectName("ascending_order")
        self.descending_order = QtWidgets.QRadioButton(parent=self.criteria_group_box)
        self.descending_order.setGeometry(QtCore.QRect(10, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.descending_order.setFont(font)
        self.descending_order.setAutoFillBackground(False)
        self.descending_order.setStyleSheet("color: rgb(250, 248, 237);\n"
"background-color: rgb(216, 162, 108);")
        self.descending_order.setObjectName("descending_order")
        self.save_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(420, 450, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.save_button.setObjectName("save_button")
        self.left_border_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.left_border_line_edit.setGeometry(QtCore.QRect(140, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.left_border_line_edit.setFont(font)
        self.left_border_line_edit.setAutoFillBackground(False)
        self.left_border_line_edit.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.left_border_line_edit.setObjectName("left_border_line_edit")
        self.right_border_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.right_border_line_edit.setGeometry(QtCore.QRect(280, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.right_border_line_edit.setFont(font)
        self.right_border_line_edit.setAutoFillBackground(False)
        self.right_border_line_edit.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.right_border_line_edit.setObjectName("right_border_line_edit")
        self.size_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.size_line_edit.setGeometry(QtCore.QRect(470, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.size_line_edit.setFont(font)
        self.size_line_edit.setAutoFillBackground(False)
        self.size_line_edit.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.size_line_edit.setObjectName("size_line_edit")
        self.compare_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.compare_button.setGeometry(QtCore.QRect(420, 490, 161, 32))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(20)
        self.compare_button.setFont(font)
        self.compare_button.setStyleSheet("background-color: rgb(249, 181, 114);\n"
"color: rgb(250, 248, 237);")
        self.compare_button.setObjectName("compare_button")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 24))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("color: rgb(250, 248, 237);\n"
"background-color: rgb(114, 130, 97);")
        self.menubar.setObjectName("menubar")
        self.about_author = QtWidgets.QMenu(parent=self.menubar)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.about_author.setFont(font)
        self.about_author.setObjectName("about_author")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.help = QtGui.QAction(parent=main_window)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.help.setFont(font)
        self.help.setObjectName("help")
        self.open_action = QtGui.QAction(parent=main_window)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.open_action.setFont(font)
        self.open_action.setObjectName("open_action")
        self.save_action = QtGui.QAction(parent=main_window)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.save_action.setFont(font)
        self.save_action.setObjectName("save_action")
        self.open_about_action = QtGui.QAction(parent=main_window)
        self.open_about_action.setObjectName("open_about_action")
        self.help_action = QtGui.QAction(parent=main_window)
        self.help_action.setObjectName("help_action")
        self.about_author.addAction(self.open_about_action)
        self.menu_3.addAction(self.open_action)
        self.menu_3.addAction(self.save_action)
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.about_author.menuAction())

        self.__retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def __retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Сортировки"))
        self.generate_label.setText(_translate("main_window", "Сгенерировать массив"))
        self.from_label.setText(_translate("main_window", "От"))
        self.to_label.setText(_translate("main_window", "До"))
        self.array_size_label.setText(_translate("main_window", "Размер"))
        self.generate_button.setText(_translate("main_window", "Сгенерировать"))
        self.sort_choice_group_box.setTitle(_translate("main_window", "Сортировки"))
        self.merge_sort_radiobutton.setText(_translate("main_window", "Слиянием"))
        self.heap_sort_radiobutton.setText(_translate("main_window", "Пирамидальная"))
        self.unsorted_array_label.setText(_translate("main_window", "Массив"))
        self.sorted_array_label.setText(_translate("main_window", "Отсортированный массив"))
        self.sort_button.setText(_translate("main_window", "Отсортировать"))
        self.criteria_group_box.setTitle(_translate("main_window", "Критерий"))
        self.ascending_order.setText(_translate("main_window", "По возрастанию"))
        self.descending_order.setText(_translate("main_window", "По убыванию"))
        self.save_button.setText(_translate("main_window", "Сохранить"))
        self.left_border_line_edit.setText("0")
        self.right_border_line_edit.setText("100")
        self.size_line_edit.setText("10")
        self.compare_button.setText(_translate("main_window", "Сравнить"))
        self.about_author.setTitle(_translate("main_window", "Об авторе"))
        self.menu_3.setTitle(_translate("main_window", "Файл"))
        self.help.setText(_translate("main_window", "Таблица символов"))
        self.open_action.setText(_translate("main_window", "Открыть файл"))
        self.save_action.setText(_translate("main_window", "Сохранить"))
        self.open_about_action.setText(_translate("main_window", "Об авторе"))
        self.help_action.setText(_translate("main_window", "Справка"))

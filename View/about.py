# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(411, 394)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        about.setFont(font)
        about.setAutoFillBackground(True)
        about.setStyleSheet("background-color: rgb(153, 176, 128);")
        self.label = QtWidgets.QLabel(parent=about)
        self.label.setGeometry(QtCore.QRect(130, 10, 151, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("View/photo_2023-11-13 11.38.56.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=about)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rrgb(250, 248, 237);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=about)
        self.label_3.setGeometry(QtCore.QRect(120, 210, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rrgb(250, 248, 237);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=about)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rrgb(250, 248, 237);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=about)
        self.label_5.setGeometry(QtCore.QRect(10, 290, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=about)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "О программе"))
        self.label_2.setText(_translate("about", "Юдин Станислав Васильевич"))
        self.label_3.setText(_translate("about", "Студент БНТУ"))
        self.label_4.setText(_translate("about", "Группа 10701322"))
        self.label_5.setText(_translate("about", "Курсовой проект по предмету"))
        self.label_6.setText(_translate("about", "\"Языки программирования\""))
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtCore.QObject):
    data_added = QtCore.pyqtSignal(str, str, str, str)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 671, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите ФИО")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 100, 671, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Введите номер телефона")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 170, 671, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Введите адрес")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 240, 481, 101))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Дополнительная информация")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(30, 380, 161, 51))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_add_info_person = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_info_person.setGeometry(QtCore.QRect(540, 380, 161, 51))
        self.pushButton_add_info_person.setObjectName("pushButton_add_info_person")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(540, 250, 138, 88))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.checkBox_per_1 = QtWidgets.QCheckBox(self.widget)
        # self.checkBox_per_1.setObjectName("checkBox_per_1")
        # self.verticalLayout.addWidget(self.checkBox_per_1)
        # self.checkBox_per_2 = QtWidgets.QCheckBox(self.widget)
        # self.checkBox_per_2.setObjectName("checkBox_per_2")
        # self.verticalLayout.addWidget(self.checkBox_per_2)
        # self.checkBox_per_3 = QtWidgets.QCheckBox(self.widget)
        # self.checkBox_per_3.setObjectName("checkBox_per_3")
        # self.verticalLayout.addWidget(self.checkBox_per_3)
        # self.checkBox_per_4 = QtWidgets.QCheckBox(self.widget)
        # self.checkBox_per_4.setObjectName("checkBox_per_4")
        # self.verticalLayout.addWidget(self.checkBox_per_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_add_info_person.clicked.connect(self.add_info)
        self.pushButton_cancel.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Новый сотрудник"))
        self.pushButton_cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))
        self.pushButton_add_info_person.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        # self.checkBox_per_1.setText(_translate("MainWindow", "УСТАНОВИТЬ ДОСТУП"))
        # self.checkBox_per_2.setText(_translate("MainWindow", "УСТАНОВИТЬ ДОСТУП"))
        # self.checkBox_per_3.setText(_translate("MainWindow", "УСТАНОВИТЬ ДОСТУП"))
        # self.checkBox_per_4.setText(_translate("MainWindow", "УСТАНОВИТЬ ДОСТУП"))

    def add_info(self):
        name = self.lineEdit.text()
        phone = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        info = self.lineEdit_4.text()

        self.data_added.emit(name, phone, address, info)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

        self.centralwidget.window().close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

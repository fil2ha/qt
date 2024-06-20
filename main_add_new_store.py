from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(QtCore.QObject):
    data_added = QtCore.pyqtSignal(str, str, str, str,)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(450, 430, 191, 51))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(30, 430, 191, 51))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 160, 641, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Название склада")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Координата а")
        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit3.setObjectName("lineEdit")
        self.lineEdit3.setPlaceholderText("Координата b")
        self.verticalLayout.addWidget(self.lineEdit3)

        self.lineEdit4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit4.setObjectName("lineEdit")
        self.lineEdit4.setPlaceholderText("Адрес")
        self.verticalLayout.addWidget(self.lineEdit4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_cancel.clicked.connect(MainWindow.close)
        self.pushButton_save.clicked.connect(self.add_info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Новый склад"))
        self.pushButton_save.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.pushButton_cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))

    def add_info(self):
        coordinates_a = self.lineEdit.text()
        name = self.lineEdit_2.text()
        coordinates_b = self.lineEdit3.text()
        adress = self.lineEdit4.text()
        self.data_added.emit(name, coordinates_a, coordinates_b, adress)
        self.lineEdit.clear()
        self.lineEdit_2.clear()

        self.centralwidget.window().close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtCore.QObject):
    data_added = QtCore.pyqtSignal(str, str, str, str, str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 671, 41))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите название товара")

        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(30, 380, 161, 51))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_add_product = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_product.setGeometry(QtCore.QRect(540, 380, 161, 51))
        self.pushButton_add_product.setObjectName("pushButton_add_product")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 90, 671, 41))
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Введите артикль товара")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 150, 671, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Введите цену товара")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 210, 671, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Введите дату хранения?")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 270, 671, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("Ссылка на фото")

        # self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_6.setGeometry(QtCore.QRect(30, 330, 671, 41))
        # self.lineEdit_6.setObjectName("lineEdit_6")
        # self.lineEdit_6.setPlaceholderText("Склад")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_cancel.clicked.connect(MainWindow.close)
        self.pushButton_add_product.clicked.connect(self.add_info)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Добавить"))
        self.pushButton_cancel.setText(_translate("mainWindow", "ОТМЕНИТЬ"))
        self.pushButton_add_product.setText(_translate("mainWindow", "ДОБАВИТЬ"))

    def add_info(self):
        name = self.lineEdit.text()
        articul = self.lineEdit_2.text()
        price = self.lineEdit_3.text()
        ex_time = self.lineEdit_4.text()
        img = self.lineEdit_5.text()
        # store = self.lineEdit_6.text()
        self.data_added.emit(name, articul, price, ex_time, img)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        # self.lineEdit_6.clear()
        self.centralwidget.window().close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtCore, QtWidgets
import sys


class Ui_MainWindow(QObject):
    data_added1 = QtCore.pyqtSignal(str, str, str, str, str, str, str, str, str, str, str, str, str)

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
        self.widget.setGeometry(QtCore.QRect(20, 20, 651, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Название организации")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Учетный номер плательщика")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Адрес")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Расчетный счет")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setPlaceholderText("БИК Банка")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setPlaceholderText("Банк")
        self.verticalLayout.addWidget(self.lineEdit_9)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setPlaceholderText("Адрес банка")
        self.verticalLayout.addWidget(self.lineEdit_12)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setPlaceholderText("Директор")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setPlaceholderText("Адрес электронной почты")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setPlaceholderText("Номер телефона")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setPlaceholderText("Номер договора")
        self.verticalLayout.addWidget(self.lineEdit_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setPlaceholderText("Дополнительная информация")
        self.verticalLayout.addWidget(self.lineEdit_10)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить нового клиента"))
        self.pushButton_save.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.pushButton_cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))

    def add_info(self):
        name = self.lineEdit.text()
        unp = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        count = self.lineEdit_4.text()
        bik = self.lineEdit_5.text()
        ceo = self.lineEdit_6.text()
        phone = self.lineEdit_7.text()
        email = self.lineEdit_8.text()
        bank = self.lineEdit_9.text()
        more = self.lineEdit_10.text()
        num_doc = self.lineEdit_11.text()
        bank_address = self.lineEdit_12.text()
        self.data_added1.emit(name, unp, address, count, bik, bank, bank_address, ceo, email, phone, num_doc, more)
        # self.lineEdit.clear()
        # self.lineEdit_2.clear()
        # self.lineEdit_3.clear()
        # self.lineEdit_4.clear()
        # self.lineEdit_5.clear()
        # self.lineEdit_6.clear()
        # self.lineEdit_7.clear()
        # self.lineEdit_8.clear()
        # self.lineEdit_9.clear()
        # self.lineEdit_10.clear()
        # self.lineEdit_11.clear()
        # self.lineEdit_12.clear()
        self.centralwidget.window().close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



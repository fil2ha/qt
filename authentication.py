from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import main

person_id = 0
person_name = ''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_OK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OK.setGeometry(QtCore.QRect(110, 270, 231, 51))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_dont = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dont.setGeometry(QtCore.QRect(390, 270, 231, 51))
        self.pushButton_dont.setObjectName("pushButton_dont")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(110, 60, 511, 51))
        self.login.setObjectName("login")
        self.login.setPlaceholderText("Введите логин")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(110, 140, 511, 51))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("Введите пароль")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_OK.clicked.connect(self.authenticate)
        self.pushButton_dont.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.pushButton_OK.setText(_translate("MainWindow", "Войти"))
        self.pushButton_dont.setText(_translate("MainWindow", "Отмена"))

    def authenticate(self):
        username = self.login.text()
        password = self.password.text()

        connection = sqlite3.connect('database.db', check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Permissions WHERE login=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            #добавть id, добавить имя
            self.open_main()

            MainWindow.close()

        else:
            QMessageBox.warning(None, "Ошибка", "Логин или пароль введены неверно!")
            print("Ошибка авторизации")

        connection.close()


    def open_main(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

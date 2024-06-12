
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 951, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_2.addWidget(self.Cancel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Delete = QtWidgets.QPushButton(self.layoutWidget)
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        self.Add = QtWidgets.QPushButton(self.layoutWidget)
        self.Add.setObjectName("Add")
        self.horizontalLayout.addWidget(self.Add)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.OK = QtWidgets.QPushButton(self.layoutWidget)
        self.OK.setObjectName("OK")
        self.horizontalLayout_2.addWidget(self.OK)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))
        self.Delete.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.Add.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.OK.setText(_translate("MainWindow", "СОХРАНИТЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

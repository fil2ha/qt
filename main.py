from PyQt5 import QtCore, QtGui, QtWidgets

import clients2, products, stores, personal, spis, replac, buy, sold
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(890, 650, 171, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_exit.setObjectName("pushButton_exit")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 1061, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)


        # self.tableView = QtWidgets.QTableView(self.centralwidget)
        # self.tableView.setGeometry(QtCore.QRect(30, 150, 1061, 491))
        # self.tableView.setObjectName("tableView")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 650, 841, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 30, 931, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_change = QtWidgets.QPushButton(self.widget)
        self.pushButton_change.setObjectName("pushButton_change")
        self.horizontalLayout_2.addWidget(self.pushButton_change)
        self.pushButton_del = QtWidgets.QPushButton(self.widget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_2.addWidget(self.pushButton_del)
        self.pushButton_post = QtWidgets.QPushButton(self.widget)
        self.pushButton_post.setObjectName("pushButton_post")
        self.horizontalLayout_2.addWidget(self.pushButton_post)
        self.pushButton_get = QtWidgets.QPushButton(self.widget)
        self.pushButton_get.setObjectName("pushButton_get")
        self.horizontalLayout_2.addWidget(self.pushButton_get)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_documents = QtWidgets.QPushButton(self.widget)
        self.pushButton_documents.setObjectName("pushButton_documents")
        self.verticalLayout_3.addWidget(self.pushButton_documents)
        self.pushButton_rollback = QtWidgets.QPushButton(self.widget)
        self.pushButton_rollback.setObjectName("pushButton_rollback")
        self.verticalLayout_3.addWidget(self.pushButton_rollback)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_clients = QtWidgets.QPushButton(self.widget)
        self.pushButton_clients.setObjectName("pushButton_clients")
        self.verticalLayout.addWidget(self.pushButton_clients)
        self.pushButton_stores = QtWidgets.QPushButton(self.widget)
        self.pushButton_stores.setObjectName("pushButton_stores")
        self.verticalLayout.addWidget(self.pushButton_stores)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_personal = QtWidgets.QPushButton(self.widget)
        self.pushButton_personal.setObjectName("pushButton_personal")
        self.verticalLayout_2.addWidget(self.pushButton_personal)
        self.pushButton__product = QtWidgets.QPushButton(self.widget)
        self.pushButton__product.setObjectName("pushButton__product")
        self.verticalLayout_2.addWidget(self.pushButton__product)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(80, 120, 421, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton_search = QtWidgets.QPushButton(self.widget1)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_4.addWidget(self.pushButton_search)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_clients.clicked.connect(self.show_clients)
        self.pushButton_stores.clicked.connect(self.show_stores)
        self.pushButton_personal.clicked.connect(self.show_personal)
        self.pushButton__product.clicked.connect(self.show_product)
        self.pushButton_change.clicked.connect(self.show_change)
        self.pushButton_del.clicked.connect(self.show_del)
        self.pushButton_get.clicked.connect(self.show_get)
        self.pushButton_post.clicked.connect(self.show_post)
        self.pushButton_exit.clicked.connect(MainWindow.close)
        self.database1()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная"))
        self.pushButton_exit.setText(_translate("MainWindow", "ВЫЙТИ ИЗ СИСТЕМЫ"))
        self.pushButton_change.setText(_translate("MainWindow", " ПЕРЕМЕСТИТЬ"))
        self.pushButton_del.setText(_translate("MainWindow", "СПИСАТЬ"))
        self.pushButton_post.setText(_translate("MainWindow", "ОТПУСТИТЬ"))
        self.pushButton_get.setText(_translate("MainWindow", "ПРИНЯТЬ"))
        self.pushButton_documents.setText(_translate("MainWindow", "Документы"))
        self.pushButton_rollback.setText(_translate("MainWindow", "Отменить операцию"))
        self.pushButton_clients.setText(_translate("MainWindow", "КЛИЕНТЫ"))
        self.pushButton_stores.setText(_translate("MainWindow", "СКЛАДЫ"))
        self.pushButton_personal.setText(_translate("MainWindow", "ПЕРСОНАЛ"))
        self.pushButton__product.setText(_translate("MainWindow", "ТОВАРЫ"))
        self.pushButton_search.setText(_translate("MainWindow", "Поиск"))

    def show_clients(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = clients2.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def show_personal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = personal.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def show_product(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = products.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_stores(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = stores.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_change(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = replac.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_del(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = spis.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_get(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = buy.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_post(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = sold.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def database1(self):
        con = sqlite3.connect('database.db', check_same_thread=False)
        table_name = 'Transactions'
        with con:
            cur = con.execute(f"Pragma table_info ('{table_name}')")
            pragma_answer = cur.fetchall()

            list_of_col = [i[1] for i in pragma_answer]

            cur = con.execute(f"Select * From {table_name}")
            table_data = cur.fetchall()
            list_of_left_rows = [str(i[0]) for i in table_data]

            self.tableWidget.setColumnCount(len(list_of_col))
            self.tableWidget.setHorizontalHeaderLabels(list_of_col)
            self.tableWidget.setRowCount(len(list_of_left_rows))
            self.tableWidget.setVerticalHeaderLabels(list_of_left_rows)

            for i in range(len(table_data)):
                for j in range(len(table_data[i])):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(table_data[i][j])))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

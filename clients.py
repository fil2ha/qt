from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3


class Ui_Dialog(object):
    def setupU(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(991, 676)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 951, 631))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Cancel = QtWidgets.QPushButton(self.widget)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_2.addWidget(self.Cancel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Delete = QtWidgets.QPushButton(self.widget)
        self.Delete.setObjectName("Delete")
        self.horizontalLayout.addWidget(self.Delete)
        self.Add = QtWidgets.QPushButton(self.widget)
        self.Add.setObjectName("Add")
        self.horizontalLayout.addWidget(self.Add)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.OK = QtWidgets.QPushButton(self.widget)
        self.OK.setObjectName("OK")
        self.horizontalLayout_2.addWidget(self.OK)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Cancel.clicked.connect(Dialog.close)
        self.Add.clicked.connect(self.add_client)
        self.Delete.clicked.connect(self.ff)
        self.function_2()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Клиенты"))
        self.Cancel.setText(_translate("Dialog", "ОТМЕНИТЬ"))
        self.Delete.setText(_translate("Dialog", "УДАЛИТЬ"))
        self.Add.setText(_translate("Dialog", "ДОБАВИТЬ"))
        self.OK.setText(_translate("Dialog", "СОХРАНИТЬ"))


    def add_client(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main_add_new_client.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def function_2(self):
        # if not table_name:
        #     table_name = self.comboBox.currentText()
        con = sqlite3.connect('database.db', check_same_thread=False)
        table_name = 'Clients'
        with con:
            cur = con.execute(f"Pragma table_info ('{table_name}')")
            pragma_answer = cur.fetchall()
            print(pragma_answer)

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
        con.commit()
    def ff(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupU(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

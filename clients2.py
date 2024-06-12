import sys

import main_add_new_client
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 951, 631))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 130, 800, 421))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Cancel.clicked.connect(MainWindow.close)
        self.Add.clicked.connect(self.add_client)
        self.Delete.clicked.connect(self.mark_for_deletion)
        self.OK.clicked.connect(self.save_changes)
        self.function_2()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.items_to_add = []
        self.items_to_delete = []
        self.main_window = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Клиенты"))
        self.Cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))
        self.Delete.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.Add.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.OK.setText(_translate("MainWindow", "СОХРАНИТЬ"))

    def add_client(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main_add_new_client.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.data_added1.connect(self.add_info_in)
        self.window.show()


    def function_2(self):
        con = sqlite3.connect('database.db', check_same_thread=False)
        table_name = 'Clients'
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
        con.commit()

    def add_info_in(self, name, unp, address, count, bik, bank, bank_address, ceo, email, phone, num_doc, more):
        max_id = 0
        row_count = self.tableWidget.rowCount()

        for row in range(row_count):
            item = self.tableWidget.item(row, 0)
            if item is not None:
                try:
                    current_id = int(item.text())
                    if current_id > max_id:
                        max_id = current_id
                except ValueError:
                    continue

        new_id = max_id + 1

        self.tableWidget.insertRow(row_count)

        id_item = QtWidgets.QTableWidgetItem(str(new_id))
        name_item = QtWidgets.QTableWidgetItem(name)
        unp_item = QtWidgets.QTableWidgetItem(unp)
        address_item = QtWidgets.QTableWidgetItem(address)
        count_item = QtWidgets.QTableWidgetItem(count)
        bik_item = QtWidgets.QTableWidgetItem(bik)
        bank_item = QtWidgets.QTableWidgetItem(bank)
        bank_address_item = QtWidgets.QTableWidgetItem(bank_address)
        ceo_item = QtWidgets.QTableWidgetItem(ceo)
        email_item = QtWidgets.QTableWidgetItem(email)
        phone_item = QtWidgets.QTableWidgetItem(phone)
        num_doc_item = QtWidgets.QTableWidgetItem(num_doc)
        more_item = QtWidgets.QTableWidgetItem(more)

        self.tableWidget.setItem(row_count, 0, id_item)
        self.tableWidget.setItem(row_count, 1, name_item)
        self.tableWidget.setItem(row_count, 2, unp_item)
        self.tableWidget.setItem(row_count, 3, address_item)
        self.tableWidget.setItem(row_count, 4, count_item)
        self.tableWidget.setItem(row_count, 5, bik_item)
        self.tableWidget.setItem(row_count, 6, bank_item)
        self.tableWidget.setItem(row_count, 7, bank_address_item)
        self.tableWidget.setItem(row_count, 8, ceo_item)
        self.tableWidget.setItem(row_count, 9, email_item)
        self.tableWidget.setItem(row_count, 10, phone_item)
        self.tableWidget.setItem(row_count, 11, num_doc_item)
        self.tableWidget.setItem(row_count, 12, more_item)

        self.items_to_add.append(
            (new_id, name, unp, address, count, bik, bank, bank_address, ceo, email, phone, num_doc, more))

    def mark_for_deletion(self):
        current_row = self.tableWidget.currentRow()
        if current_row >= 0:
            item = self.tableWidget.item(current_row, 0)
            if item:
                item_id = item.text()
                self.items_to_delete.append(item_id)
            self.tableWidget.removeRow(current_row)

    def save_changes(self):
        con = sqlite3.connect('database.db', check_same_thread=False)
        table_name = 'Clients'
        try:
            with con:
                cur = con.cursor()
            for item_id in self.items_to_delete:
                cur.execute(f"DELETE FROM {table_name} WHERE id = ?", (item_id,))
            for item in self.items_to_add:
                cur.executemany(
                    '''INSERT INTO Clients (id, name, ind_number, ceo, phone, email, address, current_account, bank, bik, bank_address, info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (item,))
            con.commit()
        except sqlite3.Error as e:
            print("Ошибка SQLite:", e)

        self.items_to_add.clear()
        self.items_to_delete.clear()

        self.main_window.close()
        con.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(985, 683)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.widget = QtWidgets.QWidget(self.centralwidget)
#         self.widget.setGeometry(QtCore.QRect(20, 20, 951, 631))
#         self.widget.setObjectName("widget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setObjectName("verticalLayout")
#
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(5, 130, 800, 421))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.verticalLayout.addWidget(self.tableWidget)
#
#
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.Cancel = QtWidgets.QPushButton(self.widget)
#         self.Cancel.setObjectName("Cancel")
#         self.horizontalLayout_2.addWidget(self.Cancel)
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.Delete = QtWidgets.QPushButton(self.widget)
#         self.Delete.setObjectName("Delete")
#         self.horizontalLayout.addWidget(self.Delete)
#         self.Add = QtWidgets.QPushButton(self.widget)
#         self.Add.setObjectName("Add")
#         self.horizontalLayout.addWidget(self.Add)
#         self.horizontalLayout_2.addLayout(self.horizontalLayout)
#         self.OK = QtWidgets.QPushButton(self.widget)
#         self.OK.setObjectName("OK")
#         self.horizontalLayout_2.addWidget(self.OK)
#         self.verticalLayout.addLayout(self.horizontalLayout_2)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#
#         self.Cancel.clicked.connect(MainWindow.close)
#         self.Add.clicked.connect(self.add_client)
#         self.Delete.clicked.connect(self.mark_for_deletion)
#         self.OK.clicked.connect(self.save_changes)
#         self.function_2()
#
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#         self.items_to_add = []
#         self.items_to_delete = []
#         self.main_window = MainWindow
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Клиенты"))
#         self.Cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))
#         self.Delete.setText(_translate("MainWindow", "УДАЛИТЬ"))
#         self.Add.setText(_translate("MainWindow", "ДОБАВИТЬ"))
#         self.OK.setText(_translate("MainWindow", "СОХРАНИТЬ"))
#
#     def add_client(self):
#         print("Кнопка 'Добавить' нажата")
#         self.window = QtWidgets.QMainWindow()
#         self.ui = main_add_new_client.Ui_MainWindow()
#         self.ui.setupUi(self.window)
#         print("Окно setupUi вызвано")
#
#         # Проверим, существует ли сигнал data_added1
#         if hasattr(self.ui, 'data_added1'):
#             print("Сигнал data_added1 существует")
#             self.ui.data_added1.connect(self.add_info_in)
#             print("Сигнал data_added1 подключен")
#         else:
#             print("Сигнал data_added1 не существует")
#
#         self.window.show()
#         print("Новое окно показано")
#
#
#
#     def function_2(self):

#
#
#     def add_info_in(self, name, unp, address, count, bik, bank, bank_address, ceo, email, phone, num_doc, more):

#
#     def mark_for_deletion(self):

#
#     def save_changes(self):

#
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

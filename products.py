from PyQt5 import QtCore, QtGui, QtWidgets
import main_admin_add_product
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 983)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 70, 951, 631))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 130, 800, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Количество", "Цена", "Изображение", "Описание", "Склад"])
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
        self.Add.clicked.connect(self.add_person)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Товары"))
        self.Cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))
        self.Delete.setText(_translate("MainWindow", "УДАЛИТЬ"))
        self.Add.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.OK.setText(_translate("MainWindow", "СОХРАНИТЬ"))


    def add_person(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main_admin_add_product.Ui_MainWindow()
        self.ui.setupUi(self.window)
        print('4')
        self.ui.data_addedd.connect(self.add_info_in)
        print('5')
        self.window.show()


    def function_2(self):
        con = sqlite3.connect('srm.db', check_same_thread=False)
        table_name = 'Goods'
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
        con.close()

    def add_info_inn(self, name, amount, price, image, desc, store):
        print('6')
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
        amount_item = QtWidgets.QTableWidgetItem(str(amount))
        price_item = QtWidgets.QTableWidgetItem(str(price))
        image_item = QtWidgets.QTableWidgetItem(image)
        desc_item = QtWidgets.QTableWidgetItem(desc)
        store_item = QtWidgets.QTableWidgetItem(str(store))

        self.tableWidget.setItem(row_count, 0, id_item)
        self.tableWidget.setItem(row_count, 1, name_item)
        self.tableWidget.setItem(row_count, 2, amount_item)
        self.tableWidget.setItem(row_count, 3, price_item)
        self.tableWidget.setItem(row_count, 4, store_item)
        self.tableWidget.setItem(row_count, 5, desc_item)
        self.tableWidget.setItem(row_count, 6, image_item)


        self.items_to_add.append((new_id, name, amount, price, store, desc, image))

    def mark_for_deletion(self):
        current_row = self.tableWidget.currentRow()
        if current_row >= 0:
            item = self.tableWidget.item(current_row, 0)
            if item:
                item_id = item.text()
                self.items_to_delete.append(item_id)
            self.tableWidget.removeRow(current_row)

    def save_changes(self):
        con = sqlite3.connect('srm.db', check_same_thread=False)
        table_name = 'Goods'
        try:
            with con:
                cur = con.cursor()
            for item_id in self.items_to_delete:
                cur.execute(f"DELETE FROM {table_name} WHERE id = ?", (item_id,))
            for item in self.items_to_add:
                cur.executemany('''INSERT INTO Goods (id, name, quantity, price, store_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?)''', (item,))
            con.commit()
        except sqlite3.Error as e:
            print("Ошибка SQLite:", e)

        self.items_to_add.clear()
        self.items_to_delete.clear()

        self.main_window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

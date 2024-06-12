from PyQt5 import QtWidgets, QtCore
import sqlite3
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 951, 641))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search = QtWidgets.QPushButton(self.widget)
        self.search.setObjectName("search")
        self.horizontalLayout_4.addWidget(self.search)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_new = QtWidgets.QPushButton(self.widget)
        self.add_new.setObjectName("add_new")
        self.horizontalLayout_3.addWidget(self.add_new)
        self.dele = QtWidgets.QPushButton(self.widget)
        self.dele.setObjectName("dele")
        self.horizontalLayout_3.addWidget(self.dele)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Cancel = QtWidgets.QPushButton(self.widget)
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_2.addWidget(self.Cancel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.OK = QtWidgets.QPushButton(self.widget)
        self.OK.setObjectName("OK")
        self.horizontalLayout_2.addWidget(self.OK)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_new.clicked.connect(self.add_new_row)
        self.search.clicked.connect(self.search_data)
        self.OK.clicked.connect(self.save_data)
        self.dele.clicked.connect(self.mark_for_deletion)
        self.Cancel.clicked.connect(MainWindow.close)

        self.current_personal_id = 1
        self.main_window = MainWindow
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Personal ID", "Product ID", "Product Name", "Store ID", "Quantity", "Date", "Reason"])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Списать"))
        self.search.setText(_translate("MainWindow", "Поиск"))
        self.add_new.setText(_translate("MainWindow", "+"))
        self.dele.setText(_translate("MainWindow", "Удалить"))
        self.Cancel.setText(_translate("MainWindow", "ОТМЕНИТЬ"))
        self.OK.setText(_translate("MainWindow", "СОХРАНИТЬ"))

    def save_data(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        for row in range(self.tableWidget.rowCount()):
            id_item = self.tableWidget.item(row, 0)
            personal_id_item = self.tableWidget.item(row, 1)
            product_id_item = self.tableWidget.item(row, 2)
            store_id_item = self.tableWidget.item(row, 4)
            quantity_item = self.tableWidget.item(row, 5)
            date_item = self.tableWidget.item(row, 6)
            reason_item = self.tableWidget.item(row, 7)
            if all([personal_id_item, product_id_item, store_id_item, quantity_item, date_item, reason_item]):

                cursor.execute("SELECT MAX(id) FROM Write_of_products")
                max_id = cursor.fetchone()[0]
                if max_id is None:
                    max_id = 0
                id_value = max_id + 1
                personal_id_value = personal_id_item.text()
                product_id_value = product_id_item.text()
                store_id_value = store_id_item.text()
                quantity_value = quantity_item.text()
                date_value = date_item.text()
                reason_value = reason_item.text()
                cursor.execute("""
                    INSERT INTO Write_of_products (id, personal_id, product_id, store_id, quantity, date, reason)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (id_value, personal_id_value, product_id_value, store_id_value, quantity_value, date_value,
                      reason_value))
        conn.commit()
        conn.close()
        self.main_window.close()

    def show_search_results(self, results):
        self.search_results_window = QtWidgets.QWidget()
        self.search_results_window.setWindowTitle("Результат поиска")
        self.search_results_window.resize(400, 300)
        self.layout = QtWidgets.QVBoxLayout(self.search_results_window)

        self.listWidget = QtWidgets.QListWidget()
        for result in results:
            self.listWidget.addItem(
                f"ID: {result[0]}, Name: {result[1]}, Store ID: {result[4]}")

        self.layout.addWidget(self.listWidget)

        self.insert_button = QtWidgets.QPushButton("Добавить")
        self.insert_button.clicked.connect(self.insert_selected_result)
        self.layout.addWidget(self.insert_button)

        self.search_results_window.show()

    def search_data(self):
        query = self.lineEdit.text()
        if not query:
            return

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Product WHERE name LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()

        if results:
            self.show_search_results(results)

        conn.close()

    def add_new_row(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM Write_of_products")
        max_id = cursor.fetchone()[0]
        if max_id is None:
            max_id = 0
        id_value = max_id + 1
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(id_value)))
        self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(self.current_personal_id)))
        self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(datetime.now().strftime('%Y-%m-%d')))
        self.tableWidget.setItem(row_position, 7, QtWidgets.QTableWidgetItem(""))
        self.tableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(""))


    def insert_selected_result(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            data = selected_item.text().split(',')
            id_value = data[0].split(':')[1].strip()
            product_name_value = data[1].split(':')[1].strip()
            store_id_value = data[2].split(':')[1].strip()
            row_position = self.tableWidget.rowCount() - 1
            self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(id_value))
            self.tableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(product_name_value))
            self.tableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(store_id_value))

        self.search_results_window.close()

    def mark_for_deletion(self):
        current_row = self.tableWidget.currentRow()
        self.tableWidget.removeRow(current_row)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

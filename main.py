from PyQt5 import QtCore, QtGui, QtWidgets
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
import clients2, products, stores, personal, sell, acceptance, writeoff, transportation
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel
from DBfuntions import db, DataBase
from documents import generate_document  # Импортируем функцию из другого файла

class TransactionDialog(QtWidgets.QDialog):
    def __init__(self, transaction_data, headers, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Transaction Details")
        self.setGeometry(300, 300, 400, 300)

        layout = QtWidgets.QVBoxLayout()

        for key, value in transaction_data.items():
            label = QtWidgets.QLabel(f"{key}: {value}")
            layout.addWidget(label)

        self.setLayout(layout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("""
             QWidget{   
                
            }
        """)
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
        self.tableWidget.itemSelectionChanged.connect(self.on_item_selection_changed)

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

        # обновляем табличку
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(540, 115, 150, 30))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_refresh.setText("Обновить таблицу")

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
        self.pushButton_documents.clicked.connect(self.open_documents)  # Подключаем новую функцию
        self.pushButton_refresh.clicked.connect(self.update_table_data)

        self.set_access_level('admin')

        self.selected_row_data = []  # Инициализация атрибута для хранения данных выбранной строки

        self.db = DataBase()
        self.database1()
        self.tableWidget.cellClicked.connect(self.show_transaction_details)

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

    def update_table_data(self): #aaaa
        self.database1()

    def set_access_level(self, access_level):
        self.pushButton_change.setEnabled(False)
        self.pushButton_del.setEnabled(False)
        self.pushButton_get.setEnabled(False)
        self.pushButton_post.setEnabled(False)
        self.pushButton_documents.setEnabled(False)
        self.pushButton_rollback.setEnabled(False)
        self.pushButton_clients.setEnabled(False)
        self.pushButton_stores.setEnabled(False)
        self.pushButton_personal.setEnabled(False)
        self.pushButton__product.setEnabled(False)

        if access_level == 'admin':
            self.pushButton_change.setEnabled(True)
            self.pushButton_del.setEnabled(True)
            self.pushButton_get.setEnabled(True)
            self.pushButton_post.setEnabled(True)
            self.pushButton_documents.setEnabled(True)
            self.pushButton_rollback.setEnabled(True)
            self.pushButton_clients.setEnabled(True)
            self.pushButton_stores.setEnabled(True)
            self.pushButton_personal.setEnabled(True)
            self.pushButton__product.setEnabled(True)

        elif access_level == 'storekeeper':
            self.pushButton_change.setEnabled(True)
            self.pushButton_del.setEnabled(True)
            self.pushButton_get.setEnabled(True)
            self.pushButton_post.setEnabled(True)
            self.pushButton_documents.setEnabled(True)
            self.pushButton_rollback.setEnabled(True)
            self.pushButton_rollback.setEnabled(False)

        elif access_level == 'user':
            pass

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
        self.ui = transportation.Ui_Dialog()
        data = self.ui.exec_()
        line_text = self.lineEdit_2.text()
        line_text += data
        self.lineEdit_2.setText(line_text)

    def show_del(self):
        self.ui = writeoff.Ui_Dialog()
        data = self.ui.exec_()
        line_text = self.lineEdit_2.text()
        line_text += data
        self.lineEdit_2.setText(line_text)

    def show_get(self):
        self.ui = acceptance.Ui_Dialog()
        data = self.ui.exec_()
        line_text = self.lineEdit_2.text()
        line_text += data
        self.lineEdit_2.setText(line_text)

    def show_post(self):
        self.ui = sell.Ui_Dialog()
        data = self.ui.exec_()
        line_text = self.lineEdit_2.text()
        line_text += data
        self.lineEdit_2.setText(line_text)

    # def database1(self):
    #     con = sqlite3.connect('srm.db', check_same_thread=False)
    #     table_name = 'Transactions'
    #     with con:
    #         cur = con.execute(f"Pragma table_info ('{table_name}')")
    #         pragma_answer = cur.fetchall()
    #
    #         list_of_col = [i[1] for i in pragma_answer]
    #
    #         cur = con.execute(f"Select * From {table_name}")
    #         table_data = cur.fetchall()
    #         list_of_left_rows = [str(i[0]) for i in table_data]
    #
    #         self.tableWidget.setColumnCount(len(list_of_col))
    #         self.tableWidget.setHorizontalHeaderLabels(list_of_col)
    #         self.tableWidget.setRowCount(len(list_of_left_rows))
    #         self.tableWidget.setVerticalHeaderLabels(list_of_left_rows)
    #
    #         for i in range(len(table_data)):
    #             for j in range(len(table_data[i])):
    #                 self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(table_data[i][j])))

    def open_documents(self):
        # Показать диалог выбора операции
        # Здесь можно реализовать логику выбора операции пользователем
        # operations = "Продажа"  # Пример операции "человеческой", может быть изменено на выбор пользователя

        id_transaction = self.selected_row_data[0]
        print(id_transaction)
        list_data_transaction = db.get_transaction_by_id(id_transaction)
        operations = list_data_transaction[0][1]
        print(list_data_transaction)
        print(operations)

        # Генерируем документ с использованием данных выбранной строки
        generate_document(operations, list_data_transaction[0])

        # Устанавливаем текст в lineEdit_2
        self.lineEdit_2.setText(
            f"Сформирован документ по транзакции - {operations}. Некоторые чекануться, а кто-то даже охереет!")

    """метод on_item_selection_changed, который вызывается при изменении выделения в tableWidget. В этом методе 
    получаются данные из выделенной строки и выводятся в консоль"""

    def on_item_selection_changed(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            self.selected_row_data = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(selected_row, column)
                if item:
                    self.selected_row_data.append(item.text())
            print("Selected row data:", self.selected_row_data)

    # def open_documents(self):
    #
    #     options = QtWidgets.QFileDialog.Options()
    #     fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите документ", "", "All Files (*);;Word Files "
    #                                                                                        "(*.docx);;Excel Files ("
    #                                                                                        "*.xlsx)", options=options)
    #     if fileName:
    #         try:
    #             os.startfile(fileName)
    #         except Exception as e:
    #             print(f"Не удалось открыть файл {fileName}. Ошибка: {e}")

    # def open_documents(self):
    #     # Показать диалог выбора операции
    #     operations = ["Продажа", "Перемещение", "Списание", "Приемка"]
    #     operation, ok = QtWidgets.QInputDialog.getItem(None, "Выберите операцию", "Операция:", operations, 0, False)
    #     if ok and operation:
    #         try:
    #             generate_document(operation)
    #         except Exception as e:
    #             QtWidgets.QMessageBox.critical(None, "Ошибка", f"Не удалось создать документ. Ошибка: {e}")

    def database1(self):
        self.conn = sqlite3.connect('srm.db')
        self.c = self.conn.cursor()

        self.c.execute('SELECT * FROM Transactions')
        data = self.c.fetchall()

        if data:
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

            headers = [description[0] for description in self.c.description]
            self.tableWidget.setHorizontalHeaderLabels(headers)

    def show_transaction_details(self, row, column):
        try:
            transaction_id = self.tableWidget.item(row, 0).text()
            transaction_type = self.tableWidget.item(row, 1).text()

            transaction_data = self.db.get_trans(transaction_id, transaction_type)
            headers = self.db.get_trans_info(transaction_type)

            self.dialog = TransactionDialog(transaction_data, headers)
            self.dialog.exec_()

        except Exception as e:
            print(f"Error in show_transaction_details: {e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.set_access_level('admin')
    sys.exit(app.exec_())




# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sell1.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DBfuntions import db
from PyQt5.QtWidgets import QMessageBox
import datetime


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(957, 895)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 341, 21))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 921, 281))
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 211, 21))
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 380, 921, 281))
        self.tableWidget_2.setObjectName("tableWidget_2")
        # self.tableWidget_2.setColumnCount(0)
        # self.tableWidget_2.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 670, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(760, 680, 181, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(550, 680, 201, 41))
        self.label_3.setObjectName("label_3")
        # self.label_4 = QtWidgets.QLabel(self)
        # self.label_4.setGeometry(QtCore.QRect(20, 760, 151, 41))
        # self.label_4.setObjectName("label_4")
        # self.comboBox = QtWidgets.QComboBox(self)
        # self.comboBox.setGeometry(QtCore.QRect(180, 761, 261, 31))
        # self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 830, 221, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 830, 221, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.table_gen()
        # self.set_combobox_items()

        self.person = db.get_username()

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(550, 750, 221, 41))
        self.label_5.setObjectName("label_5")
        self.label_5.setText(f'Ответственный: {self.person[1]}')

        self.tableWidget.cellDoubleClicked.connect(self.double_clicked)

        self.tableWidget_2.cellChanged.connect(self.cell_changed)

        self.pushButton.clicked.connect(self.delete_btn)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.save_data)

        self.log_data = ''
        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Списать"))
        self.label.setText(_translate("Dialog", "Выберите продукты из списка:"))
        self.label_2.setText(_translate("Dialog", "Выбранные продукты:"))
        self.pushButton.setText(_translate("Dialog", "Удалить"))
        self.label_3.setText(_translate("Dialog", "Итоговая сумма"))
        # self.label_4.setText(_translate("Dialog", "Ответственный"))
        self.pushButton_2.setText(_translate("Dialog", "Отменить"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))

    def table_gen(self):
        goods_lst = db.get_goods()
        headers_one = ['articul', 'name', 'price', 'ex_time', 'quant in warehouse']
        headers_two = ['articul', 'name', 'price', 'ex_time', 'quantity']

        self.tableWidget.setColumnCount(len(headers_one))
        self.tableWidget.setRowCount(len(goods_lst))
        self.tableWidget.setHorizontalHeaderLabels(headers_one)

        self.tableWidget_2.setColumnCount(len(headers_two))
        self.tableWidget_2.setHorizontalHeaderLabels(headers_two)

        for row, i in enumerate(goods_lst):
            for col, j in enumerate(i):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(j)))

    # def set_combobox_items(self):
    #     combobox_items = ['Микошевский Эдуард Викторович', 'Ловицкий Кирилл Антонович']
    #     for i in combobox_items:
    #         self.comboBox.addItem(i)

    def double_clicked(self, row, column):
        data_row = self.row_data_from_table1(row)
        data_row[4] = '' # quantity

        data_lst = self.data_from_table2()
        for data in data_lst:
            data[4] = ''
        if data_row not in data_lst: # если еще нет такой строки во второй таблице, то добавляем
            self.tableWidget_2.insertRow(0)
            for col, data in enumerate(data_row):
                self.tableWidget_2.setItem(0, col, QtWidgets.QTableWidgetItem(str(data)))

    def cell_changed(self, row, column):
        # if column == 4:
        data_changed_row = self.row_data_from_table2(row)
        if data_changed_row[4] != '': # если поменялось именно количество, то ниже меняем итоговую сумму:
            self.set_total_sum()

    def delete_btn(self):
        row = self.tableWidget_2.currentRow()
        self.tableWidget_2.removeRow(row)

        self.set_total_sum()

    def save_data(self):
        if self.quantity_check():  # если введенное количество не больше того, что есть на складе
            data_lst = self.data_from_table2()
            person_id = self.person[0]
            now = datetime.datetime.now()
            transaction_id = db.insert_transact(['Списать', person_id, now, ''])
            for data_row in data_lst:
                db.decrease_cnt(data_row[1], data_row[3], data_row[4])

            self.log_data = 'Проведена операция "Списать". '
            self.close()
        else:
            QMessageBox.warning(None, "Ошибка", "Вы указали количество больше, чем есть на складе!")

    def set_total_sum(self):
        data_lst = self.data_from_table2()
        sum = 0
        for data_row in data_lst:
            if data_row[4] != '':
                sum += round(float(data_row[2]) * int(data_row[4]), 2)
        self.lineEdit.setText(str(sum))

    def row_data_from_table1(self, row):
        data_lst = []
        for col in range(self.tableWidget.columnCount()):
            it = self.tableWidget.item(row, col)
            text = it.text() if it is not None else ""
            data_lst.append(text)
        return data_lst

    def row_data_from_table2(self, row):
        data_lst = []
        for col in range(self.tableWidget_2.columnCount()):
            it = self.tableWidget_2.item(row, col)
            text = it.text() if it is not None else ""
            data_lst.append(text)
        return data_lst

    def data_from_table2(self):
        lst = []
        for row in range(self.tableWidget_2.rowCount()):
            data = []
            for col in range(self.tableWidget_2.columnCount()):
                it = self.tableWidget_2.item(row, col)
                text = it.text() if it is not None else ""
                data.append(text)
            lst.append(data)
        return lst

    def quantity_check(self):
        data_lst_tb2 = self.data_from_table2()
        goods_lst = db.get_goods()

        for data_row in data_lst_tb2:
            for good in goods_lst:
                if data_row[1] == good[1]:
                    if int(good[4]) < int(data_row[4]):
                        return False
        return True

    def exec_(self):
        super().exec_()
        return self.log_data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())

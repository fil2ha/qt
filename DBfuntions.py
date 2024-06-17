import sqlite3 as sl

class DataBase():
    def __init__(self):
        self.connection = sl.connect('srm.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    #транзакция по id
    def get_transaction_by_id(self, id):
        self.cursor.execute("SELECT * FROM Transactions WHERE id = ?", (id,))
        return self.cursor.fetchall()

    # ФУНКЦИЯ ВЫВОДЯЩАЯ ВСЕ ТРАНЗАКЦИИ
    def get_transactions(self):
        self.cursor.execute('SELECT * FROM Transactions')
        return self.cursor.fetchall()

    #товары + коли-во
    def get_goods(self):
        self.cursor.execute('''
            SELECT Goods.articul, Goods.name, Goods.price, Goods.ex_time,  GoodsWarehouse.count FROM Goods
            JOIN GoodsWarehouse ON Goods.id = GoodsWarehouse.good_id
        ''')
        return self.cursor.fetchall()
    # возвращает список картежей
    # последний элемент кортежа количество

    #товары + склад + кол-во
    def get_goods_with_wh(self):
        self.cursor.execute('''
            SELECT Goods.articul, Goods.name, Goods.price, Goods.ex_time, GoodsWarehouse.count, Warehouse.name FROM Goods
            JOIN GoodsWarehouse ON Goods.id = GoodsWarehouse.good_id
            JOIN WareHouse ON WareHouse.id = GoodsWarehouse.warehouse_id
        ''')
        return self.cursor.fetchall()
    #возвращает список картежей
    #последний элемент кортежа имя склада

    # функции дял уменьшения и увеличения кол-ва на складе определённого товара
    def decrease_cnt(self, name, ex_time, cnt):
        self.cursor.execute(f"""
                                UPDATE GoodsWarehouse 
                                SET count = count - ?
                                WHERE id IN (
                                SELECT id FROM Goods 
                                WHERE name = ? AND ex_time = ?
                            )""", (cnt, name, ex_time))
        self.connection.commit()
    def increase_cnt(self, name, ex_time, cnt):
        self.cursor.execute(f"""
                                    UPDATE GoodsWarehouse 
                                    SET count = count + ?
                                    WHERE id IN (
                                    SELECT id FROM Goods 
                                    WHERE name = ? AND ex_time = ?
                                )""", (cnt, name, ex_time))
        self.connection.commit()


    # функция для добавления транзакции
    def insert_transact(self, list):
        pass



db = DataBase()

print(db.get_transactions())









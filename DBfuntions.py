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
    # возвращает список картежей
    # последний элемент кортежа имя склада

    # функции дял уменьшения и увеличения кол-ва на складе определённого товара
    def decrease_cnt(self, name, ex_time, cnt):#исправить
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
                                    WHERE id IN 
                                    (
                                        SELECT id FROM Goods 
                                        WHERE name = ? AND ex_time = ?
                                    )
                                """, (cnt, name, ex_time))
        self.connection.commit()


    # функция для добавления транзакции и возвращегия id этой транзакции
    def insert_transact(self, list):
        self.cursor.execute("INSERT INTO Transactions (type, who, time, PS) VALUES (?, ?, ?, ?)", list)
        self.connection.commit()
        self.cursor.execute("SELECT id  FROM Transactions WHERE type = ? AND who = ? AND time = ? AND PS = ?", (list[0], list[1],list[2], list[3],))
        return self.cursor.lastrowid #получает последний id

    #функция, которая возвращает имена складов
    def get_wh_names(self):
        self.cursor.execute("SELECT name FROM Warehouse")
        temp = []
        temp_list = self.cursor.fetchall()
        for _ in temp_list:
            for __ in _:
                if __ in temp:
                    continue
                else:
                    temp.append(__)
        return temp

    #6) заносит значения в sell
    def insert_sell(self, s_list, sd_list):
        self.cursor.execute("INSERT INTO Sell (transaction_id, client, from_wh) VALUES(?, ?, ?)", s_list)
        self.connection.commit()
        temp_sell_id = self.cursor.lastrowid
        self.cursor.execute("SELECT id FROM Goods WHERE name = ? AND ex_time = ?", (sd_list[0], sd_list[1]))
        temp_good_id = self.cursor.fetchone()[0]
        # Вставка в таблицу SellData
        self.cursor.execute("INSERT INTO SellData (good_id, sell_id, count, expire_date) VALUES (?, ?, ?, ?)",
                            (temp_good_id, temp_sell_id, sd_list[2], sd_list[3]))
        self.connection.commit()


db = DataBase()










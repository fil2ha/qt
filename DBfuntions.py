import sqlite3 as sl

class DataBase():
    def __init__(self):
        self.connection = sl.connect('srm.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.person_id = 0
        self.person_name = ''

    def login_admin(self, username, password):
        self.cursor.execute("SELECT * FROM Permission WHERE login=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user:
            self.person_id = user[0]
            self.person_name = user[2]
            return user[2]
        else:
            return ""

    def get_username(self):
        return [self.person_id, self.person_name]
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
            SELECT Goods.articul, Goods.name, Goods.price, Goods.ex_time, Warehouse.name, GoodsWarehouse.count FROM Goods
            JOIN GoodsWarehouse ON Goods.id = GoodsWarehouse.good_id
            JOIN WareHouse ON WareHouse.id = GoodsWarehouse.warehouse_id
        ''')
        return self.cursor.fetchall()
    # возвращает список картежей
    # последний элемент кортежа имя склада

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

    # доделать
    def increase_cnt(self, list_good, list_warehouse):
        self.cursor.execute(f"""
                                SELECT * FROM Goods WHERE name = ? AND ex_time = ? VALUES(?, ?)
                            """, )
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
    def insert_sell(self, s_list):
        self.cursor.execute("INSERT INTO Sell (transaction_id, client, from_wh) VALUES(?, ?, ?)", s_list)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_SellData(self, sd_list):
        self.cursor.execute("SELECT id FROM Goods WHERE name = ? AND ex_time = ?", (sd_list[0], sd_list[1]))
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute("INSERT INTO SellData (good_id, sell_id, count, expire_date) VALUES (?, ?, ?, ?)",
                            (temp_good_id, sd_list[2], sd_list[3], sd_list[4]))
        self.connection.commit()

    def insert_accept(self, list_a):
        self.cursor.execute("INSERT INTO acceptance (transaction_id, to_wh, Client) VALUES(?, ?, ?)", list_a)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_accData(self, list_ad):
        self.cursor.execute("SELECT id FROM Goods WHERE name = ? AND ex_time = ?", (list_ad[0], list_ad[1]))
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute("INSERT INTO AcceptanceData (good_id, acceptance_id, count, expire_date) VALUES (?, ?, ?, ?)",
                            (temp_good_id, list_ad[2], list_ad[3], list_ad[4]))
        self.connection.commit()

    def insert_wo(self, list_wo):
        self.cursor.execute("INSERT INTO WriteOff (transaction_id, from_wh) VALUES(?, ?)", list_wo)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_wod(self, list_wod):
        self.cursor.execute("SELECT id FROM Goods WHERE name = ? AND ex_time = ?", (list_wod[0], list_wod[1]))
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO WritOffData (good_id, acceptance_id, count, expire_date) VALUES (?, ?, ?, ?)",
            (temp_good_id, list_wod[2], list_wod[3], list_wod[4]))
        self.connection.commit()

    def insert_trans(self, list_t):
        self.cursor.execute("INSERT INTO Transportation (transaction_id, from_wh, to_wh) VALUES(?, ?, ?)", list_t)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_transData(self, list_td):
        self.cursor.execute("SELECT id FROM Goods WHERE name = ? AND ex_time = ?", (list_td[0], list_td[1]))
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO TransportationData (good_id, transportation_id, count, expire_date) VALUES (?, ?, ?, ?)",
            (temp_good_id, list_td[2], list_td[3], list_td[4]))
        self.connection.commit()

    def get_clients(self):
        self.cursor.execute("SELECT FIO FROM Client")
        temp = []
        for _ in self.cursor.fetchall():
            for __ in _:
                temp.append(__)
        return temp



db = DataBase()








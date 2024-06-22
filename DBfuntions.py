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
    def decrease_cnt(self, list_good, cnt, wh_name):
        #[articul, name, price, ex_time]
        self.cursor.execute("BEGIN TRANSACTION;")

        self.cursor.execute("""
                    UPDATE GoodsWarehouse 
                    SET count = count - ? 
                    WHERE good_id IN (
                        SELECT id FROM Goods 
                        WHERE name = ? AND ex_time = ? AND articul = ? AND price = ?
                    )
                """, (cnt, list_good[1], list_good[3],  list_good[0], list_good[2]))

        self.cursor.execute("""
                    DELETE FROM GoodsWarehouse 
                    WHERE count <= 0
                """)
        self.connection.commit()

    # доделать
    def increase_cnt(self, list_good, cnt, wh_name, acc_id, ex_date):
        #[articul, name, price, ex_time, img]
        self.cursor.execute("""
                SELECT * FROM Goods WHERE name = ? AND ex_time = ? AND articul = ? AND price = ?
                """, (list_good[1], list_good[3], list_good[0], list_good[2]))
        temp = self.cursor.fetchall()
        self.cursor.execute(f"SELECT id FROM warehouse WHERE name = '{wh_name}'")
        wh_id = self.cursor.fetchone()[0]
        if temp:
            self.cursor.execute("""
                UPDATE GoodsWarehouse 
                SET count = count + ? 
                WHERE id IN (
                    SELECT id FROM Goods 
                    WHERE name = ? AND ex_time = ? AND articul = ? AND price = ?
                )
            """, (cnt, list_good[1], list_good[3], list_good[0], list_good[2]))
            self.connection.commit()
        else:
            self.cursor.execute("""
                INSERT INTO Goods (articul, name, price, ex_time, img) VALUES (?, ?, ?, ?, ?)
            """, list_good)
            id = self.cursor.lastrowid
            self.cursor.execute("""
                INSERT INTO GoodsWarehouse (good_id, warehouse_id, count, expire_date, accept_date, accept_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (id, wh_id, cnt, ex_date, 1, acc_id))
            self.connection.commit()

    # функция для добавления транзакции и возвращегия id этой транзакции
    def insert_transact(self, list):
        self.cursor.execute("INSERT INTO Transactions (type, who, time, PS) VALUES (?, ?, ?, ?)", list)
        self.connection.commit()
        self.cursor.execute("SELECT id  FROM Transactions WHERE type = ? AND who = ? AND time = ? AND PS = ?",
                            (list[0], list[1],list[2], list[3],))
        return self.cursor.lastrowid
    #получает последний id

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

    def insert_SellData(self, list_good, sell_list):
        #list_good  [articul, name, price, ex_time]
        #sell_list [sell_id, count, expire_date]
        self.cursor.execute("SELECT id FROM Goods WHERE articul = ? AND name = ? AND price = ? AND ex_time = ?", list_good)
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute("INSERT INTO SellData (good_id, sell_id, count, expire_date) VALUES (?, ?, ?, ?)",
                            (temp_good_id, sell_list[0], sell_list[1], sell_list[2],))
        self.connection.commit()

    def insert_accept(self, list_a):
        self.cursor.execute("INSERT INTO acceptance (transaction_id, to_wh, Client) VALUES(?, ?, ?)", list_a)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_accData(self, list1, list2):
        #list1 [articul, name, price, ex_time]
        #list2 [acceptance_id, count, expire_date]
        self.cursor.execute("SELECT id FROM Goods WHERE name = ? AND ex_time = ? AND price = ? AND articul = ?",
                            (list1[1], list1[3], list1[2],list1[0]))
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute("INSERT INTO AcceptanceData (good_id, acceptance_id, count, expire_date) VALUES (?, ?, ?, ?)",
                            (temp_good_id, list2[0], list2[1], list2[2]))
        self.connection.commit()

    def insert_wo(self, list_wo):
        self.cursor.execute("INSERT INTO WriteOff (transaction_id, from_wh) VALUES(?, ?)", list_wo)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_wod(self, list_good, list_wod):
        #list_wod [write_of_id, count, expire_date]
        self.cursor.execute("SELECT id FROM Goods WHERE articul = ? AND name = ? AND price = ? AND ex_time = ?", list_good)
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO WriteOffData (good_id,  write_of_id, count, expire_date) VALUES (?, ?, ?, ?)",
            (temp_good_id, list_wod[0], list_wod[1], list_wod[2]))
        self.connection.commit()

    def insert_trans(self, list_t):
        self.cursor.execute("INSERT INTO Transportation (transaction_id, from_wh, to_wh) VALUES(?, ?, ?)", list_t)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_transData(self,  list_good, list_td):
        self.cursor.execute("SELECT id FROM Goods WHERE articul = ? AND name = ? AND price = ? AND ex_time = ?",
                            list_good)
        temp_good_id = self.cursor.fetchone()[0]
        self.cursor.execute(
            "INSERT INTO TransportationData (good_id, transportation_id, count, expire_date) VALUES (?, ?, ?, ?)",
            (temp_good_id, list_td[0], list_td[1], list_td[2]))
        self.connection.commit()

    def get_clients(self):
        self.cursor.execute("SELECT FIO FROM Client")
        temp = []
        for _ in self.cursor.fetchall():
            for __ in _:
                temp.append(__)
        return temp

    def transit(self, list_good, name_to, name_from, cnt):
        self.cursor.execute("SELECT id FROM Goods WHERE articul = ? AND name = ? AND price = ? AND ex_time = ?",
                            list_good)
        good_id = self.cursor.fetchone()[0]
        w_i_to = db.get_wh_id(name_to)
        w_i_from = db.get_wh_id(name_from)
        self.cursor.execute(f"SELECT * FROM GoodsWarehouse WHERE good_id = {good_id} AND warehouse_id = {w_i_to}")
        tp = self.cursor.fetchone()
        if not tp:
            self.cursor.execute("""
                            UPDATE GoodsWarehouse 
                            SET count = count - ? 
                            WHERE good_id = ?
                            AND warehouse_id = ? 
                        """, (cnt, good_id, w_i_from))
            self.cursor.execute("""
                INSERT INTO GoodsWarehouse (good_id, warehouse_id, count, expire_date, accept_date, accept_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (good_id, w_i_to, cnt, 12, 14, 1))
            self.connection.commit()
        else:
            self.cursor.execute("""
                UPDATE GoodsWarehouse 
                SET count = count - ? 
                WHERE good_id = ?
                AND warehouse_id = ? 
            """, (cnt, good_id, w_i_from))
            self.cursor.execute("""
                            UPDATE GoodsWarehouse 
                            SET count = count + ? 
                            WHERE good_id = ?
                            AND warehouse_id = ? 
                        """, (cnt, good_id, w_i_to))
            self.cursor.execute(
                f"SELECT count FROM GoodsWarehouse WHERE good_id = {good_id} AND warehouse_id = {w_i_from}")
            current_count = self.cursor.fetchone()[0]
            if current_count == 0:
                self.cursor.execute("""
                    DELETE FROM GoodsWarehouse 
                    WHERE good_id = ?
                    AND warehouse_id = ? 
                """, (good_id, w_i_from))
            self.connection.commit()

    def get_wh_id(self, name):
        self.cursor.execute("SELECT id FROM Warehouse WHERE name = ?",(name,))
        return self.cursor.fetchone()[0]

    # ДЛЯ ФЕДИ
    def reserch(self, rsh_type, rsh_str, table_name):
        self.cursor.execute(f'Pragma table_info ("{table_name}")')
        columns = [col[1] for col in self.cursor.fetchall()]
        if rsh_type == '_A':
            conditions = " OR ".join(f"{col} LIKE '%{rsh_str}'" for col in columns)
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {conditions}")
        elif rsh_type == '_A_':
            conditions = " OR ".join(f"{col} LIKE '%{rsh_str}%'" for col in columns)
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {conditions}")
        elif rsh_type == 'A_':
            conditions = " OR ".join(f"{col} LIKE '{rsh_str}%'" for col in columns)
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {conditions}")

        result = self.cursor.fetchall()

        if not result:
            return []
        else:
            return result

        # ДЛЯ МИРОСЛАВА

    def get_trans(self, id_trans, type):
        self.cursor.execute(f"SELECT * FROM {type} WHERE transaction_id = {id_trans}")
        temp = list(self.cursor.fetchall()[0])
        tm_id = temp[0]
        query = type.lower() + '_id'
        self.cursor.execute(f"SELECT * FROM {type+'Data'} WHERE {query} = {tm_id}")
        for _ in self.cursor.fetchall()[0]:
            temp.append(_)
        return temp

    def get_trans_info(self, type):
        self.cursor.execute(f'Pragma table_info ("{type}")')
        temp = []
        for _ in self.cursor.fetchall():
                temp.append(_[1])
        query = type+'Data'
        self.cursor.execute(f'Pragma table_info ("{query}")')
        for _ in self.cursor.fetchall():
                temp.append(_[1])
        return(temp)



db = DataBase()


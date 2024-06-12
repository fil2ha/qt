import sqlite3


connection = sqlite3.connect('database.db')

cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Personal (
# id INTEGER PRIMARY KEY,
# name VARCHAR(50),
# phone VARCHAR(30),
# address VARCHAR(50),
# info TEXT
# )
# ''')

# personal_data = [
#     (1, 'John Doe', '123456789', '123 Main St', 'Lorem ipsum dolor sit amet...'),
#     (2, 'Jane Smith', '987654321', '456 Elm St', 'Consectetur adipiscing elit...'),
#     (3, 'Alice Johnson', '555123456', '789 Oak St', 'Sed do eiusmod tempor incididunt...')
# ]
#
# cursor.executemany('''
# INSERT INTO Personal (id, name, phone, address, info) VALUES (?, ?, ?, ?, ?)
# ''', personal_data)


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Permissions (
# id INTEGER PRIMARY KEY,
# personal_id INT,
# login VARCHAR(10),
# password VARCHAR(20),
# admin BOOLEAN,
# chief BOOLEAN,
# responsible BOOLEAN,
# user BOOLEAN
# )
# ''')


# permissions_data = [
#     (1, 1, 'johndoe', 'johndoe', 1, 0, 1, 1),
#     (2, 2, 'janes', 'janepass', 0, 1, 1, 1),
#     (3, 3, 'alicej', 'alice123', 0, 0, 0, 1)
# ]
#
# cursor.executemany('''
# INSERT INTO Permissions (id, personal_id, login, password, admin, chief, responsible, user) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# ''', permissions_data)

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Clients (
# id INTEGER PRIMARY KEY,
# name VARCHAR(50),
# ind_number INT,
# ceo VARCHAR(30),
# phone VARCHAR(30),
# email VARCHAR(30),
# address VARCHAR(50),
# current_account VARCHAR(28),
# bank VARCHAR(20),
# bik VARCHAR(20),
# bank_address VARCHAR(50),
# info TEXT
# )
# ''')
#
# clients_data = [
#     (1, 'Real', 192548985, 'Mrs Brown', '+375291555555', 'office@real.by', 'Pobediteley 1 of 23', 'BY01UNBS12123232434312342134', 'BSBbank', 'UNBSBY2X', 'pobediteley 23', 'new client'),
#     (2, 'Favorit', 101505606, 'Carl Jameson', '+375447777777', 'office@fav.by', 'Nezavisimisti 13 office 1', 'BY01MTBK1212UU32434312342134', 'MTBank', 'MTBKBY2X', 'Tolstogo 4', 'goverment client')
# ]
#
# cursor.executemany('''
# INSERT INTO Clients (id, name, ind_number, ceo, phone, email, address, current_account, bank, bik, bank_address, info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# ''', clients_data)
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Transactions (
# id INTEGER PRIMARY KEY,
# invoice INT,
# invoice_date DATE,
# paid BOOLEAN,
# paid_date DATE
# )
# ''')
#
# transactions_data = [
#     (1, 1, '2024-05-01', True, "2004-05-05"),
#     (2, 2, '2024-05-06', False, None)
# ]
#
# cursor.executemany('''
# INSERT INTO Transactions (id, invoice, invoice_date, paid, paid_date) VALUES (?, ?, ?, ?, ?)
# ''', transactions_data)
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Product (
# id INTEGER PRIMARY KEY,
# name VARCHAR(50),
# quantity REAL(5, 2),
# price REAL(5, 2),
# store_id INT,
# description TEXT,
# image VARCHAR(50)
# )
# ''')

product_data = [
    (2, 'milk111', 50, 2, 1, 'white product', 'https://milk.jpg'),
    (3, 'beer', 250, 1.5, 2, 'beautiful drink', 'https://beer.jpg'),
    (4, 'mil5555k', 50, 2, 1, 'white product', 'https://milk.jpg'),
    (5, 'beer555', 250, 1.5, 2, 'beautiful drink', 'https://beer.jpg')
]

cursor.executemany('''
INSERT INTO Product (id, name, quantity, price, store_id, description, image) VALUES (?, ?, ?, ?, ?, ?, ?)
''', product_data)

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Store (
# id INTEGER PRIMARY KEY,
# name VARCHAR(50),
# geolocation VARCHAR(80)
# )
# ''')
#
# store_data = [
#     (1, 'main_store', '54.6666666, 34.5555555'),
#     (2, 'south_store', '54.666555, 34.555543')
# ]
#
# cursor.executemany('''
# INSERT INTO Store (id, name, geolocation) VALUES (?, ?, ?)
# ''', store_data)
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Write_of_products (
# id INTEGER PRIMARY KEY,
# personal_id INT,
# product_id INT,
# store_id INT,
# quantity REAL(5, 2),
# date DATE,
# reason VARCHAR(50)
# )
# ''')
#
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Displacement (
# id INTEGER PRIMARY KEY,
# personal_id INT,
# product_id INT,
# store_id_out INT,
# store_id_in INT,
# quantity REAL(5, 2),
# date DATE,
# complete BOOLEAN
# )
# ''')

connection.commit()
connection.close()
import sqlite3
import random
from faker import Faker

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# ====================================================
# create tables
# create_users_table_sql = "CREATE TABLE IF NOT EXISTS  users(id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, address TEXT);"
# cretea_account_table_sql = """
#     CREATE TABLE IF NOT EXISTS 
#     accounts(
#         id INTEGER PRIMARY KEY,
#         user_id INTEGER,
#         balance DECIMAL(10, 2), 
#         FOREIGN KEY (user_id) REFERENCES users(id)
#     )
#     """
# cursor.execute(create_users_table_sql)
# cursor.execute(cretea_account_table_sql)
# ====================================================

# ====================================================
# Insert Dummy Data
# fake = Faker()

# def insert_random_users(num_users):
#     for _ in range(num_users):
#         full_name = fake.name()
#         address = fake.address().replace("\n", ", ")
#         cursor.execute("INSERT INTO users (full_name, address) VALUES (?, ?)", (full_name, address))
#     connection.commit()

# def insert_random_accounts():
#     cursor.execute("SELECT id FROM users")
#     user_ids = [row[0] for row in cursor.fetchall()]

#     for user_id in user_ids:
#         balance = round(random.uniform(0, 10000), 2)
#         cursor.execute("INSERT INTO accounts (user_id, balance) VALUES (?, ?)", (user_id, balance))
#     connection.commit()

# num_users = 10
# insert_random_users(num_users)
# insert_random_accounts()
# ====================================================


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
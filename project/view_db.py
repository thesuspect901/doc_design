import sqlite3

DB_FILE = "discord.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

print("=== Таблиці в базі ===")

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

for table in tables:
    print(table[0])

print("\n=== Користувачі ===")

cursor.execute("SELECT * FROM users LIMIT 10")

for row in cursor.fetchall():
    print(row)

print("\n=== Чати ===")

cursor.execute("SELECT * FROM chats")

for row in cursor.fetchall():
    print(row)

print("\n=== Повідомлення (10) ===")

cursor.execute("SELECT * FROM messages LIMIT 10")

for row in cursor.fetchall():
    print(row)

conn.close()
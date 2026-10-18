import sqlite3

connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)")
print("Напишіть 1 для регистрації, або 2 для входу")
choice = input("Ваш вибір: ")

def registration():
    if choice == "1":
        login = input("Ваш логін: ")
        password = input("Ваш пароль: ")
        cur.execute("SELECT * FROM users WHERE login = ?", (login,))
        if cur.fetchone():
            print("Цей логін вже існує!")
        else:
            cur.execute("INSERT INTO users VALUES (?, ?)",(login, password))
            connection.commit()
            print("Реєстрація успішна!")

def login():
    if choice == "2":
        login = input("Ваш логін: ")
        password = input("Ваш пароль: ")
        cur.execute("SELECT * FROM users WHERE login = ? AND password = ?",(login, password))
        if cur.fetchone():
            print("Вхід успішний!")
        else:
            print("Вхід неможливий: неправильний логін або пароль")

registration()
login()

connection.close()

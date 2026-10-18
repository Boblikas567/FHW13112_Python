import sqlite3

connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS transactions (id TEXT, amount TEXT, type TEXT, category TEXT, date TEXT, description TEXT)")

print("💰 ОСОБИСТИЙ ФІНАНСОВИЙ МЕНЕДЖЕР. 1-Додати дохід, 2-Додати витрату, 3-Переглянути всі операції, 4-Редагувати або видалити операцію, 5-Переглянути баланс, 6-Вихід")
choice = input("Ваш вибір: ")

def leave():
    if choice == "6":
        print("До побачення!")

def balance():
    if choice == "5":
        print("10000 грн")

def add_money():
    if choice == "1":
        amount = input("Скільки додасте?: ")
        category = input("Категорія доходу: ")
        date = input("Дата: ")
        description = input("Опис: ")
        cur.execute("""INSERT INTO transactions(id, amount, type, category, date, description)VALUES (?, ?, ?, ?, ?, ?)""",("1", amount, "вхід", category, date, description))

def modify_action():
    if choice == "4":
        pass

def watch_action():
    if choice == "3":
        print("Зайдіть до таблиці! Всі ваші операції там!")

balance()
leave()
add_money()
watch_action()

connection.commit()
connection.close()
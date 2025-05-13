import sqlite3
con = sqlite3.connect("I love drink.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS drinks
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(30),
               ingridients TEXT,
               degree FLOAT,
               price INTEGER,
               stored INTEGER)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS cocktails
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(30),
               degree FLOAT,
               constituents TEXT,
               ingridients TEXT,
               price INTEGER,
               stored INTEGER)""")

def sale():
    print('Cклад напитков (id, название, количество):')
    cursor.execute("SELECT id, name, stored FROM drinks")
    drinks = cursor.fetchall()
    for i in drinks:
        print(*i)
    print('Cклад коктейлей (id, название, количество):')
    cursor.execute("SELECT id, name, stored FROM cocktails")
    cocktails = cursor.fetchall()
    for i in cocktails:
        print(*i)
    name = input("Введите назваие коктейля или напитка, который хотите продать: ")
    cursor.execute("SELECT COALESCE(c.stored, 0)+COALESCE(d.stored,0) FROM cocktails c FULL JOIN drinks d WHERE c.name = ? OR d.name = ?", [name, name])
    x = cursor.fetchone()
    if x is None or x[0] == 0:
        print("Такого продукта нет на складе")
    else:
        cursor.execute("UPDATE drinks SET stored = stored-1 WHERE stored > 0 AND name =?", [name])
        con.commit()
        cursor.execute("UPDATE cocktails SET stored = stored-1 WHERE stored > 0 AND name =?", [name])
        con.commit()
        print("Продано 1 шт", name)

def restocking():
    a = input("1 - добавить коктейль\n2 - добавить напиток\n")
    if a == '1':
        name = input('Введите название: ')
        print("Список доступных напитков:")
        cursor.execute("SELECT id, name FROM drinks")
        print(cursor.fetchall())
        constituents = input('Введите состав коктейля (id напитков через пробел): ').split()
        sum = 0.0
        for id in constituents:
            cursor.execute("SELECT degree FROM drinks WHERE id =?", [id])
            sum += cursor.fetchone()[0]
        degree = sum/len(constituents)
        constituents = ' '.join(map(str, constituents))
        ingridients = input('Введите ингридиенты: ')
        price = int(input('Введите цену коктейля: '))
        stored = int(input("Введите количество коктейлей: "))
        cursor.execute("INSERT INTO cocktails (name, constituents, degree, ingridients, price, stored) VALUES (?, ?, ?, ?, ?, ?)", (name, constituents, degree, ingridients, price, stored))
        con.commit()
    elif a == '2':
        name = input('Введите название: ')
        ingridients = input('Введите ингридиенты: ')
        degree = float(input('Введите крепость напитка: '))
        price = int(input('Введите цену напитка: '))
        stored = int(input("Введите количество напитков: "))
        cursor.execute("INSERT INTO drinks (name, ingridients, degree, price, stored) VALUES (?, ?, ?, ?, ?)", (name, ingridients, degree, price, stored))
        con.commit()
    else:
        return


while True:
    a = input('\n'
          '1 - Продажа коктейлей и алкогольных напитков\n'
          '2 - Пополнение запасов\n')
    if a == '1':
        sale()
    elif a == '2':
        restocking()
    else:
        break
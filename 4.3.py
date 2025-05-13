import psutil
import sqlite3
from datetime import datetime
con = sqlite3.connect("system_monitor.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cpu
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               time DATETIME,
               cpu_percent TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS memory
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               time DATETIME,
               used REAL,
               percent REAL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS disk
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              time DATETIME,
              name TEXT,
              percent REAL)""")

def cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Загрузка CPU: {cpu_percent}%")
    cursor.execute("INSERT INTO cpu (time, cpu_percent) VALUES (?, ?)",(datetime.now(), str(cpu_percent)))
    con.commit()

def memory():
    mem = psutil.virtual_memory()
    print(f"Использовано: {mem.used / (1024**3):.2f} GB ({mem.percent}%)")
    cursor.execute("INSERT INTO memory (time, used, percent) VALUES (?, ?, ?)",(datetime.now(), mem.used, str(mem.percent)))
    con.commit()

def disk():
    disks = psutil.disk_partitions(all=False)
    for disk in disks:
        x = psutil.disk_usage(disk.mountpoint)
        print(f"{disk.device} - загруженность: {x.percent}%")
        cursor.execute("INSERT INTO disk (time, name, percent) VALUES (?, ?, ?)",(datetime.now(), disk.device, str(x.percent)))
        con.commit()

def history():
    a = input('1 - История CPU\n'
              '2 - История оперативной памяти\n'
              '3 - История дисков\n')
    if a == '1':
        cursor.execute("SELECT * FROM cpu")
        for i in cursor.fetchall():
            print(f"{i[0]} - {i[1]} загрузка CPU: {i[2]}")
    elif a == '2':
        cursor.execute("SELECT * FROM memory")
        for i in cursor.fetchall():
            print(f"{i[0]} - {i[1]} использовано: {i[2] / (1024**3):.2f} GB ({i[3]}%)")
    elif a == '3':
        cursor.execute("SELECT * FROM disk")
        for i in cursor.fetchall():
            print(f"{i[0]} - {i[1]} {i[2]} - загруженность: ({i[3]}%)")


while True:
    a = input('\n'
              '1 - Мониторинг загрузки CPU\n'
              '2 - Мониторинг оперативной памяти\n'
              '3 - Загруженность дисков\n'
              '4 - Просмотр истории мониторинга\n')
    if a == '1':
        cpu()
    elif a == '2':
        memory()
    elif a == '3':
        disk()
    elif a == '4':
        history()
    else:
        break


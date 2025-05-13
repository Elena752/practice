import sqlite3
con = sqlite3.connect("students.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name VARCHAR(30),
                surname VARCHAR(30),
                secondname VARCHAR(30),
                groupN INTEGER,
                mark1 INTEGER,
                mark2 INTEGER,
                mark3 INTEGER,
                mark4 INTEGER)""")

class Student:
    name = ''
    surname = ''
    secondname = ''
    group = 222
    marks = [1, 2, 3, 4]

    @classmethod
    def from_db(cls, student_data):
        s = cls()
        s.id = student_data[0]
        s.surname = student_data[1]
        s.name = student_data[2]
        s.secondname = student_data[3]
        s.group = student_data[4]
        s.marks = list(student_data[5:9])
        return s

    def display_info(self):
        print(f"\nID: {self.id}")
        print(f"ФИО: {self.surname} {self.name} {self.secondname}")
        print(f"Группа: {self.group}")
        print(f"Оценки: {', '.join(map(str, self.marks))}")

def add_new_student():
    print('Введите: фамилию, имя, отчество, номер группы и 4 оценки 1-5 (всё через пробел)')
    s = Student()
    try:
        data = input().split()
        if len(data) == 0:
            return
        if len(data) != 8:
            print("Ошибка: фамилию, имя, отчество, номер группы, оценки через пробел. Попробуйте снова.")
            return
        s = Student()
        s.surname = data[0]
        s.name = data[1]
        s.secondname = data[2]
        s.group = int(data[3])
        s.marks = []
        for mark_str in data[4:8]:
            mark = int(mark_str)
            if mark < 1 or mark > 5:
                print("Ошибка: оценки должны быть от 1 до 5")
                return
            s.marks.append(mark)
        cursor.execute("INSERT INTO students (name, surname, secondname, groupN, mark1, mark2, mark3, mark4) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (s.name, s.surname, s.secondname, s.group, s.marks[0], s.marks[1], s.marks[2], s.marks[3]))
        con.commit()
    except ValueError:
        print("Ошибка: группа и оценки должны быть целыми числами")

def view_all_students():
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()

    for student_data in all_students:
        student = Student.from_db(student_data)
        student.display_info()

def view_student_with_average():
    id = int(input("Введите id студента: "))
    cursor.execute("SELECT *, (mark1 + mark2 + mark3 + mark4) / 4.0 AS average FROM students WHERE id = ?", [id])
    data = cursor.fetchone()
    s = Student.from_db(data)
    s.display_info()
    print("Средний балл:", data[9])

def edit_student():
    id = int(input("Введите id студента: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", [id])
    data = cursor.fetchone()
    s = Student.from_db(data)
    print("Вы выбрали студента: ")
    s.display_info()
    a = input("Что хотите изменить? 1 - фамилию, 2 - имя, 3 - отчество, 4 - группу, 5 - оценку1, 6 - оценку2, 7 - оценку3, 8 - оценку4")
    if a == '1':
        new = input("Введите новую фамилию: ")
        cursor.execute("UPDATE students SET surname =? WHERE id=?", (new, id))
    elif a == '2':
        new = input("Введите новое имя: ")
        cursor.execute("UPDATE students SET name =? WHERE id=?", (new, id))
    elif a == '3':
        new = input("Введите новое отчество: ")
        cursor.execute("UPDATE students SET secondname =? WHERE id=?", (new, id))
    elif a == '4':
        try:
            new = int(input("Введите новый номер группы: "))
            cursor.execute("UPDATE students SET groupN =? WHERE id=?", (new, id))
        except ValueError:
            print("Введите целое число!")
    elif a == '5':
        try:
            new = int(input("Введите новую оценку1: "))
            cursor.execute("UPDATE students SET mark1 =? WHERE id=?", (new, id))
        except ValueError:
            print("Введите целое число от 1 до 5")
    elif a == '6':
        try:
            new = int(input("Введите новую оценку2: "))
            cursor.execute("UPDATE students SET mark2 =? WHERE id=?", (new, id))
        except ValueError:
            print("Введите целое число от 1 до 5")
    elif a == '7':
        try:
            new = int(input("Введите новую оценку3: "))
            cursor.execute("UPDATE students SET mark3 =? WHERE id=?", (new, id))
        except ValueError:
            print("Введите целое число от 1 до 5")
    elif a == '8':
        try:
            new = int(input("Введите новую оценку4: "))
            cursor.execute("UPDATE students SET mark4 =? WHERE id=?", (new, id))
        except ValueError:
            print("Введите целое число от 1 до 5")
    con.commit()

def delete_student():
    id = int(input("Введите id студента: "))
    cursor.execute("DELETE FROM students WHERE id =?", [id])
    con.commit()

def view_group_average():
    g = int(input("Введите номер группы: "))
    cursor.execute("SELECT AVG((mark1 + mark2 + mark3 + mark4) / 4.0) AS averagestudents FROM students WHERE groupN = 778 GROUP BY ?", [g])
    data = cursor.fetchone()
    print("Cредний балл группы:", data[0])

while True:
    a = input('\n'
          '1 - Добавление нового студента\n'
          '2 - Просмотр всех студентов\n'
          '3 - Просмотр одного студента с средним баллом\n'
          '4 - Редактирование студента\n'
          '5 - Удаление студента\n'
          '6 - Просмотр среднего балла студентов группы\n')
    if a == '1':
        add_new_student()
    elif a == '2':
        view_all_students()
    elif a == '3':
        view_student_with_average()
    elif a == '4':
        edit_student()
    elif a == '5':
        delete_student()
    elif a == '6':
        view_group_average()
    else:
        break
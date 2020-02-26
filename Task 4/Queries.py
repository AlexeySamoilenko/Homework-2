import pymysql as mysql


def create_db(host, user, passwd, name_db):
    db = mysql.connect(host, user, passwd)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE {}".format(name_db))


def drop_tables():
    queries = ('''DROP TABLE IF EXISTS students''',
               '''DROP TABLE IF EXISTS rooms''')
    return queries


def create_tables():
    queries = ('''CREATE TABLE rooms(
                    id INT PRIMARY KEY,
                    name VARCHAR(20) NOT NULL
                    ) ENGINE=INNODB;''',
               '''CREATE TABLE students(
                   id INT PRIMARY KEY,
                   name varchar(100) not null,
                   sex varchar(1) not null,
                   birthday DATETIME not null,
                   room INT null, 
                   CONSTRAINT fk_room
                   FOREIGN KEY (room) 
                       REFERENCES rooms(id)
               ) ENGINE=INNODB;''')
    return queries


def show_tables():
    queries = ('select * from rooms;',
               'select * from students;')
    return queries


def stud_in_room():
    queries = '''SELECT rooms.name AS 'Room', COUNT(*) AS 'Students Count'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name'''
    return queries


def top_avg_age():
    queries = """
            SELECT Rooms.name AS ROOM, AVG((TO_DAYS(NOW())-TO_DAYS(birthday))/365) AS AVG_AGE
            FROM Students INNER JOIN Rooms ON Rooms.id = Students.room
            GROUP BY Rooms.name
            ORDER BY AVG_AGE
            LIMIT 5
            """
    return queries


def biggest_dif():
    queries = ''''SELECT rooms.name AS 'Room', (MAX(YEAR(NOW()) - year(students.birthday)) - MIN(YEAR(NOW()) - year(students.birthday))) AS 'Min Age'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name
                ORDER BY 2 DESC
                LIMIT 5'''

    return queries


def only_two_genders():
    queries = '''SELECT rooms.name AS 'Room'
                FROM rooms
                WHERE (SELECT COUNT(DISTINCT sex) FROM students WHERE rooms.id = students.room) > 1'''
    return queries


def list_of_queries() -> list:
    queries = [#stud_in_room(),
               #top_avg_age(),
               biggest_dif()
               #only_two_genders()
    ]
    return queries


def insert_data() -> dict:
    queries = {
        'rooms': 'INSERT INTO Rooms (id, name) VALUES (%s,%s)',
        'students': 'INSERT INTO Students (id, name, room, birthday, sex) VALUES (%s,%s,%s,%s,%s)'
    }
    return queries

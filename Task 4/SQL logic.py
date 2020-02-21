def drop_tables():
    queries = ('''DROP TABLE IF EXISTS students;''',
               '''DROP TABLE IF EXISTS rooms;''')
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
    queries = ('select * from rooms;'
               'select * from students;')
    return queries


def stud_in_room():
    queries = '''SELECT rooms.name AS 'Room', COUNT(*) AS 'Students Count'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name;'''
    return queries


def top_avg_age():
    queries = '''SET @currentYear = YEAR(NOW());

                SELECT rooms.name AS 'Room', AVG(@currentYear - year(students.birthday)) AS 'Average Age'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name
                ORDER BY 2
                LIMIT 5;'''
    return queries


def biggest_dif():
    queries = '''SET @currentYear = YEAR(NOW());
    
                SELECT rooms.name AS 'Room', (MAX(@currentYear - year(students.birthday)) - MIN(@currentYear - year(students.birthday))) AS 'Min Age'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name
                ORDER BY 2 DESC
                LIMIT 5;'''
    return queries


def only_two_genders():
    queries = '''SELECT rooms.name AS 'Room'
                FROM rooms
                WHERE (SELECT COUNT(DISTINCT sex) FROM students WHERE rooms.id = students.room) > 1;'''
    return queries


def list_of_queries():
    list_of_queries = [stud_in_room(),
                top_avg_age(),
                biggest_dif(),
                only_two_genders()]
    return list_of_queries


def inserting_data():
    queries = {
        'rooms': 'INSERT INTO Rooms (id, name) VALUES (%s%s)',
        'students': 'INSERT INTO Students (id, name, room, birthday, sex) VALUES (%s%s%s%s%s)'
    }
    return queries


def insert_data():
    # Inserting Multiple Rows
    cursor.executemany(inserting_data, data)
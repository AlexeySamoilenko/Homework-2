
def drop_tables():
    queries = '''DROP TABLE IF EXISTS students;
                DROP TABLE IF EXISTS rooms;'''

def create_tables():
    queries = '''CREATE TABLE rooms(
                    id INT PRIMARY KEY,
                    name VARCHAR(20) NOT NULL
                    ) ENGINE=INNODB;
                CREATE TABLE students(
                    id INT PRIMARY KEY,
                    name varchar(100) not null,
                    sex varchar(1) not null,
                    birthday DATETIME not null,
                    room INT null, 
                    CONSTRAINT fk_room
                    FOREIGN KEY (room) 
                        REFERENCES rooms(id)
                ) ENGINE=INNODB;'''

def filling_from_csv():
    queries =""
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/stu.CSV'
INTO TABLE students
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(birthday, id, name, room, sex);

SHOW VARIABLES LIKE 'secure_file_priv';


def show_tables():
    queries = '''
    select * from rooms;
    select * from students;'''

def stud_in_room():
    queries = '''SELECT rooms.name AS 'Room', COUNT(*) AS 'Students Count'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name;'''

def top_avg_age():
    queries = '''SET @currentYear = YEAR(NOW());

                SELECT rooms.name AS 'Room', AVG(@currentYear - year(students.birthday)) AS 'Average Age'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name
                ORDER BY 2
                LIMIT 5;'''

def biggest_dif():
    queries = '''SET @currentYear = YEAR(NOW());
    
                SELECT rooms.name AS 'Room', (MAX(@currentYear - year(students.birthday)) - MIN(@currentYear - year(students.birthday))) AS 'Min Age'
                FROM rooms JOIN students ON rooms.id = students.room
                GROUP BY rooms.name
                ORDER BY 2 DESC
                LIMIT 5;'''

def only_two_genders():
    queries = '''SELECT rooms.name AS 'Room'
                FROM rooms
                WHERE (SELECT COUNT(DISTINCT sex) FROM students WHERE rooms.id = students.room) > 1;'''

def list_of_request():
    requests = [stud_in_room(),
                top_avg_age(),
                biggest_dif(),
                only_two_genders()]
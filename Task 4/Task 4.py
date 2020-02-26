import pymysql as mysql
import Queries
from Parser import insert_in_db
from FileSaver import save_file


class Connector(object):
    def __init__(self, host, user, password, db):
        self._conn = mysql.connect(host, user, password, db)
        self._cursor = self._conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.connection.close()

    def __enter__(self):
        return self

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def executemany(self, sql, params=None):
        self.cursor.executemany(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def lst_str(self, fn):
        if type(fn) in [list, tuple, set]:
            for i in fn:
                self.execute(i)
        elif type(fn) == str:
            self.execute(fn)


def main(host, user, passwd, name_db,
         read_file_path1,read_file_path2, save_path_file):
    #Queries.create_db(host, user, passwd, name_db)
    with Connector(host, user, passwd, name_db) as db:
        db.lst_str(Queries.drop_tables())
        db.lst_str(Queries.create_tables())
        insert_in_db(db, read_file_path1, read_file_path2)
        db.commit()

        list_of_queries = Queries.list_of_queries()
        print(list_of_queries)
        for i in list_of_queries:
            print(db.query(i))
            save_file(db.query(i), save_path_file)


if __name__ == "__main__":
    main('localhost', 'root', 'admin', 'tests', 'rooms.json', 'students.json', 'result.json')



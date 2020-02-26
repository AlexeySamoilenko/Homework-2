import json
from Queries import insert_data


class FileHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def read(file_path: str) -> tuple:
        with open(file_path, 'r', encoding='utf-8') as f:
            return tuple(json.load(f))


def insert_in_db(db, read_file_path1, read_file_path2):
    rooms = FileHandler().read(read_file_path1)
    students = FileHandler().read(read_file_path2)
    queries = insert_data()
    for i in rooms:
        db.execute(queries['rooms'], (i["id"], i["name"]))
    for i in students:
        db.execute(queries['students'], (i["id"], i["name"], i["room"], i["birthday"], i["sex"]))


import json
from xml.dom import minidom
from abc import ABC, abstractmethod





def main(file_path: str, file_path2: str, save_path_file: str):
    if '.json' in save_path_file:
        JsonSaver(result_data, save_path_file).save_data()
    elif '.xml' in save_path_file:
        XmlSaver(result_data, save_path_file).save_data()
    else:
        return False







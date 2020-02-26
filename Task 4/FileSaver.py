import json
from xml.dom import minidom
from abc import ABC, abstractmethod


class FileSaver(ABC):
    def __init__(self, result_data: dict, save_path_file: str):
        self.result_data = result_data
        self.save_path_file = save_path_file

    @abstractmethod
    def pre(self):
        pass

    def save_data(self):
        # preparing for writing in file, turning dict into str
        self.pre()
        with open(self.save_path_file, 'a') as f:
            f.write(self.result_data)


class XmlSaver(FileSaver):
    def __init__(self, result_data: dict, save_path_file: str):
        super(XmlSaver, self).__init__(result_data, save_path_file)

    def pre(self):
        # Preparing to Save file in XML format, turning dict into str
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        for key, value in self.result_data.items():
            roomChild = root.createElement('room')
            roomChild.appendChild(root.createTextNode(key + ':' + str(value)))
            xml.appendChild(roomChild)
        self.result_data = root.toprettyxml(indent='\t')


class JsonSaver(FileSaver):
    def __init__(self, result_data: dict, save_path_file: str):
        super(JsonSaver, self).__init__(result_data, save_path_file)

    def pre(self):
        # Preparing for writing in file, turning dict into str
        self.result_data = json.dumps(self.result_data, indent=4)


def save_file(result_data, save_path_file):
    if '.json' in save_path_file:
        JsonSaver(result_data, save_path_file).save_data()
    elif '.xml' in save_path_file:
        XmlSaver(result_data, save_path_file).save_data()
    else:
        return False







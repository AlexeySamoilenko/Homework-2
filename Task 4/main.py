from FilesHandler import JsonSaver, XmlSaver, FileHandler

def main(file_path: str, file_path2: str, save_path_file: str):
    result_data = FileHandler.data_processing(file_path, file_path2)

    if '.json' in save_path_file:
        JsonSaver(result_data, save_path_file).write_json()
    elif '.xml' in save_path_file:
        XmlSaver(result_data, save_path_file).write_xml()
    else:
        return False

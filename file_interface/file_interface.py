from collections import namedtuple
import os
import typing
import csv

class FileInterface(object):
    """Reads and writes to files using lists of namedtuples"""

    def __init__(self):
        return None


    @staticmethod
    def overwrite_list_of_dicts_to_file(data:typing.List[dict],filename:str) -> None:
        if not FileInterface.does_filename_exist(filename=filename):
            FileInterface.create_file(filename=filename)
        
        FileInterface.truncate_file(filename=filename)
        FileInterface.write_list_of_dicts_to_file(filename=filename)
        return None

    @staticmethod
    def write_list_of_dicts_to_file(data:typing.List[dict],filename:str)->None:
        return None

    @staticmethod
    def does_filename_exist(filename:str) -> bool:
        return os.path.exists(filename)


    @staticmethod
    def is_file_empty(filename:str) -> bool:
        return os.stat(filename).st_size == 0


    @staticmethod
    def truncate_file(filename:str) -> None:
        with open(file=filename, mode='r', newline=None) as csv_file:
            csv_file.truncate()
        return None


    @staticmethod
    def create_file(filename:str) -> None:
        with open(filename, 'w') as fp:
            pass
        return None

    
    @staticmethod
    def convert_file_to_list_of_dicts(filename:str) -> typing.List[typing.NamedTuple]:
        if not FileInterface.does_filename_exist(filename=filename) or FileInterface.is_file_empty(filename=filename):
            return None

        with open(file=filename, mode='r', newline=None) as csv_file:
            reader:csv.DictReader = csv.DictReader(csv_file)

        return [row for row in reader]










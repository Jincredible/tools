from collections import namedtuple
import os
import typing
import csv

class FileInterface(object):
    """Reads and writes to files using lists of namedtuples"""

    def __init__(self, arg):
        return None


    @staticmethod
    def overwrite_to_file(data:typing.List[typing.NamedTuple],filename:str) -> None:
        return None


    @staticmethod
    def does_filename_exist(filename:str) -> bool:
        return os.path.exists(filename)


    @staticmethod
    def delete_file(filename:str) -> None:
        return None


    @staticmethod
    def create_file(filename:str) -> None:
        return None

    
    @staticmethod
    def convert_file_to_list_of_tuples(filename:str) -> typing.List[typing.NamedTuple]:

        with open(file=filename, mode='r', newline=None) as csv_file:
            reader = csv.DictReader(csv_file)
        return None










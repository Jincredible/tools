import sys

import os
import typing

import pathlib
path_list = str(pathlib.Path(__file__)).split("/")[1:-1][::-1] # take out the first and last element and reverse list

path_to_code_inspector: str = str(pathlib.Path(__file__).parents[path_list.index('code_inspector')])


sys.path.append(path_to_code_inspector)
from code_inspector import CodeInspector
import unittest

class TestCodeInspector(unittest.TestCase):

    def test__test_class_0(self):

        actual_method_names, actual_parameter_names = CodeInspector.get_methods_and_parameters(TestCodeInspector.TestClass_0)
        expected_method_names = []
        expected_parameter_names = []
        self.assertEqual(actual_method_names, expected_method_names)

    def test__test_class_1(self):

        actual_method_names, actual_parameter_names = CodeInspector.get_methods_and_parameters(TestCodeInspector.TestClass_1)
        expected_method_names = ['method_1']
        expected_parameter_names = [['self']]
        self.assertEqual(actual_method_names, expected_method_names)

    def test__test_class_2(self):

        actual_method_names, actual_parameter_names = CodeInspector.get_methods_and_parameters(TestCodeInspector.TestClass_2)
        expected_method_names = ['method_1', 'method_2']
        expected_parameter_names = [[], ['self', 'var1']]
        self.assertEqual(actual_method_names, expected_method_names)


    class TestClass_0(object):
        def __init__(self):
            return None
        def __name__(self):
            return None

    class TestClass_1(object):
        def __init__(self):
            return None
        def method_1(self):
            return None

    class TestClass_2(object):
        def __init__(self):
            return None
        @staticmethod
        def method_1():
            return None
        def method_2(self, var1:str):
            return None


def find_parent_directory(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root)

path_to_tools: str = str(pathlib.Path(__file__).parents[path_list.index('tools')])
path_to_file_interface:str = find_parent_directory(name='file_interface.py', path=path_to_tools)
sys.path.append(path_to_file_interface)

from file_interface import FileInterface
import inspect


def test_with_file_interface():

    CodeInspector.print_class_info(FileInterface)

    return None

if __name__ == '__main__':
    try:
        unittest.main(verbosity=2, exit=False)
        # test_with_file_interface()
        
    finally:
        sys.path.remove(path_to_code_inspector)
        sys.path.remove(path_to_file_interface)





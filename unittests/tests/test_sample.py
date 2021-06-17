import sys
import os
import typing
import pathlib
import io
path_list = str(pathlib.Path(__file__)).split("/")[1:-1][::-1] # take out the first and last element and reverse list

path_to_code: str = str(pathlib.Path(__file__).parents[path_list.index('unittests')])
sys.path.append(path_to_code)

import sample
import unittest
from unittest.mock import patch
from unittest.mock import call

class TestReturnListLength(unittest.TestCase):


    def setUp(self):
        """This module is executed first before anything else, to prepare for our unit tests"""
        return None


    def test__function_return_list_length__empty_list(self):
        input_list: list = []
        expected_output: int = 0
        actual_output = sample.function_return_list_length(input_list=input_list)

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_return_list_length__non_empty_list(self):
        input_list: list = [1, 'hi', True]
        expected_output: int = 3
        actual_output = sample.function_return_list_length(input_list=input_list)

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_return_list_length__list_with_none(self):
        input_list: list = [None]
        expected_output: int = 1
        actual_output = sample.function_return_list_length(input_list=input_list)

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_return_list_length__nested_lists(self):
        input_list: list = [[1, 2, 3], {}, {1:'hi', 'name': 'Dan', 3: True}, 'this is a string']
        expected_output: int = 4
        actual_output = sample.function_return_list_length(input_list=input_list)

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def tearDown(self):
        """This module is executed last to clean up after unit tests"""
        return None


@patch('builtins.input')
class TestConsoleInput(unittest.TestCase):


    def test__function_with_one_console_input__simple_input(self, mock_input):

        mock_input.side_effect=['sample_input']
        expected_output: int = 12
        actual_output = sample.function_with_one_console_input()

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_with_one_console_input__empty_input(self, mock_input):

        mock_input.side_effect=['']
        expected_output: int = 0
        actual_output = sample.function_with_one_console_input()

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None



@patch('builtins.input')
class TestMultipleConsoleInput(unittest.TestCase):


    def test__function_with_multiple_console_inputs__simple_input(self, mock_input):

        mock_input.side_effect=['name', 4, 0.5]
        expected_output: float = 4.0
        actual_output = sample.function_with_multiple_console_inputs()

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_with_multiple_console_inputs__empty_string(self, mock_input):

        mock_input.side_effect=['', 4, 0.5]
        expected_output: float = 2.00
        actual_output = sample.function_with_multiple_console_inputs()

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_with_multiple_console_inputs__string_of_numbers(self, mock_input):

        mock_input.side_effect=['2345', 4, 1]
        expected_output: float = 8.00
        actual_output = sample.function_with_multiple_console_inputs()

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None


    def test__function_with_multiple_console_inputs__multiply_by_zero(self, mock_input):

        mock_input.side_effect=['2345', 4, 0]
        expected_output: float = 0.00
        actual_output = sample.function_with_multiple_console_inputs()

        self.assertIsInstance(obj=actual_output, cls=type(expected_output), msg=None)
        self.assertEqual(first=actual_output, second=expected_output, msg=None)

        return None



@patch('builtins.print')
class TestPrintToConsole(unittest.TestCase):



    def test__function_with_print__empty_input(self, mock_print):
        input_str: str = ''
        expected_output: str = 'hi '
        sample.function_with_print(input_str=input_str)

        mock_print.assert_called_with(expected_output)


    def test__function_with_print__normal_input(self, mock_print):
        input_str: str = '243 abc'
        expected_output: str = 'hi 243 abc'
        sample.function_with_print(input_str=input_str)

        mock_print.assert_called_with(expected_output)


    def test__function_with_print__none_input(self, mock_print):
        input_str: str = None
        expected_output: str = 'hi '
        sample.function_with_print(input_str=input_str)

        mock_print.assert_called_with(expected_output)



@patch('builtins.print')
class TestPrintToConsoleMultipleTimes(unittest.TestCase):

    def setUp(self):
        """This module is executed first before anything else, to prepare for our unit tests"""
        return None


    def test__function_with_multiple_prints__empty_input(self, mock_print):
        input_str: str = ''
        expected_calls: list = [call('hi '), call('nice to meet you '), call('you have 0 letters in your name')]
        sample.function_with_multiple_prints(input_str=input_str)
        mock_print.assert_has_calls(expected_calls)


    def test__function_with_multiple_prints__normal_input(self, mock_print):
        input_str: str = 'Steven'
        expected_calls: list = [call('hi Steven'), call('nice to meet you Steven'), call('you have 6 letters in your name')]
        sample.function_with_multiple_prints(input_str=input_str)
        mock_print.assert_has_calls(expected_calls)


    def test__function_with_multiple_prints__none_input(self, mock_print):
        input_str: str = None
        expected_calls: list = [call('hi '), call('nice to meet you '), call('you have 0 letters in your name')]
        sample.function_with_multiple_prints(input_str=input_str)
        mock_print.assert_has_calls(expected_calls)

    def tearDown(self):
        """This module is executed last to clean up after unit tests"""
        return None



@patch('builtins.print') # the order of this is really important!
@patch('builtins.input')
class TestPrintReadAndWriteToConsole(unittest.TestCase):



    def test__function_read_and_write_to_console_once__normal_input(self, mock_input, mock_print):
        
        mock_input.side_effect=['Steven']
        expected_output: str = 'hi Steven'
        sample.function_read_and_write_to_console_once()

        mock_print.assert_called_with(expected_output)


    def test__function_read_and_write_to_console_once__empty_input(self, mock_input, mock_print):
        
        mock_input.side_effect=['']
        expected_output: str = 'hi '
        sample.function_read_and_write_to_console_once()

        mock_print.assert_called_with(expected_output)



@patch('builtins.open')
class TestReadFromFile(unittest.TestCase):


    def test__function_that_reads_from_a_file__normal_file_contents(self, mock_open):
        
        file_data:io.StringIO = io.StringIO('first line\nsecond line\n\n123\nlast line')
        mock_open.return_value = file_data
        filename: str = 'path/to/open/file.txt'


        expected_output:list = ['first line', 'second line', '', '123', 'last line']
        actual_output: list = sample.function_that_reads_from_a_file(filename=filename)


        self.assertEqual(first=actual_output, second=expected_output)
        mock_open.assert_called_with(filename, mode='r')


    def test__function_that_reads_from_a_file_once__empty_input(self, mock_open):
        
        file_data:io.StringIO = io.StringIO('')
        mock_open.return_value = file_data
        filename: str = 'path/to/open/file.txt'


        expected_output:list = []
        actual_output: list = sample.function_that_reads_from_a_file(filename=filename)


        self.assertEqual(first=actual_output, second=expected_output)
        mock_open.assert_called_with(filename, mode='r')


    def test__function_that_reads_from_a_file_once__no_input(self, mock_open):
        
        file_data:io.StringIO = io.StringIO(None)
        mock_open.return_value = file_data
        filename: str = 'path/to/open/file.txt'


        expected_output:list = []
        actual_output: list = sample.function_that_reads_from_a_file(filename=filename)


        self.assertEqual(first=actual_output, second=expected_output)
        mock_open.assert_called_with(filename, mode='r')



@patch('builtins.open')
class TestWriteToFile(unittest.TestCase):


    def test__function_that_writes_to_a_file__normal_data(self, mock_open):
        
        file_data:list = ['!!123', 'test row 1', '', None, 'last row']
        filename: str = 'path/to/open/file.txt'

        expected_calls:list = [call('!!123\n'), call('test row 1\n'), call('\n'), call('\n'), call('last row\n')]

        sample.function_that_writes_to_a_file(filename=filename, data=file_data)

        mock_open.assert_called_with(filename, mode='w')
        mock_open().__enter__().write.assert_has_calls(expected_calls)



    def test__function_that_writes_to_a_file__empty_input(self, mock_open):
        
        file_data:list = [None]
        filename: str = 'path/to/open/file.txt'

        expected_calls:list = [call('\n')]

        sample.function_that_writes_to_a_file(filename=filename, data=file_data)

        mock_open.assert_called_with(filename, mode='w')
        mock_open().__enter__().write.assert_has_calls(expected_calls)


class TestRaiseException(unittest.TestCase):

    def test__function_that_raises_an_exception__none_input(self):
        input_str: None = None
        self.assertRaises(TypeError, sample.function_that_raises_an_exception, input_str)


    def test__function_that_raises_an_exception__num_input(self):
        input_str: int = 0
        self.assertRaises(TypeError, sample.function_that_raises_an_exception, input_str)




if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)


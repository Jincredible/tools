
import sys
import re

class InputManager(object):
    """Checks user inputs into console"""

    exit_command: str = 'exit'

    @classmethod
    def _get_input_raw(cls, prompt:str):

        raw_input_value: str = input(prompt)

        if raw_input_value == InputManager.exit_command:
            sys.exit('Exit command detected. Exiting program')

        return raw_input_value

    @classmethod
    def get_input(cls, prompt:str, expected_type:type):

        raw_input_value: str = cls._get_input_raw(prompt=prompt)

        convert_function = cls._convert_input_function(expected_type=expected_type)

        try:
            return convert_function(raw_input_value=raw_input_value)
        except ValueError:
            print(f"Error, please enter a value of the type {expected_type}... ")
            return cls.get_input(prompt=prompt, expected_type=expected_type)

    @classmethod
    def _convert_input_function(cls, expected_type:type):
        if expected_type == int:
            return cls._convert_input_int
        elif expected_type == str:
            return cls._convert_input_str
        elif expected_type == float:
            return cls._convert_input_float
        elif expected_type == bool:
            return cls._convert_input_bool
        elif expected_type == tuple:
            return cls._convert_input_tuple
        elif expected_type == list:
            return cls._convert_input_list
        else:
            raise ValueError(expected_type)
        return

    @classmethod
    def _convert_input_int(cls, raw_input_value:str):
        return int(raw_input_value)

    @classmethod
    def _convert_input_str(cls, raw_input_value:str):
        return raw_input_value

    @classmethod
    def _convert_input_float(cls, raw_input_value:str):
        return float(raw_input_value)

    @classmethod
    def _convert_input_bool(cls, raw_input_value:str):
        return bool(raw_input_value)

    @classmethod
    def _apply_regex(cls,raw_input_value:str) -> list:
        # honestly, I'm not entirely sure why this works.
        return re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_input_value)

    @classmethod
    def _convert_input_tuple(cls, raw_input_value:str):
        list_of_numbers = cls._apply_regex(raw_input_value=raw_input_value)
        return tuple(float(x.replace(',', '')) for x in list_of_numbers)

    @classmethod
    def _convert_input_list(cls, raw_input_value:str):
        list_of_numbers = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_input_value)
        return list(float(x.replace(',', '')) for x in list_of_numbers)



def main_temp() -> None:

    print(f"type of None: {type(None)}")
    print(f"type of tuple: {type((1,2))}")

    my_var = tuple

    print("\n")
    print(f"type of tuple: {my_var}")
    print(f"my_var is a tuple type object?: {my_var==type((1,2))}")
    print(f"type of type: {type(type(3))}")

    print("\n")
    print(f"type of function: {type(main_temp)}")

    my_var_function = type(main_temp) # not sure of a better way to define this
    print(f"my_var_function: {my_var_function}")
    print(f"is function a function type?: {type(main_temp) == my_var_function}")


    raw_input_value = '   (minimum = -3.6, maximum = 5,000)  '



    return None

if __name__ == '__main__':
    
    temp_tuple: tuple = InputManager.get_input('enter your temperature min and max: ', tuple)
    print(f"temp_tuple: {temp_tuple}")





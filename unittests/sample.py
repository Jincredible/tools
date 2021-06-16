


def function_return_list_length(input_list:list) -> int:
    """purpose: example of a function with no console or side effects
    input: list object
    output: int
    side effects: none"""
    return len(input_list)


def function_with_one_console_input()->int:
    """purpose: example of a function that asks one thing from console
    input: console only, no parameters
    output: int
    side effects: none"""
    return len(input('input anything on console: '))


def function_with_multiple_console_inputs()->float:
    """purpose: example of a function that asks multiple things from console
    input: console only, no parameters
    output: float
    side effects: none"""
    input_str_1: str = input('input #1... enter a string: ')
    input_int_2: int = int(input('input #2... enter an int: '))
    input_float_3: float = float(input('input #3... enter a float: '))
    return (len(input_str_1) + input_int_2) * input_float_3



def function_with_print(input_str:str) -> None:
    """purpose: example of a function that prints to console once
    input: one string
    output: None
    side effects: a print to console one time
    important note: when the input is None, we want to use the logical gate {input_str or ''} to print
        an empty string"""
    print(f"hi {input_str or ''}")
    return None


def function_with_multiple_prints(input_str: str) -> None:
    """purpose: example of a function that prints to console multiple times
    input: one string
    output: None
    side effects: a print to console multiple times
    important note: when the input is None, we want to use the logical gate {input_str or ''} to print
        an empty string"""

    print(f"hi {input_str or ''}")
    print(f"nice to meet you {input_str or ''}")

    try:
        num_letters: int = len(input_str)
    except TypeError:
        num_letters: int = 0
    
    print(f"you have {num_letters} letters in your name")
    return None



def function_read_and_write_to_console_once() -> None:
    """purpose: example of a function that takes one input from console and prints to console once
    input: once from console
    output: None
    side effects: a print to console one time
    important note: when the input is None, we want to use the logical gate {input_str or ''} to print
        an empty string"""
    print(f"hi {input('Enter your name: ') or ''}")
    return None



if __name__ == '__main__':
    pass

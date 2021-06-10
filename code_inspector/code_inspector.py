import inspect
import typing

class CodeInspector(object):
    """Prints methods and parameters of classes"""

    def __init__(self):
        return None

    @staticmethod
    def get_methods_and_parameters(input_class: type) -> typing.List[typing.Dict[str,typing.List[str]]]:
        method_names: typing.List[str] = [method_name for method_name in dir(input_class) if method_name[:2] != '__']
        parameter_names: typing.List[typing.List[str]] = [list(inspect.signature(getattr(input_class,method_name)).parameters) for method_name in method_names]

        return method_names, parameter_names

    @staticmethod
    def get_methods_and_signatures(input_class: type) -> typing.Tuple[typing.List[str],typing.List[str]]:
        method_names: typing.List[str] = [method_name for method_name in dir(input_class) if method_name[:2] != '__']
        signatures: typing.List[str] = [str(inspect.signature(getattr(input_class,method_name))) for method_name in method_names]

        return method_names, signatures

    @staticmethod
    def print_class_info(input_class:type) -> None:
        print(f"\nmethods and parameters for {input_class.__name__}")
        method_names, signatures = CodeInspector.get_methods_and_signatures(input_class=input_class)

        [CodeInspector.print_method_info(method_name=method_name, signature=signature) for method_name, signature in zip(method_names, signatures)]
        return None


    @staticmethod
    def print_method_info(method_name:str, signature: str) -> None:
        print(f"\nmethod name: {method_name}")
        print(f"\t{signature}")
        return None


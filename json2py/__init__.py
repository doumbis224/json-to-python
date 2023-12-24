# coding:utf-8

from io import TextIOWrapper

import json


class Parser:
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self.data = self.load()

    def load(self) -> dict[str, any]:
        data = None
        with open(self.json_file, 'r') as f:
            data = json.load(f)

        return data

    @classmethod
    def from_json(cls, filename) -> 'Parser':
        return cls(filename)

    def to_python_file(self, filename: str) -> bool:
        if self.data == None:
            return False

        with open(filename, 'w') as o:
            self.__write_header(o)
            for class_name, properties in self.data.items():
                parent = properties['parent']
                methods = properties['methods']
                modules = properties['modules']
                self.__import_modules(o, modules)
                self.__write_class_name(o, class_name, parent)
                for method_name, return_type in methods.items():
                    self.__write_class_method(o, method_name, return_type)

        return True

    @staticmethod
    def __write_header(file_descriptor: 'TextIOWrapper') -> None:
        file_descriptor.write("# coding:utf-8\n\n")

    @staticmethod
    def __write_class_name(file_descriptor: 'TextIOWrapper', class_name: str, parent: str = None) -> None:
        parent_name = "" if parent is None else f"({parent})"
        file_descriptor.write(f'\nclass {class_name}{parent_name}:\n')
        file_descriptor.write('\tdef __init__(self) -> None:\n')
        file_descriptor.write('\t\tpass\n')

    @staticmethod
    def __write_class_method(file_descriptor: 'TextIOWrapper', method_name: str, return_type: str = 'None') -> None:
        file_descriptor.write(
            f'\n\tdef {method_name}(self) -> {return_type}:\n')
        file_descriptor.write('\t\tpass\n')

    @staticmethod
    def __import_modules(file_descriptor: 'TextIOWrapper', modules: list) -> None:
        for module in modules:
            file_descriptor.write(f"import {module}\n")

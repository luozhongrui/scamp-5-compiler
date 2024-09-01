import os
import sys

current_script_path = os.path.abspath(__file__)


parent_directory = os.path.dirname(os.path.dirname(current_script_path))


lib_path = os.path.join(parent_directory, 'lib')


sys.path.append(lib_path)

from ast_tool import AssemblyGenerator
import argparse


def read_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error while reading file: {e}")


def write_file_contents(filename, content):

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error while writing file: {e}")


def main():

    parser = argparse.ArgumentParser(description="Command line tool for processing files.")

    parser.add_argument('-path', required=True, help="Path to the input Python file")

    parser.add_argument('-o', required=True, help="Output file path for the converted C++ file")
    args = parser.parse_args()

    input_path = args.path
    output_path = args.o

    source_code = read_file_contents(input_path)
    generator = AssemblyGenerator()
    asm_code = generator.generate_assembly(source_code)
    write_file_contents(output_path, asm_code)


if __name__ == "__main__":
    main()




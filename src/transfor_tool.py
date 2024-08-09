import os
import sys

# 获取当前脚本文件的绝对路径
current_script_path = os.path.abspath(__file__)

# 获取当前脚本所在的目录的上一级目录
parent_directory = os.path.dirname(os.path.dirname(current_script_path))

# 指向上一级目录中的 'lib' 文件夹
lib_path = os.path.join(parent_directory, 'lib')

# 将这个路径添加到 sys.path 中，使其成为可搜索的模块路径
sys.path.append(lib_path)

from ast_tool import AssemblyGenerator
import argparse


def read_file_contents(filename):
    """
    读取指定文件的全部内容并返回。

    参数:
        filename (str): 要读取的文件的路径名。

    返回:
        str: 文件的全部内容。
    """
    try:
        # 使用 'with' 语句确保文件正确关闭
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # 读取文件内容
        return content
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error while reading file: {e}")


def write_file_contents(filename, content):
    """
    将指定内容写入文件。

    参数:
        filename (str): 要写入的文件的路径名。
        content (str): 要写入的内容。
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error while writing file: {e}")


def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="Command line tool for processing files.")
    # 添加 `-path` 参数
    parser.add_argument('-path', required=True, help="Path to the input Python file")
    # 添加 `-o` 参数
    parser.add_argument('-o', required=True, help="Output file path for the converted C++ file")
    args = parser.parse_args()
    # 从 args 中提取 path 和 output 文件名
    input_path = args.path
    output_path = args.o

    source_code = read_file_contents(input_path)
    generator = AssemblyGenerator()
    asm_code = generator.generate_assembly(source_code)
    write_file_contents(output_path, asm_code)


if __name__ == "__main__":
    main()




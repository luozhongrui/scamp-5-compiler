import ast


class AssemblyGenerator(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.assembly_code = []

    def generic_visit(self, node):
        super().generic_visit(node)

    def visit_FunctionDef(self, node):
        self.assembly_code.append(f"scamp5_kernel_begin();")
        self.generic_visit(node)
        self.assembly_code.append("scamp5_kernel_end();")

    def visit_Assign(self, node):
        # 你可以根据具体的操作添加相应的汇编代码
        self.generic_visit(node)
        if node.targets[0].value.id != 'scamp5':
            raise ValueError("Only support scamp5 object")
        if node.targets[0].attr not in {'A', 'B', 'C', 'D', 'E', 'F'}:
            raise ValueError("Only support A, B, C D, E, F scamp5.Cisters")
        src = node.targets[0].attr
        if isinstance(node.value, ast.Call):
            # if node.value.func.value.id != 'scamp5':
            #     raise ValueError("Only support scamp5 object")
            if node.value.func.attr == 'load_value':
                self.assembly_code.append("scamp5_in({}, {});".format(src, node.value.args[0].value))
            if node.value.func.attr == 'get_image':
                self.assembly_code.append("get_image({});".format(src))

            if node.value.func.attr in {'north', 'south', 'west', 'east'}:
                dest = node.value.func.value.attr
                dir = node.value.func.attr
                self.assembly_code.append("movx({}, {}, {});".format(src, dest, dir))

            if node.value.func.attr in {'north_east', 'north_west', 'south_east', 'south_west', 'north_north', 'south_south', 'east_east', 'west_west'}:
                dest = node.value.func.value.attr
                dir = node.value.func.attr
                dir = dir.split('_')
                self.assembly_code.append("mov2x({}, {}, {}, {});".format(src, dest, dir[0], dir[1]))

    def visit_Expr(self, node):
        self.generic_visit(node)
        if isinstance(node.value, ast.Call):
            if node.value.func.value.id != 'scamp5':
                raise ValueError("Only support scamp5 object")
            if node.value.func.attr == 'where':
                src1 = node.value.args[0].left.attr
                option = node.value.args[0].ops[0]
                src2 = node.value.args[0].comparators[0].attr
                if isinstance(option, ast.LtE) or isinstance(option, ast.Lt):
                    self.assembly_code.append("sub({}, {}, {});".format(src2, src2, src1))
                    self.assembly_code.append("where({});".format(src2))
                    self.assembly_code.append("MOV(R12, FLAG);")
                    self.assembly_code.append("all();")
                    self.assembly_code.append("add({}, {}, {});".format(src2, src2, src1))
                    self.assembly_code.append("WHERE(R12);")
                elif isinstance(option, ast.GtE) or isinstance(option, ast.Gt):
                    self.assembly_code.append("sub({}, {}, {});".format(src1, src1, src2))
                    self.assembly_code.append("where({});".format(src1))
                    self.assembly_code.append("MOV(R12, FLAG);")
                    self.assembly_code.append("all();")
                    self.assembly_code.append("add({}, {}, {});".format(src1, src1, src2))
                    self.assembly_code.append("WHERE(R12);")
            if node.value.func.attr == 'mov':
                src1 = node.value.args[0].attr
                src2 = node.value.args[1].attr
                self.assembly_code.append("mov({}, {});".format(src1, src2))
            if node.value.func.attr == 'all':
                self.assembly_code.append("all();")

    def visit_Call(self, node):
        # if node.func.attr == 'where':
        #     src1 = node.args[0].left.attr
        #     option = node.args[0].ops[0]
        #     src2 = node.args[0].comparators[0].attr
        #     if isinstance(option, ast.LtE) or isinstance(option, ast.Lt):
        #         self.assembly_code.append("sub({}, {}, {});".format(src2, src2, src1))
        #         self.assembly_code.append("where({});".format(src2))
        #         self.assembly_code.append("MOV(R12, FLAG);")
        #         self.assembly_code.append("all();")
        #         self.assembly_code.append("add({}, {}, {});".format(src2, src2, src1))
        #         self.assembly_code.append("WHERE(R12);")
        #     elif isinstance(option, ast.GtE) or isinstance(option, ast.Gt):
        #         self.assembly_code.append("sub({}, {}, {});".format(src1, src1, src2))
        #         self.assembly_code.append("where({});".format(src1))
        #         self.assembly_code.append("MOV(R12, FLAG);")
        #         self.assembly_code.append("all();")
        #         self.assembly_code.append("add({}, {}, {});".format(src1, src1, src2))
        #         self.assembly_code.append("WHERE(R12);")
        # if node.func.attr == 'mov':
        #     src1 = node.args[0].attr
        #     src2 = node.args[1].attr
        #     self.assembly_code.append("mov({}, {});".format(src1, src2))
        # if node.func.attr == 'all':
        #     self.assembly_code.append("all();")
        self.generic_visit(node)

    # def visit_While(self, node):
    #     self.assembly_code.append("; Start of while loop")
    #     self.generic_visit(node)
    #     self.assembly_code.append("; End of while loop")

    def generate_assembly(self, source_code):
        tree = ast.parse(source_code)
        self.visit(tree)
        return "\n".join(self.assembly_code)


# 使用示例
if __name__ == "__main__":
    generator = AssemblyGenerator()
    source_code = """
def median_filter():
    scamp5.C = scamp5.B.west()
    scamp5.A = scamp5.B.north_west()
    
"""
    asm_code = generator.generate_assembly(source_code)
    print(asm_code)
    print("AST Structure:")
    parsed_code = ast.parse(source_code)
    # 使用 ast.dump 打印解析后的 AST 结构
    print(ast.dump(parsed_code, indent=4))

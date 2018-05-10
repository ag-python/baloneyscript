from subprocess import Popen

from .parser import parse
from .opcodes import command_to_op
import lark.lexer


def main(file):
    print(f'compiling {file}')

    with open(file, 'r') as f_in:
        code = f_in.read()
    try:
        tree = parse(code)
        # print(tree.pretty())
        scope = {}
        operations = [command_to_op(command.children[0], scope) for command in tree.children if command.data == 'command'] 

        with open(f"{file}.c", 'w+') as f_out:
            f_out.write("#include <stdio.h>\n#include \"baloney.h\"\nint main(){\n")
            
            for line, scope in operations:
                f_out.write("\t" + line)
            f_out.write("return 0; }")

        Popen(["gcc", f"{file}.c", "--save-stats", "-o",  f"{file}.bin"])
        
    except lark.lexer.UnexpectedInput as ue:
        print(f"Failed to compile : {ue}")
        exit(-1)

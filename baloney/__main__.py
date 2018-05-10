import argparse
from .compile import main as compiler
from .run import main as run

parser = argparse.ArgumentParser(
    description='Baloney Script interpreter')
parser.add_argument(
    'command', metavar='command', type=str,
    help='the command, e.g. compile, run')
parser.add_argument(
    'file', metavar='file', type=str,
    help='the target file (if compiling)')



if __name__ == '__main__':
    args = parser.parse_args()
    if args.command == 'compile':
        compiler(args.file)
    elif args.command == 'run':
        main(args)
    else:
        print("Command not recognised")

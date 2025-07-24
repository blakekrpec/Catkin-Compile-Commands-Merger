import os
import json
import argparse
import sys


def modify_compile_commands(file_path, old_prefix, new_prefix):
    with open(file_path, 'r') as file:
        compile_commands = json.load(file)

    for command in compile_commands:
        command['directory'] = command['directory'].replace(old_prefix, new_prefix)
        command['command'] = command['command'].replace(old_prefix, new_prefix)
        command['file'] = command['file'].replace(old_prefix, new_prefix)

    with open(file_path, 'w') as file:
        json.dump(compile_commands, file, indent=2)


def parse_args():
    parser = argparse.ArgumentParser(description='Modify paths in compile_commands.json')
    parser.add_argument('old_prefix', help='Old prefix path to be replaced')
    parser.add_argument('new_prefix', help='New prefix path to replace with')

    args = parser.parse_args()
    if not args.old_prefix or not args.new_prefix:
        parser.print_help()
        print("\nError: Both old_prefix and new_prefix are required.")
        sys.exit(1)

    return args


def main():
    args = parse_args()
    old_prefix = args.old_prefix
    new_prefix = args.new_prefix

    workspace_root = os.getcwd()
    compile_commands_file = os.path.join(workspace_root, 'compile_commands.json')

    if not os.path.isfile(compile_commands_file):
        print(f"Error: '{compile_commands_file}' not found")
        return

    modify_compile_commands(compile_commands_file, old_prefix, new_prefix)
    print(f"Success: Paths in '{compile_commands_file}' updated from '{old_prefix}' to '{new_prefix}'")


if __name__ == '__main__':
    main()

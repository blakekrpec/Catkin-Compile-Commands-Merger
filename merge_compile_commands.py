import os
import json


def find_compile_commands_files(build_dir):
    compile_commands_files = []
    for root, dirs, files in os.walk(build_dir):
        if 'compile_commands.json' in files:
            compile_commands_files.append(os.path.join(root, 'compile_commands.json'))
    return compile_commands_files


def merge_compile_commands(compile_commands_files):
    merged_commands = []
    for file in compile_commands_files:
        with open(file, 'r') as f:
            commands = json.load(f)
            merged_commands.extend(commands)
    return merged_commands


def dump_merged_commands(merged_commands, output_file):
    with open(output_file, 'w') as f:
        json.dump(merged_commands, f, indent=2)


def main():
    workspace_root = os.getcwd()
    build_dir = os.path.join(workspace_root, 'build')
    
    if not os.path.isdir(build_dir):
        print(f"Build directory '{build_dir}' not found")
        return

    compile_commands_files = find_compile_commands_files(build_dir)
    if not compile_commands_files:
        print(f"No 'compile_commands.json' files found in the '{build_dir}' directory")
        return

    merged_commands = merge_compile_commands(compile_commands_files)
    output_file = os.path.join(workspace_root, 'compile_commands.json')
    
    dump_merged_commands(merged_commands, output_file)
    print(f"Merged compile commands dumped to '{output_file}'")


if __name__ == '__main__':
    main()

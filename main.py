import os
import sys
import shutil
import re


def get_arg(arg_flag: str, arg_label: str, default_value):
    if arg_flag not in sys.argv:
        return default_value
    arg_index = sys.argv.index(arg_flag) + 1
    assert arg_index < len(sys.argv), f'{arg_label} should be entered after the {arg_flag} flag.'
    return sys.argv[arg_index]


def get_extractable_paths(src_dir_path: str, regex: re.Pattern[str] | None, min_depth: int, max_depth: int, curr_depth: int = 0) -> list[str]:
    if max_depth > -1 and max_depth < curr_depth:
        return []

    extractable_paths = []
    for item_name in os.listdir(src_dir_path):
        item_path = os.path.join(src_dir_path, item_name)
        if os.path.isdir(item_path):
            extractable_paths.extend(get_extractable_paths(item_path, regex, min_depth, max_depth, curr_depth + 1))
        elif min_depth <= curr_depth and (regex is None or regex.search(item_name)):
            extractable_paths.append(item_path)
    return extractable_paths


def extract_paths(extractable_paths: list[str], dest_dir_path: str):
    for src_item_path in extractable_paths:
        try:
            if '--preserve-metadata' in sys.argv:
                shutil.copy2(src_item_path, dest_dir_path)
            else:
                shutil.copy(src_item_path, dest_dir_path)
        except shutil.SameFileError:
            print(f'{src_item_path} cannot be copied on to itself.')
        else:
            print(f'{src_item_path} extracted successfully.')


def main():
    src_dir_path = get_arg('--src', 'Source directory', os.getcwd())
    dest_dir_path = get_arg('--dest', 'Destination directory', os.getcwd())
    regex_str = get_arg('--re', 'Regex', None)
    regex = re.compile(regex_str) if regex_str is not None else None
    min_depth = int(get_arg('--min-depth', 'Minimum Depth', -1))
    max_depth = int(get_arg('--max-depth', 'Maximum Depth', -1))

    assert os.path.isdir(src_dir_path), f'Source directory {src_dir_path} not found.'
    assert os.path.isdir(dest_dir_path), f'Destination directory {dest_dir_path} not found.'
    extract_paths(get_extractable_paths(src_dir_path, regex, min_depth, max_depth), dest_dir_path)


if __name__ == '__main__':
    main()


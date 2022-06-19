from os import remove, rename, path
from config import SHIFT_OFFSET


def decrypt(filename: str):
    src_name: str = filename
    dest_name: str = src_name.split('.enc')[0] if src_name.endswith('.enc') else f'{src_name}.dec'
    success_flag: bool = False

    try:
        # Decrypt as a text-based file
        with open(src_name, 'r') as src_file, open(dest_name, 'w') as dest_file:
            for char in src_file.read():
                dest_file.write(chr(ord(str(char)) - SHIFT_OFFSET))
        success_flag = True

    except UnicodeDecodeError:
        # Decrypt as a byte-based file
        with open(src_name, 'rb') as src_file, open(dest_name, 'wb') as dest_file:
            line_idx: int = 0
            for line in src_file:
                if line_idx % 2 == 1:
                    dest_file.write(line)
                line_idx += 1
        success_flag = True

    if success_flag:
        remove(src_name)
        if dest_name.endswith('.dec'):
            rename(dest_name, dest_name.split('.dec')[0])
    else:
        print('Can not decrypt it!')
        if path.exists(dest_name): remove(dest_name)

from os import remove, path
from config import SHIFT_OFFSET


def encrypt(filename: str):
    src_name: str = filename
    dest_name: str = f'{src_name}.enc'
    success_flag: bool = False

    try:
        # Encrypt as a text-based file
        with open(src_name, 'r') as src_file, open(dest_name, 'w') as dest_file:
            for char in src_file.read():
                dest_file.write(chr(ord(str(char)) + SHIFT_OFFSET))
        success_flag = True

    except UnicodeDecodeError:
        # Encrypt as a byte-based file
        with open(src_name, 'rb') as src_file, open(dest_name, 'wb') as dest_file:
            for line in src_file:
                dest_file.write(b'\x0b\n' + line)
        success_flag = True

    if success_flag:
        remove(src_name)
    else:
        print('Can not encrypt it!')
        if path.exists(dest_name): remove(dest_name)

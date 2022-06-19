#!/bin/python3
from os import path
from sys import argv, exit
from encrypt import encrypt
from decrypt import decrypt


def main():
    operation = argv[1]
    filename = argv[2]

    if (
        len(argv) < 3
        or operation not in ['--enc', '--dec']
        or not path.exists(filename)
    ):
        print('Encrypt:\tcryptic -enc <filename>\nDecrypt:\tcryptic -dec <filename>')
        exit()

    if operation == '--enc':
        encrypt(filename)
    else: decrypt(filename)


if __name__ == '__main__':
    main()

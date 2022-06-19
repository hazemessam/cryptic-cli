# Cryptic

## Description
Cryptic is a Python CLI tool that encrypts and decrypts any type of files. The tool firstly tries to encrypt/decrypt the file as a text based file using the caesar cipher and if it throws an `UnicodeDecodeError` exception, the tool detects that it is a byte based file and encrypt it using an encryption algorithm that reads the file line by line and add a specific byte line between every two successive lines and when the user tries to decrypt the file it removes the added specific byte lines from the file.

## File Structure
- ### \_\_init__.py
    It is an empty file that makes Python deal the directory as a one package.

- ### cryptic.py
    The main file and the file that runs the project. It fetchs the command line arguments and checks if the operation type is correct and also checks if the file is exists then run the required operation on the specified file.

- ### encrypt.py
    It contains the encryption algorithm.

- ### decrypt.py
    It contains the decryption algorithm.

- ### config.py
    It stores the global variables that are needed to get accessed from multiple files like `SHIFT_OFFSET` to avoid the circular dependency problem.

## Usage
### Encrypt file:
```
$ python cryptic.py --enc <filename>
```
### Decrypt file:
```
$ python cryptic.py --dec <filename>
```

## Video Demo
https://youtu.be/GBTJcRQYLzY

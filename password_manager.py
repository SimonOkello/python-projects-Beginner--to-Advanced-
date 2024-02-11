import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_password = input('What is your master password?: ')

key = load_key()
fer = Fernet(key)

'''
def write_key():
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


write_key()
'''


def view():
    with open('passwords.txt', 'r') as pwd_file:
        for line in pwd_file.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print('User:', user, '| Password:',
                  fer.decrypt(password).decode())


def add():
    username = input('Account Name: ')
    password = input('Account Password: ')

    with open('passwords.txt', 'a') as pwd_file:
        pwd_file.write(
            f'{username}|{fer.encrypt(password.encode()).decode()}\n')


while True:
    mode = input(
        'Would you like to add a new password or view existing ones(add/view),press q to quit: ').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid choice')
        continue

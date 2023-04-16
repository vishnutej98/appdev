from cryptography.fernet import Fernet
import getpass


def main():
    password_from_user = getpass.getpass(prompt="Enter the password: ")

    # Check the below link for byte implimentation
    # https://stackoverflow.com/questions/43013931/how-to-read-bytes-from-user-in-python

    
    with open('secret.key', 'r') as fp:
        key_secret = fp.read()
    password_len = len(password_from_user)
    user_option = int(input('''
    1. Encryption
    2. Decryption

    '''))
    User_option(user_option, password_from_user, key_secret)


def func():
    with open('secret.key', 'r') as fp:
        return fp.read()


def User_option(user_option, password_form_user, key_secret):
    if user_option != 2:
        EP = EncPass(password_form_user)
        print(EP)

    else:
        DP = DecPass(password_form_user, key_secret)
        print(DP)


def EncPass(password_from_user):
    key = func()
    fernet = Fernet(key)
    enc_pass = fernet.encrypt(password_from_user.encode())
    return enc_pass


def DecPass(password_from_user, KEY):
    key = func()
    fernet = Fernet(key)
    dec_pass = fernet.decrypt(password_from_user).decode()
    return dec_pass

if __name__ == '__main__':
    main()

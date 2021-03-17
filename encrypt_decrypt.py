import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import file_functions


def key_generation():
    """
    Generate random encryption key
    :return: key: bytes
    """
    key = get_random_bytes(32)
    print(key)
    file_functions.fileWriting(key)
    return key


def cipher_generation(key: bytes):
    """
    Generate Encryption-Cipher
    :param key: Encryption-key
    :return: Encryption-Cipher
    """
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher


def encrypt(message: str, key: bytes = None):
    """
    Encrypt Data using AES encryption with random IV, nonce and 256-bit key length
    :param key: Encryption key
    :param message: Message to encrypt in string format
    :return: Encrypted data in string format
    """
    if key is None:
        key = key_generation()

    if type(message) not in [str]:
        raise TypeError('The input type can only be a valid String!')

    cipher = cipher_generation(key)
    ciphertext = cipher.encrypt(pad(str_to_bytes(message), 32))
    return_list = [str(base64.b64encode(ciphertext), 'utf-8'), key]
    return return_list


def decrypt(cipher: str):
    """
    Decrypt Data to retrieve original plaintext from encrypted data
    :param cipher: list consisting of ciphertext, key, nonce and tag
    :return: decrypted Data in string format
    """
    ciphertext = cipher
#   key = cipher[1]
    key = file_functions.fileOpening()

    if type(ciphertext) not in [str] and type(key) not in [bytes]:
        raise TypeError('The input type can only be a valid String!')

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    return bytes_to_str(plaintext)


def str_to_bytes(message: str):
    """
    Convert String message into Byte in 'utf-8'
    :param message: plaintext in string format
    :return: Message in Bytes
    """
    if type(message) not in [str]:
        raise TypeError('The input type can only be a valid String!')

    message_bytes = bytes(message, 'utf-8')
    return message_bytes


def bytes_to_str(message_bytes: bytes):
    """
    Convert Message in Byte to String format
    :param message_bytes: Message in Bytes
    :return: Message in String format
    """
    if type(message_bytes) not in [bytes]:
        raise TypeError('The input type can only be a valid Byte!')

    message_str = unpad(message_bytes, 32).decode("utf-8")
    return message_str

import os


def fileWriting(input_key: bytes):
    """
    Write Encryption keys in .txt-file
    If file doesnt exist --> create file
    If file exists --> append to file
    :param input_key: the key to add/write to the file
    :return: none
    """
    if not os.path.exists("EncryptionKey.txt"):
        f = open("EncryptionKey.txt", "wb")
        f.write(input_key)
        f.close()


def fileOpening():
    """
    Open File to read Encryption key(s)
    :return: none
    """
    contents = ""
    f = open("EncryptionKey.txt", "rb")
    if f.mode == 'rb':
        contents = f.read()
    return contents

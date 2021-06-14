import binascii


def encode_message(message: str):
    """
    Encode Message into Hex
    :param message: Message in string format
    :return: new Hex-Message in string format
    """
    if type(message) not in [str]:
        raise TypeError('The input type can only be a valid String!')

    msg_bytes = message.encode("utf-8")
    msg_str = binascii.hexlify(msg_bytes)
    msg_str = str(msg_str, "utf-8")
    return msg_str


def str_to_hex_list(message: str):
    """
    Convert ASCII-string into Hex-List using encode_message-Method
    :param message: Message in string method
    :return: List with two chars joined in Hex-format on each position
    """
    if type(message) not in [str]:
        raise TypeError('The input type can only be a valid String!')

    char_list = []
    char_iter = iter(encode_message(message))
    for char in char_iter:
        char_list.append(char + next(char_iter))
    return char_list


def decode_message(s: list):
    """
    Decode Hex into String Message
    :param s: Hex-Message in string format
    :return: Message in ASCII-Format (string)
    """
    if type(s) not in [list]:
        raise TypeError('The input type can only be a valid List!')

    dec_message_string = ''.join([str(elem) for elem in s])
    decode_bytes = binascii.unhexlify(bytes(dec_message_string, encoding='utf8'))
    decode_str = decode_bytes.decode("utf-8")
    return decode_str


def str_from_hex_list(message: list):
    """
    Convert hex-list to string using decode_str-Method
    :param message: Hex-List in string-Format
    :return: Message in ASCII-String
    """
    if type(message) not in [list]:
        raise TypeError('The input type can only be a valid String!')

    result = decode_message(message)
    return result.replace(" ", "")

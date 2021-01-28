import scapy.all as scapy
import sys
import base64,binascii

def encode_message(message: str):
	msgBytes = base64.b64encode(message.encode("utf-8"))
	print('Encoded Base64: ',msgBytes)
	msgStr = binascii.hexlify(msgBytes)
	print('Encoded Hex: ',msgStr)
	msgStr = str(msgStr, "utf-8")
	return msgStr

def str_to_hex_list(message: str):
	char_list = []
	char_iter = iter(encode_message(message))
	for char in char_iter:
		char_list.append(char + next(char_iter))
	return char_list



def decode_str(s: str): 
    decodeBytes = binascii.unhexlify(bytes(s, encoding='utf8'))
    print('Decoded Base64: ',decodeBytes)
    decodeStr = base64.b64decode(decodeBytes)
    print('Decoded String: ',decodeStr)
    decodeStr = str(decodeStr, "utf-8")
    return decodeStr


def str_from_hex_list(message: str):
    result = decode_str(message)
    return result


if __name__ == '__main__':
	message = sys.argv[1]
	print('\n','INPUT: ',message,'\n')
	encMessage = str_to_hex_list(message)
	encMessage_String = ' '.join([str(elem) for elem in encMessage])
	print('\n','ENCODED: ',encMessage,'\n','  -->  ',encMessage_String,'\n')

	decMessage = str_from_hex_list(encMessage_String.replace(" ",""))
	print('\n','DECODED: ',decMessage)














import encrypt_decrypt
import encode_decode
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    encryption = encrypt_decrypt.encrypt(sys.argv[1])
    message = encryption[0]
    print('\n', 'INPUT ENCRYPTED: ', message, '\n')
    encMessage = encode_decode.str_to_hex_list(message)
    print(encMessage)
    encMessage_String = ' '.join([str(elem) for elem in encMessage])
    print('\n', 'ENCODED: ', encMessage, '\n', '  -->  ', encMessage_String, '\n')

    decMessage = encode_decode.str_from_hex_list(encMessage)
    print(decMessage)
    print('\n', 'DECRYPTED: ', encrypt_decrypt.decrypt(encryption[0]))

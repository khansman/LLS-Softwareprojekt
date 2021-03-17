import unittest
import random
import string
import sys

sys.path.append("..")
import encrypt_decrypt


def random_string_generator():
    return ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(20))


class TestEncryptionDecryption(unittest.TestCase):

    def test_EqualWithSameKey(self):
        key = encrypt_decrypt.key_generation()
        print("\n key = ", key)
        self.assertEqual(encrypt_decrypt.encrypt("Test", key), encrypt_decrypt.encrypt("Test", key))
        self.assertEqual(encrypt_decrypt.encrypt("Dies ist ein Unit Test", key),
                         encrypt_decrypt.encrypt("Dies ist ein Unit Test", key))
        self.assertEqual(encrypt_decrypt.encrypt("", key), encrypt_decrypt.encrypt("", key))

    # def test_EqualCipher(self):
    #   key = encrypt_decrypt.key_generation()
    #  self.assertEqual(encrypt_decrypt.cipher_generation(key), encrypt_decrypt.cipher_generation(key))

    def test_EncodingDecoding_RndString(self):
        for i in range(100):
            rnd = random_string_generator()
            print(i, ": ", rnd)
            self.assertEqual(rnd, encrypt_decrypt.decrypt(encrypt_decrypt.encrypt(rnd)))

    def test_EncodingDecoding_Empty(self):
        self.assertEqual("", encrypt_decrypt.decrypt(encrypt_decrypt.encrypt("")))

    def test_EncodingDecoding_NotString(self):
        self.assertRaises(TypeError, encrypt_decrypt.encrypt, 1)
        self.assertRaises(TypeError, encrypt_decrypt.encrypt, True)
        self.assertRaises(TypeError, encrypt_decrypt.encrypt, 1.0)

        self.assertRaises(TypeError, encrypt_decrypt.decrypt, [1, 1, 1, 1])
        self.assertRaises(TypeError, encrypt_decrypt.decrypt, [True, True, True, True])
        self.assertRaises(TypeError, encrypt_decrypt.decrypt, [1.0, 1.0, 1.0, 1.0])


if __name__ == '__main__':
    unittest.main()

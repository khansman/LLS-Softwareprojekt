import unittest
import sys
import string
import random

sys.path.append("..")
import encode_decode


def random_string_generator():
    return ''.join(random.SystemRandom().choice(
        string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(20))


class TestEncodingDecoding(unittest.TestCase):

    def test_EncodingDecoding_RndString(self):
        for i in range(100):
            rnd = random_string_generator()
            print(i, ": ", rnd)
            self.assertEqual(rnd, encode_decode.str_from_hex_list(encode_decode.str_to_hex_list(rnd)))

    def test_EncodingDecoding_Empty(self):
        self.assertEqual("", encode_decode.str_from_hex_list(encode_decode.str_to_hex_list("")))

    def test_EncodingDecoding_NotString(self):
        self.assertRaises(TypeError, encode_decode.str_from_hex_list, 1)
        self.assertRaises(TypeError, encode_decode.str_from_hex_list, True)
        self.assertRaises(TypeError, encode_decode.str_from_hex_list, 1.0)

        self.assertRaises(TypeError, encode_decode.str_to_hex_list, 1)
        self.assertRaises(TypeError, encode_decode.str_to_hex_list, True)
        self.assertRaises(TypeError, encode_decode.str_to_hex_list, 1.0)


if __name__ == '__main__':
    unittest.main()

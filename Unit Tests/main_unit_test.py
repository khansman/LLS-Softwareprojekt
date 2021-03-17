import unittest
import encoding_unit_test
import encryption_unit_test


class MainUnitTest(unittest.TestCase):

    def test_Encoding(self):
        encoding_unit_test.TestEncodingDecoding.test_EncodingDecoding_Empty(self)
        encoding_unit_test.TestEncodingDecoding.test_EncodingDecoding_RndString(self)
        encoding_unit_test.TestEncodingDecoding.test_EncodingDecoding_NotString(self)

    def test_Encryption(self):
        encryption_unit_test.TestEncryptionDecryption.test_EqualWithSameKey(self)
#       encryption_unit_test.TestEncryptionDecryption.test_EqualCipher(self)
        encryption_unit_test.TestEncryptionDecryption.test_EncodingDecoding_Empty(self)
        encryption_unit_test.TestEncryptionDecryption.test_EncodingDecoding_RndString(self)
        encryption_unit_test.TestEncryptionDecryption.test_EncodingDecoding_NotString(self)


if __name__ == '__main__':
    unittest.main()

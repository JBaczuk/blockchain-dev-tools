import unittest
from blockchain_fundamentals import *

#class TestLE32toBE(unittest.TestCase):
    # todo

class TestBitsToTarget(unittest.TestCase):
    def test_one(self):
        self.assertEqual(BitsToTarget('181bc330'), '00000000000000001bc330000000000000000000000000000000000000000000')

class TestReverseEndian(unittest.TestCase):
    def test_one(self):
        self.assertEqual(ReverseEndian('deadbeef'), 'efbeadde')

class TestSha256(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(sha256('deadbeef').hex(), '5f78c33274e43fa9de5659265c1d917e25c03722dcb0b8d27db8d5feaa813953')

class TestHash256(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(hash256('deadbeef').hex(), '281dd50f6f56bc6e867fe73dd614a73c55a647a479704f64804b574cafb0f5c5')

class TestHash160(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(hash160('deadbeef').hex(), 'f04df4c4b30d2b7ac6e1ed2445aeb12a9cb4d2ec')

class TestHash160(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(ripemd160('deadbeef').hex(), '226821c2f5423e11fe9af68bd285c249db2e4b5a')

class TestBase58Encode(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(base58encode('deadbeef').decode('utf-8'), '6h8cQN')

class TestBase58Decode(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(base58decode('6h8cQN').hex(), 'deadbeef')

class TestBase58CheckEncode(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(base58encode_check('deadbeef').decode('utf-8'), 'eFGDJPketnz')

class TestBase58CheckDecode(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(base58decode_check('eFGDJPketnz').hex(), 'deadbeef')

if __name__ == '__main__':
    unittest.main()

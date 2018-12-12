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
        self.assertEqual(sha256('deadbeef'), '5f78c33274e43fa9de5659265c1d917e25c03722dcb0b8d27db8d5feaa813953')

class TestHash256(unittest.TestCase):
    def test_deadbeef(self):
        self.assertEqual(hash256('deadbeef'), '281dd50f6f56bc6e867fe73dd614a73c55a647a479704f64804b574cafb0f5c5')

if __name__ == '__main__':
    unittest.main()

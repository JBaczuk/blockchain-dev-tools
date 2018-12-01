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

if __name__ == '__main__':
    unittest.main()

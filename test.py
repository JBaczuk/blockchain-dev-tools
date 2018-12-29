import unittest
from blockchain_fundamentals import *

#class TestLE32toBE(unittest.TestCase):
    # todo

class TestToPublicKey(unittest.TestCase):
    def test_sha_zero(self):
        self.assertEqual(ToPublicKey('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'), '04a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd5b8dec5235a0fa8722476c7709c02559e3aa73aa03918ba2d492eea75abea235')
    def test_invalid_privkey(self):
        self.assertRaises(TypeError, ToPublicKey, 'something not hex')
    def test_privkey_length_incorrect(self):
        self.assertRaises(ValueError, ToPublicKey, 'deadbeef')

class TestToCompressedKey(unittest.TestCase):
    def test_sha_zero(self):
        self.assertEqual(ToCompressedKey('04a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd5b8dec5235a0fa8722476c7709c02559e3aa73aa03918ba2d492eea75abea235'), '03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd')
    def test_invalid_pubkey(self):
        self.assertRaises(TypeError, ToCompressedKey, 'something not hex')
    def test_pubkey_length_incorrect(self):
        self.assertRaises(ValueError, ToCompressedKey, 'deadbeef')

class TestToWIF(unittest.TestCase):
    def test_sha_zero_mainnet(self):
        self.assertEqual(ToWIF('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'mainnet').decode('utf-8'), 'L4rK1yDtCWekvXuE6oXD9jCYfFNV2cWRpVuPLBcCU2z8TrisoyY1')
    def test_sha_zero_testnet(self):
        self.assertEqual(ToWIF('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'testnet').decode('utf-8'), 'cVDJUtDjdaM25yNVVDLLX3hcHUfth4c7tY3rSc4hy9e8ibtCuj6G')
        self.assertEqual(ToWIF('e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'regtest').decode('utf-8'), 'cVDJUtDjdaM25yNVVDLLX3hcHUfth4c7tY3rSc4hy9e8ibtCuj6G')
    def test_invalid_network(self):
        self.assertRaises(ValueError, ToWIF, 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'invalid')
    def test_invalid_privkey(self):
        self.assertRaises(TypeError, ToWIF, 'something not hex', 'mainnet')
    def test_privkey_length_incorrect(self):
        self.assertRaises(ValueError, ToWIF, 'deadbeef', 'mainnet')

class TestToP2PKH(unittest.TestCase):
    def test_sha_zero_mainnet(self):
        self.assertEqual(ToP2PKH('03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'mainnet').decode('utf-8'), '1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV')
    def test_sha_zero_testnet(self):
        self.assertEqual(ToP2PKH('03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'testnet').decode('utf-8'), 'muZpTpBYhxmRFuCjLc7C6BBDF32C8XVJUi')
        self.assertEqual(ToP2PKH('03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'regtest').decode('utf-8'), 'muZpTpBYhxmRFuCjLc7C6BBDF32C8XVJUi')
    def test_invalid_network(self):
        self.assertRaises(ValueError, ToP2PKH, '03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'invalid')
    def test_invalid_pubkey(self):
        self.assertRaises(TypeError, ToCompressedKey, 'something not hex')
    def test_pubkey_length_incorrect(self):
        self.assertRaises(ValueError, ToCompressedKey, 'deadbeef')

class TestToP2SHP2WPKH(unittest.TestCase):
    def test_sha_zero_mainnet(self):
        self.assertEqual(ToP2SHP2WPKH('03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'mainnet').decode('utf-8'), '3DnW8JGpPViEZdpqat8qky1zc26EKbXnmM')
    def test_sha_zero_testnet(self):
        self.assertEqual(ToP2SHP2WPKH('03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'testnet').decode('utf-8'), '2N5LiC3CqzxDamRTPG1kiNv1FpNJQ7x28sb')
        self.assertEqual(ToP2SHP2WPKH('03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'regtest').decode('utf-8'), '2N5LiC3CqzxDamRTPG1kiNv1FpNJQ7x28sb')
    def test_invalid_network(self):
        self.assertRaises(ValueError, ToP2SHP2WPKH, '03a34b99f22c790c4e36b2b3c2c35a36db06226e41c692fc82b8b56ac1c540c5bd', 'invalid')
    def test_invalid_pubkey(self):
        self.assertRaises(TypeError, ToCompressedKey, 'something not hex')
    def test_pubkey_length_incorrect(self):
        self.assertRaises(ValueError, ToCompressedKey, 'deadbeef')

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

#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert private key from hex to Wallet Import Format (WIF)')
    parser.add_argument('privkey', metavar='privkey')
    parser.add_argument('-n', '--network', choices=('mainnet', 'testnet', 'regtest'), default='mainnet')
    parser.add_argument('-u', '--uncompressed', action='store_true')
    args = parser.parse_args()
    
    wif = ToWIF(args.privkey, args.network, not args.uncompressed)

    print(wif.decode('utf-8'))

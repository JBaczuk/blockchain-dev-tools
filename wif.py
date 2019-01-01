#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert private key from hex to Wallet Import Format (WIF)')
    parser.add_argument('privkey', metavar='privkey')
    parser.add_argument('-m', '--mainnet', action='store_true', default=True)
    parser.add_argument('-t', '--testnet', action='store_true')
    parser.add_argument('-r', '--regtest', action='store_true')
    args = parser.parse_args()

    if args.mainnet:
        network = 'mainnet'
    elif args.testnet:
        network = 'testnet'
    else:
        network = 'regtest'
    
    wif = ToWIF(args.privkey, network)

    print(wif.decode('utf-8'))

#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate P2PKH address from compressed public key')
    parser.add_argument('pubkey', metavar='pubkey')
    parser.add_argument('-m', '--mainnet', action='store_true', default=True)
    parser.add_argument('-t', '--testnet', action='store_true')
    parser.add_argument('-r', '--regtest', action='store_true')
    args = parser.parse_args()

    if args.mainnet:
        address = ToP2PKH(args.pubkey, 'mainnet').decode('utf-8')
    if args.testnet:
        address = ToP2PKH(args.pubkey, 'testnet').decode('utf-8')
    if args.regtest:
        address = ToP2PKH(args.pubkey, 'regtest').decode('utf-8')

    print(address)

#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate keys and addresses for a private key.')
    parser.add_argument('value', metavar='value')
    args = parser.parse_args()

    if not isHex(args.value):
        print('Private key must be valid hex')
    if len(args.value) != 64:
        print('Private key must be 32 bytes')

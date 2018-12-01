#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform the SHA256 function on input hex string')
    parser.add_argument('hexStr', metavar='hexStr')
    args = parser.parse_args()

    print('result:', sha256(args.hexStr))


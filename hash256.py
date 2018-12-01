#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform a double SHA256 function on input hex string')
    parser.add_argument('hexStr', metavar='hexStr')
    args = parser.parse_args()

    print('result:', hash256(args.hexStr))


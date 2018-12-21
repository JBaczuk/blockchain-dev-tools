#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reverse the endianness of a hex string')
    parser.add_argument('hexStr', metavar='hexStr')
    args = parser.parse_args()

    print(ReverseEndian(args.hexStr))


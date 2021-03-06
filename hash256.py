#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform a double SHA256 function on input string. Can be hex or ascii.')
    parser.add_argument('value', metavar='value')
    args = parser.parse_args()

    result = hash256(args.value)
    print(result.hex())

#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert bits from compact to extended format')
    parser.add_argument('bits', metavar='bits')
    args = parser.parse_args()

    if (len(args.bits) != 8):
        print('bits arg must by 4 bytes')
        parser.print_help()
        exit()

    print(BitsToTarget(args.bits))


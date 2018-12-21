#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert bits to and from compact or extended format')
    parser.add_argument('value', metavar='value')
    parser.add_argument('-c', '--to_compact', action='store_true')
    args = parser.parse_args()

    if args.to_compact:
        print('coming soon')
        parser.print_help()
        #if(len(args.value) != 64):
        #    print('target value must be 32 bytes')
        #    parser.print_help()
        #    exit()
        #else:
        #    result = TargetToBits(args.value)
    else:
        if (len(args.value) != 8):
            print('bits value must be 4 bytes')
            parser.print_help()
            exit()
        else:
            result = BitsToTarget(args.value)

    print(result)


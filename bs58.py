#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encode/decode using base58 or base58check. Can be hex or utf-8.')
    parser.add_argument('value', metavar='value')
    parser.add_argument('-c', '--check', action='store_true')
    parser.add_argument('-d', '--decode', action='store_true')
    args = parser.parse_args()

    if not args.check and not args.decode:
        result = base58encode(args.value).decode('utf-8') 
    elif args.check and not args.decode:
        result = base58encode_check(args.value).decode('utf-8')
    elif not args.check and args.decode:
        result = base58decode(args.value).hex()
    elif args.check and args.decode:
        result = base58decode_check(args.value).hex()
    
    print(result);

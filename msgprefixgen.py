#!/usr/bin/env python3

import argparse
from blockchain_fundamentals import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate random message prefix bytes in upper ASCII for all networks')
    #parser.add_argument('value', metavar='value')
    args = parser.parse_args()

    genMsgPrefix()


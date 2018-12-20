import struct
import hashlib
import random

def LE32toBE(value):
    return struct.unpack("<I", struct.pack(">I", value))[0]

def BE256toLE(value):
    valueStr = hex(value)[2:]
    reversedStr = ""
    for i, c in enumerate(valueStr):
        if (i % 2 == 0):
            reversedStr = valueStr[i-1] + c + reversedStr
    return int(reversedStr, 16)

def BitsToTarget(bits):
    # reverse endianess
    bitsInt = int(bits, 16)

    exponent = (bitsInt & 0xff000000) >> 8 * 3
    mantissa = bitsInt & 0x00ffffff

    target = mantissa * 256 ** (exponent - 3)
    return "{0:0{1}x}".format(target, 64)

def ReverseEndian(line):
    n = 2
    orig_list = [line[i:i+n] for i in range(0, len(line), n)]
    reversed_list = orig_list[::-1]
    reversedStr = ''.join(reversed_list)
    return reversedStr

def sha256(value):
    try:
        int(value, 16)
        return hashlib.sha256(bytes.fromhex(value)).digest().hex()
    except ValueError:
        return hashlib.sha256(value.encode('utf-8')).digest().hex()
    except:
        raise

def hash256(value):
    return sha256(sha256(value))

def ripemd160(value):
    try:
        int(value, 16)
        return hashlib.new('ripemd160', bytes.fromhex(value)).digest().hex()
    except ValueError:
        return hashlib.new('ripemd160', value.encode('utf-8')).digest().hex()
    except:
        raise Exception("Input format not understood")

def hash160(value):
    return ripemd160(sha256(value))

def genMsgPrefix():
    networks = ['Mainnet', 'Testnet', 'Regtest']
    for network in networks:
        print(network)
        print("pchMessageStart[0] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print("pchMessageStart[1] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print("pchMessageStart[2] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print("pchMessageStart[3] = ", hex(random.sample(range(0x80, 0xff), 1)[0]), ";", sep='')
        print()


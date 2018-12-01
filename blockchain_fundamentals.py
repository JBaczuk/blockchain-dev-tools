import struct
import hashlib

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
    reversed = ''.join(reversed_list)
    return reversed

def sha256(hexStr):
    return hashlib.sha256(bytes.fromhex(hexStr)).digest().hex()

def hash256(hexStr):
    return sha256(sha256(hexStr))

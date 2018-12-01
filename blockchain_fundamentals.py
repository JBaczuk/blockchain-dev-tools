import struct

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

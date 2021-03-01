from bitarray import bitarray
from random import randint


def GenerateRandomKey(length: int) -> list:
    return [randint(0, 1) for i in range(length)]


def BitarrayToBinary(ba: bitarray) -> list:
    return ba.to01()


def StringToBitarray(msg: str) -> bitarray:
    ba = bitarray()
    ba.frombytes(msg.encode('utf-8'))
    return ba


def BitarrayToString(bits: bitarray) -> list:
    ba = bitarray(bits)
    return ba.tobytes().decode('utf-8')


def BinaryToBitarray(string: str) -> bitarray:
    return bitarray(string)


def ApplyPadToBits(bits: bitarray, pad: bitarray) -> bitarray:
    return bitarray([b ^ p for b, p in zip(bits, pad)])

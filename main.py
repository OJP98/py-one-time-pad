import sys
import getopt
from cypher import *
from utils import *

HELP_MSG = '''
To cypher a message:
> python main.py -c
> python main.py --cypher


To decypher a message:
> python main.py -d -i <msgfile> -k <keyfile>
> python main.py --decypher --inputfile <msgfile> -keyfile <keyfile>
'''


def main(argv):
    cypher = True
    input_file = False
    key_file = False

    try:
        opts, _ = getopt.getopt(
            argv, 'hi:k:dc:', ['inputfile=', 'keyfile=', 'decypher', 'cypher'])
    except getopt.GetoptError:
        print(HELP_MSG)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(HELP_MSG)
            sys.exit()
        elif opt in ('-i', '--inputfile'):
            input_file = arg
        elif opt in ('-k', '--keyfile'):
            key_file = arg
        elif opt in ('-c', '--cypher'):
            cypher = True
        elif opt in ('-d', '--decypher'):
            cypher = False

    if not cypher:
        if not input_file or not key_file:
            print('Missing file input!')
            print(HELP_MSG)
            sys.exit()

    return cypher, input_file, key_file


def CypherMessage(message: str):
    ba = StringToBitarray(message)
    key = GenerateRandomKey(len(ba))

    cyphered = ApplyPadToBits(ba, key)
    binary_cyphered = BitarrayToBinary(cyphered)
    key_str = ''.join(str(i) for i in key)

    print(f'''
        Message: {message}
        Generated key:
            {key_str}
        Encrypted message:
            {binary_cyphered}
        ''')

    cyphered_filename = WriteToFile('cyphered.txt', binary_cyphered)
    print(cyphered_filename)
    key_filename = WriteToFile('key.txt', key_str)
    print(key_filename)


def DecypherMessage(message: str, key: str):
    c_msg_ba = BinaryToBitarray(message)
    key_ba = BinaryToBitarray(key)

    msg_ba = ApplyPadToBits(c_msg_ba, key_ba)
    msg = BitarrayToString(msg_ba)

    print(f'''
        The message is the following:
        "{msg}"
        ''')


if __name__ == "__main__":
    cypher, inp, key = main(sys.argv[1:])

    if cypher:
        print('Cypher!')
        message = input('Enter a message to cypher: ')
        CypherMessage(message)
        sys.exit(1)
    else:
        print('Decypher!')
        cyphered_msg = GetFileContent(inp)
        key = GetFileContent(key)
        DecypherMessage(cyphered_msg, key)
        sys.exit(1)

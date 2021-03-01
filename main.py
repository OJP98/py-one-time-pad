import sys
import getopt
# from cypher import *
# from utils import *

HELP_MSG = '''
To cypher a message:
> python main.py -c -i <msgfile>
> python main.py --cypher --inputfile <msgfile>


To decypher a message:
> python main.py -d -i <msgfile> -k <keyfile>
> python main.py --decypher --inputfile <msgfile> -keyfile <keyfile>
'''


def main(argv):
    cypher = True
    input_file = False
    key_file = False

    try:
        opts, args = getopt.getopt(
            argv, 'hi:k:dc', ['inputfile=', 'keyfile=', 'decypher', 'cypher'])
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

    if not input_file:
        print('Missing file input!')
        print(HELP_MSG)
        sys.exit()
    elif not cypher and not key_file:
        print('Missing key input!')
        print(HELP_MSG)
        sys.exit()

    return cypher, input_file, key_file


if __name__ == "__main__":
    cypher, inp, key = main(sys.argv[1:])

    if cypher:
        print('Cypher!')
        print(inp)
    else:
        print('Decypher!')

from FileHandler import FileHandler
import sys

class PDA:
    def __init__(self):
        self.stack = []


def main():
    fh = FileHandler()
    pda = PDA()
    pdaFilePath = sys.argv[1]
    lines = fh.readFile(pdaFilePath)
    inputStringFilePath = sys.argv[2]
    with open(inputStringFilePath, 'r') as inputStringFile:
        inputString = inputStringFile.read().replace('\n', '').replace(' ','')
    print(inputString)
    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Starting State: ', parsedLines['starting_state'])
    print('Starting Stack: ', parsedLines['starting_stack'])
    print('Accepting States: ', parsedLines['accepting_states'])
    print('Accept By: ', parsedLines['accept_by'])
    print('Productions List:')
    for production in parsedLines['productions']:
        print('\t', production)

if __name__ == '__main__':
    main()

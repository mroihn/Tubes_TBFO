from FileHandler import FileHandler
import sys
import lexer
import os

class PDA:
    def __init__(self, states, alphabet, stack_alphabet, initial_state, initial_stack_symbol, transitions, final_states):
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.transitions = transitions
        self.final_states = final_states
        self.stack = []

    def reset(self):
        self.stack = [self.initial_stack_symbol]

    def process_input(self, inputString):
        currentStackSymbol = self.initial_stack_symbol
        currentState = self.initial_state
        self.stack.append(currentStackSymbol)
        for symbol in inputString:
            # print(symbol)
            self.cek = False
            for transition in self.transitions:
                if ((transition[0] == currentState) and (transition[1] == symbol) and (transition[2] == currentStackSymbol)):
                    # print('{} {} {} {} {} {} {}'.format(transition[0],currentState,transition[1],symbol,transition[2],currentStackSymbol,transition[3]))
                    currentState = transition[3]
                    # print(symbol)
                    self.stack.pop()
                    if(transition[4] !='epsilon'):
                        for el in transition[4][::-1]:
                            self.stack.append(el)
                    currentStackSymbol = self.stack[len(self.stack)-1]
                    self.cek = True
            if(self.cek == False):
                return False

        if(currentStackSymbol == self.initial_stack_symbol):
            print('String accepted by PDA.')
            return True
        else:
            print('String rejected by PDA.')
            return False
        


def main():
    fh = FileHandler()

    
    pdaFilePath = sys.argv[1]
    lines = fh.readFile(pdaFilePath)
    inputStringFilePath = sys.argv[2]
    token = lexer.createToken(inputStringFilePath)
    token = list(filter(lambda x: x != 'ENTER',token))
            
   
    with open(inputStringFilePath, 'r') as inputStringFile:
        inputString = inputStringFile.read().replace('\n', '').replace(' ','')

    # print(inputString)
    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    states = parsedLines['states']
    print('Input Symbols: ', parsedLines['input_symbols'])
    alphabet = parsedLines['input_symbols']
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    stack_alphabet = parsedLines['stack_symbols']
    print('Starting State: ', parsedLines['starting_state'])
    initial_state = parsedLines['starting_state'][0]
    print('Starting Stack: ', parsedLines['starting_stack'])
    initial_stack_symbol = parsedLines['starting_stack'][0]
    print('Accepting States: ', parsedLines['accepting_states'])
    final_states = parsedLines['accepting_states']
    print('Accept By: ', parsedLines['accept_by'])
    print('Productions List:')
    transitions = parsedLines['productions']
    for production in parsedLines['productions']:
        print('\t', production)

    pda = PDA(states, alphabet, stack_alphabet, initial_state, initial_stack_symbol, transitions, final_states)

    result = pda.process_input(token)
    if result:
        print("String HTML valid secara tag-structure-wise.")
    else:
        print("String HTML tidak valid secara tag-structure-wise.")




if __name__ == '__main__':
    main()

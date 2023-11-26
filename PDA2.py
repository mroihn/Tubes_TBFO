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

    def process_input(self, input_string):
        current_state = self.initial_state
        self.reset()

        for symbol in input_string:
            transition_key = (current_state, symbol, self.stack[-1] if self.stack else None)
            print(self.stack)
            print(symbol)
            # print(transition_key)
            if transition_key in self.transitions:
                action = self.transitions[transition_key]
                self.stack.pop()
                if action[1] != 'epsilon':
                    # print(action[1])
                    for stack_symbol in action[1][::-1]:
                        self.stack.append(stack_symbol)
                current_state = action[0]
                print(current_state)
                # self.stack.pop()
            else:
                return False
    def compute(self, inputString):

        currentStackSymbol = self.initial_stack_symbol
        currentState = self.initial_state
        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, self.stack))
        for char in inputString:
            for transition in self.transitions:
                if ((transition[0] == currentState) and (transition[1] == char) and (transition[2] == currentStackSymbol)):
                    currentState = transition[3]
                    if(len(transition[4]) == 2):
                        self.stack.append(char)
                    elif(len(transition[4]) == 3):
                        self.stack.append(char)
                        self.stack.append(char)
                        
            previousStackSymbol = currentStackSymbol
            currentStackSymbol = self.stack[len(self.stack)-1]
            print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, currentStackSymbol, self.stack))

        if(currentState == self.initial_state):
            print('String accepted by PDA.')
        else:
            print('String rejected by PDA.')



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

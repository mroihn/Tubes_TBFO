from FileHandler import FileHandler
import sys
import lexer

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
                # print(current_state)
                # self.stack.pop()
            else:
                return False

        return len(self.stack) == 1


def main():
    fh = FileHandler()
    # pda = PDA()

    states = {'q0', 'q1', 'q2', 'q3'}
    alphabet = {'<', '>', '/', ' ', 'h', 't', 'm', 'l'}
    stack_alphabet = {'tag_open', 'tag_close'}
    initial_state = 'qhtml'
    initial_stack_symbol = 'Z'
    transitions = {
        # HTML
        ('qhtml', 'KURUNG_V_BUKA', 'Z'): ('qhtml', ('X', 'Z')),
        ('qhtml', 'HTML', 'X'): ('qhtml', 'X'),
        ('qhtml', 'KURUNG_V_TUTUP', 'X'): ('qhtml', 'epsilon'),
        ('qhtml', 'ENTER', 'X'): ('qhtml', 'X'),
        ('qhtml', 'ENTER', 'Z'): ('qhtml', 'Z'),
        ('qhtml', 'GARIS_MIRING', 'X'): ('qhtml', 'X'),

        ('qhtml', 'KURUNG_V_BUKA', 'Z'): ('qhead', ('X', 'Z')),
        ('qhead', 'HEAD', 'X'): ('qhead', 'X'),
        ('qhead', 'KURUNG_V_TUTUP', 'X'): ('qhead', 'epsilon'),
        ('qhead', 'ENTER', 'X'): ('qhead', 'X'),
        ('qhead', 'ENTER', 'Z'): ('qhead', 'Z'),
        ('qhead', 'GARIS_MIRING', 'X'): ('qhead', 'X'),


        ('qhtml', '<', 'Z'): ('qhtml', ('X','Z')),
        ('qhtml', 'h', 'X'): ('qhtml', ('html','X')),
        ('qhtml', 't', 'html'): ('qhtml', 'html'),
        ('qhtml', 'm', 'h'): ('qhtml', 'h'),
        ('qhtml', 'l', 'h'): ('qhtml', 'h'),
        ('qhtml', '>', 'h'): ('qhtml', 'h'),
        ('qhtml', 'l', 'X'): ('qhtml', 'X'),
        ('qhtml', '>', 'X'): ('qhtml', 'epsilon'),
        ('qhtml', '/', 'X'): ('qhtml', 'Y'),
        ('qhtml', 'h', 'Y'): ('qhtml', 'html'),
        ('qhtml', 't', 'h'): ('qhtml', 'html'),
        ('qhtml', 'h', 'Y'): ('qhead', 'head'),
        ('qhtml', 't', 'Y'): ('qhtml', 'Y'),
        ('qhtml', 'm', 'Y'): ('qhtml', 'Y'),
        ('qhtml', 'l', 'Y'): ('qhtml', 'Y'),
        ('qhtml', '>', 'Y'): ('qhtml', 'epsilon')
    }
    final_states = {'q0'}
    pda = PDA(states, alphabet, stack_alphabet, initial_state, initial_stack_symbol, transitions, final_states)



    # pdaFilePath = sys.argv[1]
    # lines = fh.readFile(pdaFilePath)
    inputStringFilePath = sys.argv[1]
    token = lexer.createToken(inputStringFilePath)
    print(token)
    print("\n")
    # token.remove('ENTER')
    print(token)
            
   
    # with open(inputStringFilePath, 'r') as inputStringFile:
    #     inputString = inputStringFile.read().replace('\n', '').replace(' ','')
    # print(inputString)
    # parsedLines = fh.parseFile(lines)
    # print('States: ', parsedLines['states'])
    # print('Input Symbols: ', parsedLines['input_symbols'])
    # print('Stack Symbols: ', parsedLines['stack_symbols'])
    # print('Starting State: ', parsedLines['starting_state'])
    # print('Starting Stack: ', parsedLines['starting_stack'])
    # print('Accepting States: ', parsedLines['accepting_states'])
    # print('Accept By: ', parsedLines['accept_by'])
    # print('Productions List:')
    # for production in parsedLines['productions']:
    #     print('\t', production)
    result = pda.process_input(token)
    if result:
        print("String HTML valid secara tag-structure-wise.")
    else:
        print("String HTML tidak valid secara tag-structure-wise.")




if __name__ == '__main__':
    main()

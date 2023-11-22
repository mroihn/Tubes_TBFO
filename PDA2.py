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
                print(current_state)
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
        ('qhtml', 'HTML_OPEN', 'Z'): ('qhtml', ('A', 'Z')),
        ('qhtml', 'HTML_CLOSE', 'A'): ('qhtml', 'epsilon'),

        ('qhtml', 'HEAD_OPEN', 'A'): ('qhtml', ('B', 'A')),
        ('qhtml', 'HEAD_CLOSE', 'B'): ('qhtml', 'epsilon'),

        ('qhtml', 'BODY_OPEN', 'B'): ('qhtml', ('C', 'B')),
        ('qhtml', 'BODY_CLOSE', 'C'): ('qhtml', 'epsilon'),

        ('qhtml', 'TITLE_OPEN', 'B'): ('qhtml', ('D', 'B')),
        ('qhtml', 'TITLE_OPEN', 'E'): ('qhtml', ('D', 'E')),
        ('qhtml', 'TITLE_OPEN', 'F'): ('qhtml', ('D', 'F')),
        ('qhtml', 'TITLE_OPEN', 'G'): ('qhtml', ('D', 'G')),
        ('qhtml', 'TITLE_OPEN', 'H'): ('qhtml', ('D', 'H')),
        ('qhtml', 'TITLE_OPEN', 'I'): ('qhtml', ('D', 'I')),
        ('qhtml', 'TITLE_OPEN', 'J'): ('qhtml', ('D', 'J')),
        ('qhtml', 'TITLE_OPEN', 'K'): ('qhtml', ('D', 'K')),
        ('qhtml', 'TITLE_OPEN', 'L'): ('qhtml', ('D', 'L')),
        ('qhtml', 'TITLE_OPEN', 'M'): ('qhtml', ('D', 'M')),
        ('qhtml', 'TITLE_OPEN', 'N'): ('qhtml', ('D', 'N')),
        ('qhtml', 'TITLE_OPEN', 'O'): ('qhtml', ('D', 'O')),
        ('qhtml', 'TITLE_OPEN', 'P'): ('qhtml', ('D', 'P')),
        ('qhtml', 'TITLE_OPEN', 'Q'): ('qhtml', ('D', 'Q')),
        ('qhtml', 'TITLE_OPEN', 'R'): ('qhtml', ('D', 'R')),
        ('qhtml', 'TITLE_OPEN', 'S'): ('qhtml', ('D', 'S')),
        ('qhtml', 'TITLE_OPEN', 'T'): ('qhtml', ('D', 'T')),
        ('qhtml', 'TITLE_OPEN', 'U'): ('qhtml', ('D', 'U')),
        ('qhtml', 'TITLE_OPEN', 'V'): ('qhtml', ('D', 'V')),
        ('qhtml', 'TITLE_OPEN', 'W'): ('qhtml', ('D', 'W')),
        ('qhtml', 'TITLE_OPEN', 'X'): ('qhtml', ('D', 'X')),
        ('qhtml', 'TITLE_OPEN', 'Y'): ('qhtml', ('D', 'Y')),
        ('qhtml', 'TITLE_CLOSE', 'D'): ('qhtml', 'epsilon'),

        ('qhtml', 'LINK_OPEN', 'B'): ('qhtml', 'B'),
        ('qhtml', 'LINK_OPEN', 'C'): ('qhtml', 'C'),
        ('qhtml', 'LINK_OPEN', 'E'): ('qhtml', 'E'),
        ('qhtml', 'LINK_OPEN', 'F'): ('qhtml', 'F'),
        ('qhtml', 'LINK_OPEN', 'G'): ('qhtml', 'G'),
        ('qhtml', 'LINK_OPEN', 'H'): ('qhtml', 'H'),
        ('qhtml', 'LINK_OPEN', 'I'): ('qhtml', 'I'),
        ('qhtml', 'LINK_OPEN', 'J'): ('qhtml', 'J'),
        ('qhtml', 'LINK_OPEN', 'K'): ('qhtml', 'K'),
        ('qhtml', 'LINK_OPEN', 'L'): ('qhtml', 'L'),
        ('qhtml', 'LINK_OPEN', 'M'): ('qhtml', 'M'),
        ('qhtml', 'LINK_OPEN', 'N'): ('qhtml', 'N'),
        ('qhtml', 'LINK_OPEN', 'O'): ('qhtml', 'O'),
        ('qhtml', 'LINK_OPEN', 'P'): ('qhtml', 'P'),
        ('qhtml', 'LINK_OPEN', 'Q'): ('qhtml', 'Q'),
        ('qhtml', 'LINK_OPEN', 'R'): ('qhtml', 'R'),
        ('qhtml', 'LINK_OPEN', 'S'): ('qhtml', 'S'),
        ('qhtml', 'LINK_OPEN', 'T'): ('qhtml', 'T'),
        ('qhtml', 'LINK_OPEN', 'U'): ('qhtml', 'U'),
        ('qhtml', 'LINK_OPEN', 'V'): ('qhtml', 'V'),
        ('qhtml', 'LINK_OPEN', 'W'): ('qhtml', 'W'),
        ('qhtml', 'LINK_OPEN', 'X'): ('qhtml', 'X'),
        ('qhtml', 'LINK_OPEN', 'Y'): ('qhtml', 'Y'),
  
      
    


        ('qhtml', '>', 'Y'): ('qhtml', 'epsilon')
    }
    final_states = {'q0'}
    pda = PDA(states, alphabet, stack_alphabet, initial_state, initial_stack_symbol, transitions, final_states)



    # pdaFilePath = sys.argv[1]
    # lines = fh.readFile(pdaFilePath)
    inputStringFilePath = sys.argv[1]
    token = lexer.createToken(inputStringFilePath)
    token = list(filter(lambda x: x != 'ENTER',token))
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

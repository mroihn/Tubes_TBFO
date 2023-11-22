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
  
        ('qhtml', 'A_OPEN', 'C'): ('qhtml', ('S', 'C')),
        ('qhtml', 'A_OPEN', 'D'): ('qhtml', ('S', 'D')),
        ('qhtml', 'A_OPEN', 'E'): ('qhtml', ('S', 'E')),
        ('qhtml', 'A_OPEN', 'F'): ('qhtml', ('S', 'F')),
        ('qhtml', 'A_OPEN', 'G'): ('qhtml', ('S', 'G')),
        ('qhtml', 'A_OPEN', 'H'): ('qhtml', ('S', 'H')),
        ('qhtml', 'A_OPEN', 'I'): ('qhtml', ('S', 'I')),
        ('qhtml', 'A_OPEN', 'J'): ('qhtml', ('S', 'J')),
        ('qhtml', 'A_OPEN', 'K'): ('qhtml', ('S', 'K')),
        ('qhtml', 'A_OPEN', 'L'): ('qhtml', ('S', 'L')),
        ('qhtml', 'A_OPEN', 'M'): ('qhtml', ('S', 'M')),
        ('qhtml', 'A_OPEN', 'N'): ('qhtml', ('S', 'N')),
        ('qhtml', 'A_OPEN', 'O'): ('qhtml', ('S', 'O')),
        ('qhtml', 'A_OPEN', 'P'): ('qhtml', ('S', 'P')),
        ('qhtml', 'A_OPEN', 'Q'): ('qhtml', ('S', 'Q')),
        ('qhtml', 'A_OPEN', 'R'): ('qhtml', ('S', 'R')),
        ('qhtml', 'A_OPEN', 'S'): ('qhtml', ('S', 'S')),
        ('qhtml', 'A_OPEN', 'T'): ('qhtml', ('S', 'T')),
        ('qhtml', 'A_OPEN', 'U'): ('qhtml', ('S', 'U')),
        ('qhtml', 'A_OPEN', 'V'): ('qhtml', ('S', 'V')),
        ('qhtml', 'A_OPEN', 'W'): ('qhtml', ('S', 'W')),
        ('qhtml', 'A_OPEN', 'X'): ('qhtml', ('S', 'X')),
        ('qhtml', 'A_OPEN', 'Y'): ('qhtml', ('S', 'Y')),
        ('qhtml', 'A_CLOSE', 'S'): ('qhtml', 'epsilon'),
    
        ('qhtml', 'BUTTON_OPEN', 'C'): ('qhtml', ('T', 'C')),
        ('qhtml', 'BUTTON_OPEN', 'D'): ('qhtml', ('T', 'D')),
        ('qhtml', 'BUTTON_OPEN', 'E'): ('qhtml', ('T', 'E')),
        ('qhtml', 'BUTTON_OPEN', 'F'): ('qhtml', ('T', 'F')),
        ('qhtml', 'BUTTON_OPEN', 'G'): ('qhtml', ('T', 'G')),
        ('qhtml', 'BUTTON_OPEN', 'H'): ('qhtml', ('T', 'H')),
        ('qhtml', 'BUTTON_OPEN', 'I'): ('qhtml', ('T', 'I')),
        ('qhtml', 'BUTTON_OPEN', 'J'): ('qhtml', ('T', 'J')),
        ('qhtml', 'BUTTON_OPEN', 'K'): ('qhtml', ('T', 'K')),
        ('qhtml', 'BUTTON_OPEN', 'L'): ('qhtml', ('T', 'L')),
        ('qhtml', 'BUTTON_OPEN', 'M'): ('qhtml', ('T', 'M')),
        ('qhtml', 'BUTTON_OPEN', 'N'): ('qhtml', ('T', 'N')),
        ('qhtml', 'BUTTON_OPEN', 'O'): ('qhtml', ('T', 'O')),
        ('qhtml', 'BUTTON_OPEN', 'P'): ('qhtml', ('T', 'P')),
        ('qhtml', 'BUTTON_OPEN', 'Q'): ('qhtml', ('T', 'Q')),
        ('qhtml', 'BUTTON_OPEN', 'R'): ('qhtml', ('T', 'R')),
        ('qhtml', 'BUTTON_OPEN', 'S'): ('qhtml', ('T', 'S')),
        ('qhtml', 'BUTTON_OPEN', 'U'): ('qhtml', ('T', 'U')),
        ('qhtml', 'BUTTON_OPEN', 'V'): ('qhtml', ('T', 'V')),
        ('qhtml', 'BUTTON_OPEN', 'W'): ('qhtml', ('T', 'W')),
        ('qhtml', 'BUTTON_OPEN', 'X'): ('qhtml', ('T', 'X')),
        ('qhtml', 'BUTTON_OPEN', 'Y'): ('qhtml', ('T', 'Y')),
        ('qhtml', 'BUTTON_CLOSE', 'T'): ('qhtml', 'epsilon'),
    
        ('qhtml', 'FORM_OPEN', 'C'): ('qhtml', ('U', 'C')),
        ('qhtml', 'FORM_OPEN', 'D'): ('qhtml', ('U', 'D')),
        ('qhtml', 'FORM_OPEN', 'E'): ('qhtml', ('U', 'E')),
        ('qhtml', 'FORM_OPEN', 'F'): ('qhtml', ('U', 'F')),
        ('qhtml', 'FORM_OPEN', 'G'): ('qhtml', ('U', 'G')),
        ('qhtml', 'FORM_OPEN', 'H'): ('qhtml', ('U', 'H')),
        ('qhtml', 'FORM_OPEN', 'I'): ('qhtml', ('U', 'I')),
        ('qhtml', 'FORM_OPEN', 'J'): ('qhtml', ('U', 'J')),
        ('qhtml', 'FORM_OPEN', 'K'): ('qhtml', ('U', 'K')),
        ('qhtml', 'FORM_OPEN', 'L'): ('qhtml', ('U', 'L')),
        ('qhtml', 'FORM_OPEN', 'M'): ('qhtml', ('U', 'M')),
        ('qhtml', 'FORM_OPEN', 'N'): ('qhtml', ('U', 'N')),
        ('qhtml', 'FORM_OPEN', 'O'): ('qhtml', ('U', 'O')),
        ('qhtml', 'FORM_OPEN', 'P'): ('qhtml', ('U', 'P')),
        ('qhtml', 'FORM_OPEN', 'Q'): ('qhtml', ('U', 'Q')),
        ('qhtml', 'FORM_OPEN', 'R'): ('qhtml', ('U', 'R')),
        ('qhtml', 'FORM_OPEN', 'S'): ('qhtml', ('U', 'S')),
        ('qhtml', 'FORM_OPEN', 'T'): ('qhtml', ('U', 'T')),
        ('qhtml', 'FORM_OPEN', 'V'): ('qhtml', ('U', 'V')),
        ('qhtml', 'FORM_OPEN', 'W'): ('qhtml', ('U', 'W')),
        ('qhtml', 'FORM_OPEN', 'X'): ('qhtml', ('U', 'X')),
        ('qhtml', 'FORM_OPEN', 'Y'): ('qhtml', ('U', 'Y')),
        ('qhtml', 'FORM_CLOSE', 'U'): ('qhtml', 'epsilon'),

        ('qhtml', 'TABLE_OPEN', 'C'): ('qhtml', ('V', 'C')),
        ('qhtml', 'TABLE_OPEN', 'D'): ('qhtml', ('V', 'D')),
        ('qhtml', 'TABLE_OPEN', 'E'): ('qhtml', ('V', 'E')),
        ('qhtml', 'TABLE_OPEN', 'F'): ('qhtml', ('V', 'F')),
        ('qhtml', 'TABLE_OPEN', 'G'): ('qhtml', ('V', 'G')),
        ('qhtml', 'TABLE_OPEN', 'H'): ('qhtml', ('V', 'H')),
        ('qhtml', 'TABLE_OPEN', 'I'): ('qhtml', ('V', 'I')),
        ('qhtml', 'TABLE_OPEN', 'J'): ('qhtml', ('V', 'J')),
        ('qhtml', 'TABLE_OPEN', 'K'): ('qhtml', ('V', 'K')),
        ('qhtml', 'TABLE_OPEN', 'L'): ('qhtml', ('V', 'L')),
        ('qhtml', 'TABLE_OPEN', 'M'): ('qhtml', ('V', 'M')),
        ('qhtml', 'TABLE_OPEN', 'N'): ('qhtml', ('V', 'N')),
        ('qhtml', 'TABLE_OPEN', 'O'): ('qhtml', ('V', 'O')),
        ('qhtml', 'TABLE_OPEN', 'P'): ('qhtml', ('V', 'P')),
        ('qhtml', 'TABLE_OPEN', 'Q'): ('qhtml', ('V', 'Q')),
        ('qhtml', 'TABLE_OPEN', 'R'): ('qhtml', ('V', 'R')),
        ('qhtml', 'TABLE_OPEN', 'S'): ('qhtml', ('V', 'S')),
        ('qhtml', 'TABLE_OPEN', 'T'): ('qhtml', ('V', 'T')),
        ('qhtml', 'TABLE_OPEN', 'U'): ('qhtml', ('V', 'U')),
        ('qhtml', 'TABLE_OPEN', 'W'): ('qhtml', ('V', 'W')),
        ('qhtml', 'TABLE_OPEN', 'X'): ('qhtml', ('V', 'X')),
        ('qhtml', 'TABLE_OPEN', 'Y'): ('qhtml', ('V', 'Y')),
        ('qhtml', 'TABLE_CLOSE', 'V'): ('qhtml', 'epsilon'),

        
        ('qhtml', 'TR_OPEN', 'V'): ('qhtml', ('W', 'V')),
        ('qhtml', 'TR_CLOSE', 'W'): ('qhtml', 'epsilon'),

        ('qhtml', 'TD_OPEN', 'V'): ('qhtml', ('X', 'V')),
        ('qhtml', 'TD_CLOSE', 'X'): ('qhtml', 'epsilon'),

        ('qhtml', 'TH_OPEN', 'V'): ('qhtml', ('Y', 'V')),
        ('qhtml', 'TH_CLOSE', 'Y'): ('qhtml', 'epsilon'),

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

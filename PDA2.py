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
        
        ('qhtml', 'H1_OPEN', 'C'): ('qhtml', ('F', 'C')),
        ('qhtml', 'H1_OPEN', 'E'): ('qhtml', ('F', 'E')),
        ('qhtml', 'H1_OPEN', 'G'): ('qhtml', ('F', 'G')),
        ('qhtml', 'H1_OPEN', 'H'): ('qhtml', ('F', 'H')),
        ('qhtml', 'H1_OPEN', 'I'): ('qhtml', ('F', 'I')),
        ('qhtml', 'H1_OPEN', 'J'): ('qhtml', ('F', 'J')),
        ('qhtml', 'H1_OPEN', 'K'): ('qhtml', ('F', 'K')),
        ('qhtml', 'H1_OPEN', 'L'): ('qhtml', ('F', 'L')),
        ('qhtml', 'H1_OPEN', 'M'): ('qhtml', ('F', 'M')),
        ('qhtml', 'H1_OPEN', 'N'): ('qhtml', ('F', 'N')),
        ('qhtml', 'H1_OPEN', 'O'): ('qhtml', ('F', 'O')),
        ('qhtml', 'H1_OPEN', 'P'): ('qhtml', ('F', 'P')),
        ('qhtml', 'H1_OPEN', 'Q'): ('qhtml', ('F', 'Q')),
        ('qhtml', 'H1_OPEN', 'R'): ('qhtml', ('F', 'R')),
        ('qhtml', 'H1_OPEN', 'S'): ('qhtml', ('F', 'S')),
        ('qhtml', 'H1_OPEN', 'T'): ('qhtml', ('F', 'T')),
        ('qhtml', 'H1_OPEN', 'U'): ('qhtml', ('F', 'U')),
        ('qhtml', 'H1_OPEN', 'V'): ('qhtml', ('F', 'V')),
        ('qhtml', 'H1_OPEN', 'W'): ('qhtml', ('F', 'W')),
        ('qhtml', 'H1_OPEN', 'X'): ('qhtml', ('F', 'X')),
        ('qhtml', 'H1_OPEN', 'Y'): ('qhtml', ('F', 'Y')),
        ('qhtml', 'H1_CLOSE', 'F'): ('qhtml', 'epsilon'),

        ('qhtml', 'H2_OPEN', 'C'): ('qhtml', ('G', 'C')),
        ('qhtml', 'H2_OPEN', 'E'): ('qhtml', ('G', 'E')),
        ('qhtml', 'H2_OPEN', 'F'): ('qhtml', ('G', 'F')),
        ('qhtml', 'H2_OPEN', 'H'): ('qhtml', ('G', 'H')),
        ('qhtml', 'H2_OPEN', 'I'): ('qhtml', ('G', 'I')),
        ('qhtml', 'H2_OPEN', 'J'): ('qhtml', ('G', 'J')),
        ('qhtml', 'H2_OPEN', 'K'): ('qhtml', ('G', 'K')),
        ('qhtml', 'H2_OPEN', 'L'): ('qhtml', ('G', 'L')),
        ('qhtml', 'H2_OPEN', 'M'): ('qhtml', ('G', 'M')),
        ('qhtml', 'H2_OPEN', 'N'): ('qhtml', ('G', 'N')),
        ('qhtml', 'H2_OPEN', 'O'): ('qhtml', ('G', 'O')),
        ('qhtml', 'H2_OPEN', 'P'): ('qhtml', ('G', 'P')),
        ('qhtml', 'H2_OPEN', 'Q'): ('qhtml', ('G', 'Q')),
        ('qhtml', 'H2_OPEN', 'R'): ('qhtml', ('G', 'R')),
        ('qhtml', 'H2_OPEN', 'S'): ('qhtml', ('G', 'S')),
        ('qhtml', 'H2_OPEN', 'T'): ('qhtml', ('G', 'T')),
        ('qhtml', 'H2_OPEN', 'U'): ('qhtml', ('G', 'U')),
        ('qhtml', 'H2_OPEN', 'V'): ('qhtml', ('G', 'V')),
        ('qhtml', 'H2_OPEN', 'W'): ('qhtml', ('G', 'W')),
        ('qhtml', 'H2_OPEN', 'X'): ('qhtml', ('G', 'X')),
        ('qhtml', 'H2_OPEN', 'Y'): ('qhtml', ('G', 'Y')),
        ('qhtml', 'H2_CLOSE', 'F'): ('qhtml', 'epsilon'),
        
        ('qhtml', 'H3_OPEN', 'C'): ('qhtml', ('H', 'C')),
        ('qhtml', 'H3_OPEN', 'E'): ('qhtml', ('H', 'E')),
        ('qhtml', 'H3_OPEN', 'F'): ('qhtml', ('H', 'F')),
        ('qhtml', 'H3_OPEN', 'G'): ('qhtml', ('H', 'G')),
        ('qhtml', 'H3_OPEN', 'I'): ('qhtml', ('H', 'I')),
        ('qhtml', 'H3_OPEN', 'J'): ('qhtml', ('H', 'J')),
        ('qhtml', 'H3_OPEN', 'K'): ('qhtml', ('H', 'K')),
        ('qhtml', 'H3_OPEN', 'L'): ('qhtml', ('H', 'L')),
        ('qhtml', 'H3_OPEN', 'M'): ('qhtml', ('H', 'M')),
        ('qhtml', 'H3_OPEN', 'N'): ('qhtml', ('H', 'N')),
        ('qhtml', 'H3_OPEN', 'O'): ('qhtml', ('H', 'O')),
        ('qhtml', 'H3_OPEN', 'P'): ('qhtml', ('H', 'P')),
        ('qhtml', 'H3_OPEN', 'Q'): ('qhtml', ('H', 'Q')),
        ('qhtml', 'H3_OPEN', 'R'): ('qhtml', ('H', 'R')),
        ('qhtml', 'H3_OPEN', 'S'): ('qhtml', ('H', 'S')),
        ('qhtml', 'H3_OPEN', 'T'): ('qhtml', ('H', 'T')),
        ('qhtml', 'H3_OPEN', 'U'): ('qhtml', ('H', 'U')),
        ('qhtml', 'H3_OPEN', 'V'): ('qhtml', ('H', 'V')),
        ('qhtml', 'H3_OPEN', 'W'): ('qhtml', ('H', 'W')),
        ('qhtml', 'H3_OPEN', 'X'): ('qhtml', ('H', 'X')),
        ('qhtml', 'H3_OPEN', 'Y'): ('qhtml', ('H', 'Y')),
        ('qhtml', 'H3_CLOSE', 'F'): ('qhtml', 'epsilon'),
        
        ('qhtml', 'H4_OPEN', 'C'): ('qhtml', ('I', 'C')),
        ('qhtml', 'H4_OPEN', 'E'): ('qhtml', ('I', 'E')),
        ('qhtml', 'H4_OPEN', 'F'): ('qhtml', ('I', 'F')),
        ('qhtml', 'H4_OPEN', 'G'): ('qhtml', ('I', 'G')),
        ('qhtml', 'H4_OPEN', 'H'): ('qhtml', ('I', 'H')),
        ('qhtml', 'H4_OPEN', 'J'): ('qhtml', ('I', 'J')),
        ('qhtml', 'H4_OPEN', 'K'): ('qhtml', ('I', 'K')),
        ('qhtml', 'H4_OPEN', 'L'): ('qhtml', ('I', 'L')),
        ('qhtml', 'H4_OPEN', 'M'): ('qhtml', ('I', 'M')),
        ('qhtml', 'H4_OPEN', 'N'): ('qhtml', ('I', 'N')),
        ('qhtml', 'H4_OPEN', 'O'): ('qhtml', ('I', 'O')),
        ('qhtml', 'H4_OPEN', 'P'): ('qhtml', ('I', 'P')),
        ('qhtml', 'H4_OPEN', 'Q'): ('qhtml', ('I', 'Q')),
        ('qhtml', 'H4_OPEN', 'R'): ('qhtml', ('I', 'R')),
        ('qhtml', 'H4_OPEN', 'S'): ('qhtml', ('I', 'S')),
        ('qhtml', 'H4_OPEN', 'T'): ('qhtml', ('I', 'T')),
        ('qhtml', 'H4_OPEN', 'U'): ('qhtml', ('I', 'U')),
        ('qhtml', 'H4_OPEN', 'V'): ('qhtml', ('I', 'V')),
        ('qhtml', 'H4_OPEN', 'W'): ('qhtml', ('I', 'W')),
        ('qhtml', 'H4_OPEN', 'X'): ('qhtml', ('I', 'X')),
        ('qhtml', 'H4_OPEN', 'Y'): ('qhtml', ('I', 'Y')),
        ('qhtml', 'H4_CLOSE', 'F'): ('qhtml', 'epsilon'),
        
        ('qhtml', 'H5_OPEN', 'C'): ('qhtml', ('J', 'C')),
        ('qhtml', 'H5_OPEN', 'E'): ('qhtml', ('J', 'E')),
        ('qhtml', 'H5_OPEN', 'F'): ('qhtml', ('J', 'F')),
        ('qhtml', 'H5_OPEN', 'G'): ('qhtml', ('J', 'G')),
        ('qhtml', 'H5_OPEN', 'H'): ('qhtml', ('J', 'H')),
        ('qhtml', 'H5_OPEN', 'I'): ('qhtml', ('J', 'I')),
        ('qhtml', 'H5_OPEN', 'K'): ('qhtml', ('J', 'K')),
        ('qhtml', 'H5_OPEN', 'L'): ('qhtml', ('J', 'L')),
        ('qhtml', 'H5_OPEN', 'M'): ('qhtml', ('J', 'M')),
        ('qhtml', 'H5_OPEN', 'N'): ('qhtml', ('J', 'N')),
        ('qhtml', 'H5_OPEN', 'O'): ('qhtml', ('J', 'O')),
        ('qhtml', 'H5_OPEN', 'P'): ('qhtml', ('J', 'P')),
        ('qhtml', 'H5_OPEN', 'Q'): ('qhtml', ('J', 'Q')),
        ('qhtml', 'H5_OPEN', 'R'): ('qhtml', ('J', 'R')),
        ('qhtml', 'H5_OPEN', 'S'): ('qhtml', ('J', 'S')),
        ('qhtml', 'H5_OPEN', 'T'): ('qhtml', ('J', 'T')),
        ('qhtml', 'H5_OPEN', 'U'): ('qhtml', ('J', 'U')),
        ('qhtml', 'H5_OPEN', 'V'): ('qhtml', ('J', 'V')),
        ('qhtml', 'H5_OPEN', 'W'): ('qhtml', ('J', 'W')),
        ('qhtml', 'H5_OPEN', 'X'): ('qhtml', ('J', 'X')),
        ('qhtml', 'H5_OPEN', 'Y'): ('qhtml', ('J', 'Y')),
        ('qhtml', 'H5_CLOSE', 'F'): ('qhtml', 'epsilon'),

        ('qhtml', 'H6_OPEN', 'C'): ('qhtml', ('K', 'C')),
        ('qhtml', 'H6_OPEN', 'E'): ('qhtml', ('K', 'E')),
        ('qhtml', 'H6_OPEN', 'F'): ('qhtml', ('K', 'F')),
        ('qhtml', 'H6_OPEN', 'G'): ('qhtml', ('K', 'G')),
        ('qhtml', 'H6_OPEN', 'H'): ('qhtml', ('K', 'H')),
        ('qhtml', 'H6_OPEN', 'I'): ('qhtml', ('K', 'I')),
        ('qhtml', 'H6_OPEN', 'J'): ('qhtml', ('K', 'J')),
        ('qhtml', 'H6_OPEN', 'L'): ('qhtml', ('K', 'L')),
        ('qhtml', 'H6_OPEN', 'M'): ('qhtml', ('K', 'M')),
        ('qhtml', 'H6_OPEN', 'N'): ('qhtml', ('K', 'N')),
        ('qhtml', 'H6_OPEN', 'O'): ('qhtml', ('K', 'O')),
        ('qhtml', 'H6_OPEN', 'P'): ('qhtml', ('K', 'P')),
        ('qhtml', 'H6_OPEN', 'Q'): ('qhtml', ('K', 'Q')),
        ('qhtml', 'H6_OPEN', 'R'): ('qhtml', ('K', 'R')),
        ('qhtml', 'H6_OPEN', 'S'): ('qhtml', ('K', 'S')),
        ('qhtml', 'H6_OPEN', 'T'): ('qhtml', ('K', 'T')),
        ('qhtml', 'H6_OPEN', 'U'): ('qhtml', ('K', 'U')),
        ('qhtml', 'H6_OPEN', 'V'): ('qhtml', ('K', 'V')),
        ('qhtml', 'H6_OPEN', 'W'): ('qhtml', ('K', 'W')),
        ('qhtml', 'H6_OPEN', 'X'): ('qhtml', ('K', 'X')),
        ('qhtml', 'H6_OPEN', 'Y'): ('qhtml', ('K', 'Y')),
        ('qhtml', 'H6_CLOSE', 'F'): ('qhtml', 'epsilon'),

        ('qhtml', 'P_OPEN', 'C'): ('qhtml', ('L', 'C')),
        ('qhtml', 'P_OPEN', 'E'): ('qhtml', ('L', 'E')),
        ('qhtml', 'P_OPEN', 'F'): ('qhtml', ('L', 'F')),
        ('qhtml', 'P_OPEN', 'G'): ('qhtml', ('L', 'G')),
        ('qhtml', 'P_OPEN', 'H'): ('qhtml', ('L', 'H')),
        ('qhtml', 'P_OPEN', 'I'): ('qhtml', ('L', 'I')),
        ('qhtml', 'P_OPEN', 'J'): ('qhtml', ('L', 'J')),
        ('qhtml', 'P_OPEN', 'K'): ('qhtml', ('L', 'K')),
        ('qhtml', 'P_OPEN', 'M'): ('qhtml', ('L', 'M')),
        ('qhtml', 'P_OPEN', 'N'): ('qhtml', ('L', 'N')),
        ('qhtml', 'P_OPEN', 'O'): ('qhtml', ('L', 'O')),
        ('qhtml', 'P_OPEN', 'P'): ('qhtml', ('L', 'P')),
        ('qhtml', 'P_OPEN', 'Q'): ('qhtml', ('L', 'Q')),
        ('qhtml', 'P_OPEN', 'R'): ('qhtml', ('L', 'R')),
        ('qhtml', 'P_OPEN', 'S'): ('qhtml', ('L', 'S')),
        ('qhtml', 'P_OPEN', 'T'): ('qhtml', ('L', 'T')),
        ('qhtml', 'P_OPEN', 'U'): ('qhtml', ('L', 'U')),
        ('qhtml', 'P_OPEN', 'V'): ('qhtml', ('L', 'V')),
        ('qhtml', 'P_OPEN', 'W'): ('qhtml', ('L', 'W')),
        ('qhtml', 'P_OPEN', 'X'): ('qhtml', ('L', 'X')),
        ('qhtml', 'P_OPEN', 'Y'): ('qhtml', ('L', 'Y')),
        ('qhtml', 'P_CLOSE', 'F'): ('qhtml', 'epsilon'),
      
        ('qhtml', 'EM_OPEN', 'C'): ('qhtml', ('M', 'C')),
        ('qhtml', 'EM_OPEN', 'E'): ('qhtml', ('M', 'E')),
        ('qhtml', 'EM_OPEN', 'F'): ('qhtml', ('M', 'F')),
        ('qhtml', 'EM_OPEN', 'G'): ('qhtml', ('M', 'G')),
        ('qhtml', 'EM_OPEN', 'H'): ('qhtml', ('M', 'H')),
        ('qhtml', 'EM_OPEN', 'I'): ('qhtml', ('M', 'I')),
        ('qhtml', 'EM_OPEN', 'J'): ('qhtml', ('M', 'J')),
        ('qhtml', 'EM_OPEN', 'K'): ('qhtml', ('M', 'K')),
        ('qhtml', 'EM_OPEN', 'M'): ('qhtml', ('M', 'M')),
        ('qhtml', 'EM_OPEN', 'N'): ('qhtml', ('M', 'N')),
        ('qhtml', 'EM_OPEN', 'O'): ('qhtml', ('M', 'O')),
        ('qhtml', 'EM_OPEN', 'P'): ('qhtml', ('M', 'P')),
        ('qhtml', 'EM_OPEN', 'Q'): ('qhtml', ('M', 'Q')),
        ('qhtml', 'EM_OPEN', 'R'): ('qhtml', ('M', 'R')),
        ('qhtml', 'EM_OPEN', 'S'): ('qhtml', ('M', 'S')),
        ('qhtml', 'EM_OPEN', 'T'): ('qhtml', ('M', 'T')),
        ('qhtml', 'EM_OPEN', 'U'): ('qhtml', ('M', 'U')),
        ('qhtml', 'EM_OPEN', 'V'): ('qhtml', ('M', 'V')),
        ('qhtml', 'EM_OPEN', 'W'): ('qhtml', ('M', 'W')),
        ('qhtml', 'EM_OPEN', 'X'): ('qhtml', ('M', 'X')),
        ('qhtml', 'EM_OPEN', 'Y'): ('qhtml', ('M', 'Y')),
        ('qhtml', 'EM_CLOSE', 'F'): ('qhtml', 'epsilon'),

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

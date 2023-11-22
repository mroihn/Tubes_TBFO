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

        ('qhtml', 'BODY_OPEN', 'A'): ('qhtml', ('C', 'A')),
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
        ('qhtml', 'LINK_OPEN', 'D'): ('qhtml', 'D'),
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

        ('qhtml', 'IMG', 'C'): ('qhtml', 'C'),
        ('qhtml', 'IMG', 'E'): ('qhtml', 'E'),
        ('qhtml', 'IMG', 'F'): ('qhtml', 'F'),
        ('qhtml', 'IMG', 'G'): ('qhtml', 'G'),
        ('qhtml', 'IMG', 'H'): ('qhtml', 'H'),
        ('qhtml', 'IMG', 'I'): ('qhtml', 'I'),
        ('qhtml', 'IMG', 'J'): ('qhtml', 'J'),
        ('qhtml', 'IMG', 'K'): ('qhtml', 'K'),
        ('qhtml', 'IMG', 'L'): ('qhtml', 'L'),
        ('qhtml', 'IMG', 'M'): ('qhtml', 'M'),
        ('qhtml', 'IMG', 'N'): ('qhtml', 'N'),
        ('qhtml', 'IMG', 'O'): ('qhtml', 'O'),
        ('qhtml', 'IMG', 'P'): ('qhtml', 'P'),
        ('qhtml', 'IMG', 'Q'): ('qhtml', 'Q'),
        ('qhtml', 'IMG', 'R'): ('qhtml', 'R'),
        ('qhtml', 'IMG', 'S'): ('qhtml', 'S'),
        ('qhtml', 'IMG', 'T'): ('qhtml', 'T'),
        ('qhtml', 'IMG', 'U'): ('qhtml', 'U'),
        ('qhtml', 'IMG', 'V'): ('qhtml', 'V'),
        ('qhtml', 'IMG', 'W'): ('qhtml', 'W'),
        ('qhtml', 'IMG', 'X'): ('qhtml', 'X'),
        ('qhtml', 'IMG', 'Y'): ('qhtml', 'Y'),

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
  
        ('qhtml', 'A_OPEN', 'C'): ('qhtml', ('S', 'C')),
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

        ('qhtml', 'B_OPEN', 'C'): ('qhtml', ('N', 'C')),
        ('qhtml', 'B_OPEN', 'E'): ('qhtml', ('N', 'E')),
        ('qhtml', 'B_OPEN', 'F'): ('qhtml', ('N', 'F')),
        ('qhtml', 'B_OPEN', 'G'): ('qhtml', ('N', 'G')),
        ('qhtml', 'B_OPEN', 'H'): ('qhtml', ('N', 'H')),
        ('qhtml', 'B_OPEN', 'I'): ('qhtml', ('N', 'I')),
        ('qhtml', 'B_OPEN', 'J'): ('qhtml', ('N', 'J')),
        ('qhtml', 'B_OPEN', 'K'): ('qhtml', ('N', 'K')),
        ('qhtml', 'B_OPEN', 'L'): ('qhtml', ('N', 'L')),
        ('qhtml', 'B_OPEN', 'M'): ('qhtml', ('N', 'M')),
        ('qhtml', 'B_OPEN', 'O'): ('qhtml', ('N', 'O')),
        ('qhtml', 'B_OPEN', 'P'): ('qhtml', ('N', 'P')),
        ('qhtml', 'B_OPEN', 'Q'): ('qhtml', ('N', 'Q')),
        ('qhtml', 'B_OPEN', 'R'): ('qhtml', ('N', 'R')),
        ('qhtml', 'B_OPEN', 'S'): ('qhtml', ('N', 'S')),
        ('qhtml', 'B_OPEN', 'T'): ('qhtml', ('N', 'T')),
        ('qhtml', 'B_OPEN', 'U'): ('qhtml', ('N', 'U')),
        ('qhtml', 'B_OPEN', 'V'): ('qhtml', ('N', 'V')),
        ('qhtml', 'B_OPEN', 'W'): ('qhtml', ('N', 'W')),
        ('qhtml', 'B_OPEN', 'X'): ('qhtml', ('N', 'X')),
        ('qhtml', 'B_OPEN', 'Y'): ('qhtml', ('N', 'Y')),
        ('qhtml', 'B_CLOSE', 'N'): ('qhtml', 'epsilon'),
    
        ('qhtml', 'ABBR_OPEN', 'C'): ('qhtml', ('O', 'C')),
        ('qhtml', 'ABBR_OPEN', 'E'): ('qhtml', ('O', 'E')),
        ('qhtml', 'ABBR_OPEN', 'F'): ('qhtml', ('O', 'F')),
        ('qhtml', 'ABBR_OPEN', 'G'): ('qhtml', ('O', 'G')),
        ('qhtml', 'ABBR_OPEN', 'H'): ('qhtml', ('O', 'H')),
        ('qhtml', 'ABBR_OPEN', 'I'): ('qhtml', ('O', 'I')),
        ('qhtml', 'ABBR_OPEN', 'J'): ('qhtml', ('O', 'J')),
        ('qhtml', 'ABBR_OPEN', 'K'): ('qhtml', ('O', 'K')),
        ('qhtml', 'ABBR_OPEN', 'L'): ('qhtml', ('O', 'L')),
        ('qhtml', 'ABBR_OPEN', 'M'): ('qhtml', ('O', 'M')),
        ('qhtml', 'ABBR_OPEN', 'N'): ('qhtml', ('O', 'N')),
        ('qhtml', 'ABBR_OPEN', 'P'): ('qhtml', ('O', 'P')),
        ('qhtml', 'ABBR_OPEN', 'Q'): ('qhtml', ('O', 'Q')),
        ('qhtml', 'ABBR_OPEN', 'R'): ('qhtml', ('O', 'R')),
        ('qhtml', 'ABBR_OPEN', 'S'): ('qhtml', ('O', 'S')),
        ('qhtml', 'ABBR_OPEN', 'T'): ('qhtml', ('O', 'T')),
        ('qhtml', 'ABBR_OPEN', 'U'): ('qhtml', ('O', 'U')),
        ('qhtml', 'ABBR_OPEN', 'V'): ('qhtml', ('O', 'V')),
        ('qhtml', 'ABBR_OPEN', 'W'): ('qhtml', ('O', 'W')),
        ('qhtml', 'ABBR_OPEN', 'X'): ('qhtml', ('O', 'X')),
        ('qhtml', 'ABBR_OPEN', 'Y'): ('qhtml', ('O', 'Y')),
        ('qhtml', 'ABBR_CLOSE', 'O'): ('qhtml', 'epsilon'),

        ('qhtml', 'STRONG_OPEN', 'C'): ('qhtml', ('P', 'C')),
        ('qhtml', 'STRONG_OPEN', 'E'): ('qhtml', ('P', 'E')),
        ('qhtml', 'STRONG_OPEN', 'F'): ('qhtml', ('P', 'F')),
        ('qhtml', 'STRONG_OPEN', 'G'): ('qhtml', ('P', 'G')),
        ('qhtml', 'STRONG_OPEN', 'H'): ('qhtml', ('P', 'H')),
        ('qhtml', 'STRONG_OPEN', 'I'): ('qhtml', ('P', 'I')),
        ('qhtml', 'STRONG_OPEN', 'J'): ('qhtml', ('P', 'J')),
        ('qhtml', 'STRONG_OPEN', 'K'): ('qhtml', ('P', 'K')),
        ('qhtml', 'STRONG_OPEN', 'L'): ('qhtml', ('P', 'L')),
        ('qhtml', 'STRONG_OPEN', 'M'): ('qhtml', ('P', 'M')),
        ('qhtml', 'STRONG_OPEN', 'N'): ('qhtml', ('P', 'N')),
        ('qhtml', 'STRONG_OPEN', 'O'): ('qhtml', ('P', 'O')),
        ('qhtml', 'STRONG_OPEN', 'Q'): ('qhtml', ('P', 'Q')),
        ('qhtml', 'STRONG_OPEN', 'R'): ('qhtml', ('P', 'R')),
        ('qhtml', 'STRONG_OPEN', 'S'): ('qhtml', ('P', 'S')),
        ('qhtml', 'STRONG_OPEN', 'T'): ('qhtml', ('P', 'T')),
        ('qhtml', 'STRONG_OPEN', 'U'): ('qhtml', ('P', 'U')),
        ('qhtml', 'STRONG_OPEN', 'V'): ('qhtml', ('P', 'V')),
        ('qhtml', 'STRONG_OPEN', 'W'): ('qhtml', ('P', 'W')),
        ('qhtml', 'STRONG_OPEN', 'X'): ('qhtml', ('P', 'X')),
        ('qhtml', 'STRONG_OPEN', 'Y'): ('qhtml', ('P', 'Y')),
        ('qhtml', 'STRONG_CLOSE', 'P'): ('qhtml', 'epsilon'),

        ('qhtml', 'SMALL_OPEN', 'C'): ('qhtml', ('Q', 'C')),
        ('qhtml', 'SMALL_OPEN', 'E'): ('qhtml', ('Q', 'E')),
        ('qhtml', 'SMALL_OPEN', 'F'): ('qhtml', ('Q', 'F')),
        ('qhtml', 'SMALL_OPEN', 'G'): ('qhtml', ('Q', 'G')),
        ('qhtml', 'SMALL_OPEN', 'H'): ('qhtml', ('Q', 'H')),
        ('qhtml', 'SMALL_OPEN', 'I'): ('qhtml', ('Q', 'I')),
        ('qhtml', 'SMALL_OPEN', 'J'): ('qhtml', ('Q', 'J')),
        ('qhtml', 'SMALL_OPEN', 'K'): ('qhtml', ('Q', 'K')),
        ('qhtml', 'SMALL_OPEN', 'L'): ('qhtml', ('Q', 'L')),
        ('qhtml', 'SMALL_OPEN', 'M'): ('qhtml', ('Q', 'M')),
        ('qhtml', 'SMALL_OPEN', 'N'): ('qhtml', ('Q', 'N')),
        ('qhtml', 'SMALL_OPEN', 'O'): ('qhtml', ('Q', 'O')),
        ('qhtml', 'SMALL_OPEN', 'P'): ('qhtml', ('Q', 'P')),
        ('qhtml', 'SMALL_OPEN', 'R'): ('qhtml', ('Q', 'R')),
        ('qhtml', 'SMALL_OPEN', 'S'): ('qhtml', ('Q', 'S')),
        ('qhtml', 'SMALL_OPEN', 'T'): ('qhtml', ('Q', 'T')),
        ('qhtml', 'SMALL_OPEN', 'U'): ('qhtml', ('Q', 'U')),
        ('qhtml', 'SMALL_OPEN', 'V'): ('qhtml', ('Q', 'V')),
        ('qhtml', 'SMALL_OPEN', 'W'): ('qhtml', ('Q', 'W')),
        ('qhtml', 'SMALL_OPEN', 'X'): ('qhtml', ('Q', 'X')),
        ('qhtml', 'SMALL_OPEN', 'Y'): ('qhtml', ('Q', 'Y')),
        ('qhtml', 'SMALL_CLOSE', 'Q'): ('qhtml', 'epsilon'),

        ('qhtml', 'HR_OPEN', 'B'): ('qhtml', 'B'),
        ('qhtml', 'HR_OPEN', 'C'): ('qhtml', 'C'),
        ('qhtml', 'HR_OPEN', 'D'): ('qhtml', 'D'),
        ('qhtml', 'HR_OPEN', 'E'): ('qhtml', 'E'),
        ('qhtml', 'HR_OPEN', 'F'): ('qhtml', 'F'),
        ('qhtml', 'HR_OPEN', 'G'): ('qhtml', 'G'),
        ('qhtml', 'HR_OPEN', 'H'): ('qhtml', 'H'),
        ('qhtml', 'HR_OPEN', 'I'): ('qhtml', 'I'),
        ('qhtml', 'HR_OPEN', 'J'): ('qhtml', 'J'),
        ('qhtml', 'HR_OPEN', 'K'): ('qhtml', 'K'),
        ('qhtml', 'HR_OPEN', 'L'): ('qhtml', 'L'),
        ('qhtml', 'HR_OPEN', 'M'): ('qhtml', 'M'),
        ('qhtml', 'HR_OPEN', 'N'): ('qhtml', 'N'),
        ('qhtml', 'HR_OPEN', 'O'): ('qhtml', 'O'),
        ('qhtml', 'HR_OPEN', 'P'): ('qhtml', 'P'),
        ('qhtml', 'HR_OPEN', 'Q'): ('qhtml', 'Q'),
        ('qhtml', 'HR_OPEN', 'R'): ('qhtml', 'R'),
        ('qhtml', 'HR_OPEN', 'S'): ('qhtml', 'S'),
        ('qhtml', 'HR_OPEN', 'T'): ('qhtml', 'T'),
        ('qhtml', 'HR_OPEN', 'U'): ('qhtml', 'U'),
        ('qhtml', 'HR_OPEN', 'V'): ('qhtml', 'V'),
        ('qhtml', 'HR_OPEN', 'W'): ('qhtml', 'W'),
        ('qhtml', 'HR_OPEN', 'X'): ('qhtml', 'X'),
        ('qhtml', 'HR_OPEN', 'Y'): ('qhtml', 'Y'),

        ('qhtml', 'DIV_OPEN', 'C'): ('qhtml', ('R', 'C')),
        ('qhtml', 'DIV_OPEN', 'E'): ('qhtml', ('R', 'E')),
        ('qhtml', 'DIV_OPEN', 'F'): ('qhtml', ('R', 'F')),
        ('qhtml', 'DIV_OPEN', 'G'): ('qhtml', ('R', 'G')),
        ('qhtml', 'DIV_OPEN', 'H'): ('qhtml', ('R', 'H')),
        ('qhtml', 'DIV_OPEN', 'I'): ('qhtml', ('R', 'I')),
        ('qhtml', 'DIV_OPEN', 'J'): ('qhtml', ('R', 'J')),
        ('qhtml', 'DIV_OPEN', 'K'): ('qhtml', ('R', 'K')),
        ('qhtml', 'DIV_OPEN', 'L'): ('qhtml', ('R', 'L')),
        ('qhtml', 'DIV_OPEN', 'M'): ('qhtml', ('R', 'M')),
        ('qhtml', 'DIV_OPEN', 'N'): ('qhtml', ('R', 'N')),
        ('qhtml', 'DIV_OPEN', 'O'): ('qhtml', ('R', 'O')),
        ('qhtml', 'DIV_OPEN', 'P'): ('qhtml', ('R', 'P')),
        ('qhtml', 'DIV_OPEN', 'Q'): ('qhtml', ('Q', 'R')),
        ('qhtml', 'DIV_OPEN', 'S'): ('qhtml', ('R', 'S')),
        ('qhtml', 'DIV_OPEN', 'T'): ('qhtml', ('R', 'T')),
        ('qhtml', 'DIV_OPEN', 'U'): ('qhtml', ('R', 'U')),
        ('qhtml', 'DIV_OPEN', 'V'): ('qhtml', ('R', 'V')),
        ('qhtml', 'DIV_OPEN', 'W'): ('qhtml', ('R', 'W')),
        ('qhtml', 'DIV_OPEN', 'X'): ('qhtml', ('R', 'X')),
        ('qhtml', 'DIV_OPEN', 'Y'): ('qhtml', ('R', 'Y')),
        ('qhtml', 'DIV_CLOSE', 'R'): ('qhtml', 'epsilon'),
     
      
    
        ('qhtml', 'BUTTON_OPEN', 'C'): ('qhtml', ('T', 'C')),
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

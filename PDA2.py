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
    initial_state = 'qkurung'
    initial_stack_symbol = 'Z'
    transitions = {
        # HTML
        ('qkurung', 'HTML_OPEN', 'Z'): ('qhtml', ('A', 'Z')),
        ('qhtml', 'CLASS', 'A'): ('qhtml', 'A'),
        ('qhtml', 'ID', 'A'): ('qhtml', 'A'),
        ('qhtml', 'NAME', 'A'): ('qhtml', 'A'),
        ('qhtml', 'KURUNG_TUTUP', 'A'): ('qkurunghead', 'A'),
        ('qkurunghead', 'VAR', 'A'): ('qkurunghead', 'A'),
        ('qkurung', 'HTML_CLOSE', 'A'): ('qkurung', 'epsilon'),

        ('qkurunghead', 'HEAD_OPEN', 'A'): ('qhead', ('B', 'A')),
        ('qhead', 'CLASS', 'B'): ('qhead', 'B'),
        ('qhead', 'ID', 'B'): ('qhead', 'B'),
        ('qhead', 'STYLE', 'B'): ('qhead', 'B'),
        ('qhead', 'KURUNG_TUTUP', 'B'): ('qkurunghead', 'B'),
        ('qkurunghead', 'VAR', 'B'): ('qkurunghead', 'B'),
        ('qkurunghead', 'HEAD_CLOSE', 'B'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'BODY_OPEN', 'A'): ('qbody', ('C', 'A')),
        ('qbody', 'CLASS', 'C'): ('qbody', 'C'),
        ('qbody', 'ID', 'C'): ('qbody', 'C'),
        ('qbody', 'STYLE', 'C'): ('qbody', 'C'),
        ('qbody', 'KURUNG_TUTUP', 'C'): ('qkurungbody', 'C'),
        ('qkurungbody', 'VAR', 'C'): ('qkurungbody', 'C'),
        ('qkurungbody', 'BODY_CLOSE', 'C'): ('qkurung', 'epsilon'),

        ('qkurunghead', 'TITLE_OPEN', 'B'): ('qtitle', ('D', 'B')),
        ('qtitle', 'CLASS', 'D'): ('qtitle', 'D'),
        ('qtitle', 'ID', 'D'): ('qtitle', 'D'),
        ('qtitle', 'STYLE', 'D'): ('qtitle', 'D'),
        ('qtitle', 'KURUNG_TUTUP', 'D'): ('qkurunghead', 'D'),
        ('qkurunghead', 'VAR', 'D'): ('qkurunghead', 'D'),
        ('qkurunghead', 'TITLE_CLOSE', 'D'): ('qkurunghead', 'epsilon'),

        ('qkurunghead', 'SCRIPT_OPEN', 'B'): ('qscripthead', ('E', 'B')),
        ('qkurungbody', 'SCRIPT_OPEN', 'C'): ('qscriptbody', ('E', 'C')),
        ('qscripthead', 'SRC', 'E'): ('qscripthead', 'E'),
        ('qscriptbody', 'SRC', 'E'): ('qscriptbody', 'E'),
        ('qscripthead', 'CLASS', 'E'): ('qscripthead', 'E'),
        ('qscriptbody', 'CLASS', 'E'): ('qscriptbody', 'E'),
        ('qscripthead', 'ID', 'E'): ('qscripthead', 'E'),
        ('qscriptbody', 'ID', 'E'): ('qscriptbody', 'E'),
        ('qscripthead', 'STYLE', 'E'): ('qscripthead', 'E'),
        ('qscriptbody', 'STYLE', 'E'): ('qscriptbody', 'E'),
        ('qscripthead', 'KURUNG_TUTUP', 'E'): ('qkurunghead', 'E'),
        ('qkurunghead', 'VAR', 'E'): ('qkurunghead', 'E'),
        ('qscriptbody', 'KURUNG_TUTUP', 'E'): ('qkurungbody', 'E'),
        ('qkurungbody', 'VAR', 'E'): ('qkurungbody', 'E'),
        ('qkurunghead', 'SCRIPT_CLOSE', 'E'): ('qkurunghead', 'epsilon'),
        ('qkurungbody', 'SCRIPT_CLOSE', 'E'): ('qkurungbody', 'epsilon'),


        ('qkurungbody', 'H1_OPEN', 'C'): ('qh1', ('F', 'C')),
        ('qkurungbody', 'H1_OPEN', 'S'): ('qh1', ('F', 'S')),
        ('qh1', 'CLASS', 'F'): ('qh1', 'F'),
        ('qh1', 'ID', 'F'): ('qh1', 'F'),
        ('qh1', 'STYLE', 'F'): ('qh1', 'F'),
        ('qh1', 'KURUNG_TUTUP', 'F'): ('qkurungbody', 'F'),
        ('qkurungbody', 'VAR', 'F'): ('qkurungbody', 'F'),
        ('qkurungbody', 'H1_CLOSE', 'F'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'H2_OPEN', 'C'): ('qh2', ('G', 'C')),
        ('qkurungbody', 'H2_OPEN', 'S'): ('qh1', ('G', 'S')),
        ('qh2', 'CLASS', 'G'): ('qh2', 'G'),
        ('qh2', 'ID', 'G'): ('qh2', 'G'),
        ('qh2', 'STYLE', 'G'): ('qh2', 'G'),
        ('qh2', 'KURUNG_TUTUP', 'G'): ('qkurungbody', 'G'),
        ('qkurungbody', 'VAR', 'G'): ('qkurungbody', 'G'),
        ('qkurungbody', 'H2_CLOSE', 'G'): ('qkurungbody', 'epsilon'),
        
        ('qkurungbody', 'H3_OPEN', 'C'): ('qh3', ('H', 'C')),
        ('qkurungbody', 'H3_OPEN', 'S'): ('qh3', ('H', 'S')),
        ('qh3', 'CLASS', 'H'): ('qh3', 'H'),
        ('qh3', 'ID', 'H'): ('qh3', 'H'),
        ('qh3', 'STYLE', 'H'): ('qh3', 'H'),
        ('qh3', 'KURUNG_TUTUP', 'H'): ('qkurungbody', 'H'),
        ('qkurungbody', 'VAR', 'H'): ('qkurungbody', 'H'),
        ('qkurungbody', 'H3_CLOSE', 'H'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'H4_OPEN', 'C'): ('qh4', ('I', 'C')),
        ('qkurungbody', 'H4_OPEN', 'S'): ('qh4', ('I', 'S')),
        ('qh4', 'CLASS', 'I'): ('qh4', 'I'),
        ('qh4', 'ID', 'I'): ('qh4', 'I'),
        ('qh4', 'STYLE', 'I'): ('qh4', 'I'),
        ('qh4', 'KURUNG_TUTUP', 'I'): ('qkurungbody', 'I'),
        ('qkurungbody', 'VAR', 'I'): ('qkurungbody', 'I'),
        ('qkurungbody', 'H4_CLOSE', 'I'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'H5_OPEN', 'C'): ('qh5', ('J', 'C')),
        ('qkurungbody', 'H5_OPEN', 'S'): ('qh5', ('J', 'S')),
        ('qh5', 'CLASS', 'J'): ('qh5', 'J'),
        ('qh5', 'ID', 'J'): ('qh5', 'J'),
        ('qh5', 'STYLE', 'J'): ('qh5', 'J'),
        ('qh5', 'KURUNG_TUTUP', 'J'): ('qkurungbody', 'J'),
        ('qkurungbody', 'VAR', 'J'): ('qkurungbody', 'J'),
        ('qkurungbody', 'H5_CLOSE', 'J'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'H6_OPEN', 'C'): ('qh6', ('K', 'C')),
        ('qkurungbody', 'H6_OPEN', 'S'): ('qh6', ('K', 'S')),
        ('qh6', 'CLASS', 'K'): ('qh6', 'K'),
        ('qh6', 'ID', 'K'): ('qh6', 'K'),
        ('qh6', 'STYLE', 'K'): ('qh6', 'K'),
        ('qh6', 'KURUNG_TUTUP', 'K'): ('qkurungbody', 'K'),
        ('qkurungbody', 'VAR', 'K'): ('qkurungbody', 'K'),
        ('qkurungbody', 'H6_CLOSE', 'K'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'P_OPEN', 'C'): ('qp', ('L', 'C')),
        ('qkurungbody', 'P_OPEN', 'S'): ('qp', ('L', 'S')),
        ('qp', 'CLASS', 'L'): ('qp', 'L'),
        ('qp', 'ID', 'L'): ('qp', 'L'),
        ('qp', 'STYLE', 'L'): ('qp', 'L'),
        ('qp', 'KURUNG_TUTUP', 'L'): ('qkurungbody', 'L'),
        ('qkurungbody', 'VAR', 'L'): ('qkurungbody', 'L'),
        ('qkurungbody', 'P_CLOSE', 'L'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'EM_OPEN', 'C'): ('qem', ('M', 'C')),
        ('qkurunghead', 'EM_OPEN', 'D'): ('qemhead', ('M', 'D')),
        ('qkurunghead', 'EM_OPEN', 'E'): ('qemhead', ('M', 'E')),
        ('qkurungbody', 'EM_OPEN', 'E'): ('qem', ('M', 'E')),
        ('qkurungbody', 'EM_OPEN', 'F'): ('qem', ('M', 'F')),
        ('qkurungbody', 'EM_OPEN', 'G'): ('qem', ('M', 'G')),
        ('qkurungbody', 'EM_OPEN', 'H'): ('qem', ('M', 'H')),
        ('qkurungbody', 'EM_OPEN', 'I'): ('qem', ('M', 'I')),
        ('qkurungbody', 'EM_OPEN', 'J'): ('qem', ('M', 'J')),
        ('qkurungbody', 'EM_OPEN', 'K'): ('qem', ('M', 'K')),
        ('qkurungbody', 'EM_OPEN', 'L'): ('qem', ('M', 'L')),
        ('qkurungbody', 'EM_OPEN', 'N'): ('qem', ('M', 'N')),
        ('qkurungbody', 'EM_OPEN', 'S'): ('qem', ('M', 'S')),
        ('qkurungbody', 'EM_OPEN', 'T'): ('qem', ('M', 'T')),
        ('qkurungbody', 'EM_OPEN', 'U'): ('qem', ('M', 'U')),
        ('qkurungbody', 'EM_OPEN', 'V'): ('qem', ('M', 'V')),
        ('qkurungbody', 'EM_OPEN', 'W'): ('qem', ('M', 'W')),
        ('qkurungbody', 'EM_OPEN', 'X'): ('qem', ('M', 'X')),
        ('qkurungbody', 'EM_OPEN', 'Y'): ('qem', ('M', 'Y')),
        ('qem', 'CLASS', 'M'): ('qem', 'M'),
        ('qem', 'ID', 'M'): ('qem', 'M'),
        ('qem', 'STYLE', 'M'): ('qem', 'M'),
        ('qem', 'KURUNG_TUTUP', 'M'): ('qkurungbody', 'M'),
        ('qemhead', 'CLASS', 'M'): ('qemhead', 'M'),
        ('qemhead', 'ID', 'M'): ('qemhead', 'M'),
        ('qemhead', 'STYLE', 'M'): ('qemhead', 'M'),
        ('qemhead', 'KURUNG_TUTUP', 'M'): ('qkurunghead', 'M'),
        ('qkurungbody', 'VAR', 'M'): ('qkurungbody', 'M'),
        ('qkurunghead', 'VAR', 'M'): ('qkurunghead', 'M'),
        ('qkurungbody', 'EM_CLOSE', 'M'): ('qkurungbody', 'epsilon'),
        ('qkurunghead', 'EM_CLOSE', 'M'): ('qkurunghead', 'epsilon'),

        ('qkurungbody', 'BUTTON_OPEN', 'C'): ('qbutton', ('N', 'C')),
        ('qkurungbody', 'BUTTON_OPEN', 'U'): ('qbutton', ('N', 'U')),
        ('qkurungbody', 'BUTTON_OPEN', 'S'): ('qbutton', ('N', 'S')),
        ('qbutton', 'TYPE_BUTTON', 'N'): ('qbutton', 'N'),
        ('qbutton', 'CLASS', 'N'): ('qbutton', 'N'),
        ('qbutton', 'ID', 'N'): ('qbutton', 'N'),
        ('qbutton', 'STYLE', 'N'): ('qbutton', 'N'),
        ('qbutton', 'KURUNG_TUTUP', 'N'): ('qkurungbody', 'N'),
        ('qkurungbody', 'VAR', 'N'): ('qkurungbody', 'N'),
        ('qkurungbody', 'BUTTON_CLOSE', 'N'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'B_OPEN', 'C'): ('qb', ('O', 'C')),
        ('qkurunghead', 'B_OPEN', 'D'): ('qbhead', ('O', 'D')),
        ('qkurunghead', 'B_OPEN', 'E'): ('qbhead', ('O', 'E')),
        ('qkurungbody', 'B_OPEN', 'E'): ('qb', ('O', 'E')),
        ('qkurungbody', 'B_OPEN', 'F'): ('qb', ('O', 'F')),
        ('qkurungbody', 'B_OPEN', 'G'): ('qb', ('O', 'G')),
        ('qkurungbody', 'B_OPEN', 'H'): ('qb', ('O', 'H')),
        ('qkurungbody', 'B_OPEN', 'I'): ('qb', ('O', 'I')),
        ('qkurungbody', 'B_OPEN', 'J'): ('qb', ('O', 'J')),
        ('qkurungbody', 'B_OPEN', 'K'): ('qb', ('O', 'K')),
        ('qkurungbody', 'B_OPEN', 'L'): ('qb', ('O', 'L')),
        ('qkurungbody', 'B_OPEN', 'N'): ('qb', ('O', 'N')),
        ('qkurungbody', 'B_OPEN', 'S'): ('qb', ('O', 'S')),
        ('qkurungbody', 'B_OPEN', 'T'): ('qb', ('O', 'T')),
        ('qkurungbody', 'B_OPEN', 'U'): ('qb', ('O', 'U')),
        ('qkurungbody', 'B_OPEN', 'V'): ('qb', ('O', 'V')),
        ('qkurungbody', 'B_OPEN', 'W'): ('qb', ('O', 'W')),
        ('qkurungbody', 'B_OPEN', 'X'): ('qb', ('O', 'X')),
        ('qkurungbody', 'B_OPEN', 'Y'): ('qb', ('O', 'Y')),
        ('qb', 'CLASS', 'O'): ('qb', 'O'),
        ('qb', 'ID', 'O'): ('qb', 'O'),
        ('qb', 'STYLE', 'O'): ('qb', 'O'),
        ('qb', 'KURUNG_TUTUP', 'O'): ('qkurungbody', 'O'),
        ('qbhead', 'CLASS', 'O'): ('qbhead', 'O'),
        ('qbhead', 'ID', 'O'): ('qbhead', 'O'),
        ('qbhead', 'STYLE', 'O'): ('qbhead', 'O'),
        ('qbhead', 'KURUNG_TUTUP', 'O'): ('qkurunghead', 'O'),
        ('qkurungbody', 'VAR', 'O'): ('qkurungbody', 'O'),
        ('qkurunghead', 'VAR', 'O'): ('qkurunghead', 'O'),
        ('qkurungbody', 'B_CLOSE', 'O'): ('qkurungbody', 'epsilon'),
        ('qkurunghead', 'B_CLOSE', 'O'): ('qkurunghead', 'epsilon'),

        ('qkurungbody', 'ABBR_OPEN', 'C'): ('qabbr', ('P', 'C')),
        ('qkurunghead', 'ABBR_OPEN', 'D'): ('qabbrhead', ('P', 'D')),
        ('qkurunghead', 'ABBR_OPEN', 'E'): ('qabbrhead', ('P', 'E')),
        ('qkurungbody', 'ABBR_OPEN', 'E'): ('qabbr', ('P', 'E')),
        ('qkurungbody', 'ABBR_OPEN', 'F'): ('qabbr', ('P', 'F')),
        ('qkurungbody', 'ABBR_OPEN', 'G'): ('qabbr', ('P', 'G')),
        ('qkurungbody', 'ABBR_OPEN', 'H'): ('qabbr', ('P', 'H')),
        ('qkurungbody', 'ABBR_OPEN', 'I'): ('qabbr', ('P', 'I')),
        ('qkurungbody', 'ABBR_OPEN', 'J'): ('qabbr', ('P', 'J')),
        ('qkurungbody', 'ABBR_OPEN', 'K'): ('qabbr', ('P', 'K')),
        ('qkurungbody', 'ABBR_OPEN', 'L'): ('qabbr', ('P', 'L')),
        ('qkurungbody', 'ABBR_OPEN', 'N'): ('qabbr', ('P', 'N')),
        ('qkurungbody', 'ABBR_OPEN', 'S'): ('qabbr', ('P', 'S')),
        ('qkurungbody', 'ABBR_OPEN', 'T'): ('qabbr', ('P', 'T')),
        ('qkurungbody', 'ABBR_OPEN', 'U'): ('qabbr', ('P', 'U')),
        ('qkurungbody', 'ABBR_OPEN', 'V'): ('qabbr', ('P', 'V')),
        ('qkurungbody', 'ABBR_OPEN', 'W'): ('qabbr', ('P', 'W')),
        ('qkurungbody', 'ABBR_OPEN', 'X'): ('qabbr', ('P', 'X')),
        ('qkurungbody', 'ABBR_OPEN', 'Y'): ('qabbr', ('P', 'Y')),
        ('qabbr', 'CLASS', 'P'): ('qabbr', 'P'),
        ('qabbr', 'ID', 'P'): ('qabbr', 'P'),
        ('qabbr', 'STYLE', 'P'): ('qabbr', 'P'),
        ('qabbr', 'KURUNG_TUTUP', 'P'): ('qkurungbody', 'P'),
        ('qabbrhead', 'CLASS', 'P'): ('qabbrhead', 'P'),
        ('qabbrhead', 'ID', 'P'): ('qabbrhead', 'P'),
        ('qabbrhead', 'STYLE', 'P'): ('qabbrhead', 'P'),
        ('qabbrhead', 'KURUNG_TUTUP', 'P'): ('qkurunghead', 'P'),
        ('qkurungbody', 'VAR', 'P'): ('qkurungbody', 'P'),
        ('qkurunghead', 'VAR', 'P'): ('qkurunghead', 'P'),
        ('qkurungbody', 'ABBR_CLOSE', 'P'): ('qkurungbody', 'epsilon'),
        ('qkurunghead', 'ABBR_CLOSE', 'P'): ('qkurunghead', 'epsilon'),

        ('qkurungbody', 'STRONG_OPEN', 'C'): ('qstrong', ('Q', 'C')),
        ('qkurunghead', 'STRONG_OPEN', 'D'): ('qstronghead', ('Q', 'D')),
        ('qkurunghead', 'STRONG_OPEN', 'E'): ('qstronghead', ('Q', 'E')),
        ('qkurungbody', 'STRONG_OPEN', 'E'): ('qstrong', ('Q', 'E')),
        ('qkurungbody', 'STRONG_OPEN', 'F'): ('qstrong', ('Q', 'F')),
        ('qkurungbody', 'STRONG_OPEN', 'G'): ('qstrong', ('Q', 'G')),
        ('qkurungbody', 'STRONG_OPEN', 'H'): ('qstrong', ('Q', 'H')),
        ('qkurungbody', 'STRONG_OPEN', 'I'): ('qstrong', ('Q', 'I')),
        ('qkurungbody', 'STRONG_OPEN', 'J'): ('qstrong', ('Q', 'J')),
        ('qkurungbody', 'STRONG_OPEN', 'K'): ('qstrong', ('Q', 'K')),
        ('qkurungbody', 'STRONG_OPEN', 'L'): ('qstrong', ('Q', 'L')),
        ('qkurungbody', 'STRONG_OPEN', 'N'): ('qstrong', ('Q', 'N')),
        ('qkurungbody', 'STRONG_OPEN', 'S'): ('qstrong', ('Q', 'S')),
        ('qkurungbody', 'STRONG_OPEN', 'T'): ('qstrong', ('Q', 'T')),
        ('qkurungbody', 'STRONG_OPEN', 'U'): ('qstrong', ('Q', 'U')),
        ('qkurungbody', 'STRONG_OPEN', 'V'): ('qstrong', ('Q', 'V')),
        ('qkurungbody', 'STRONG_OPEN', 'W'): ('qstrong', ('Q', 'W')),
        ('qkurungbody', 'STRONG_OPEN', 'X'): ('qstrong', ('Q', 'X')),
        ('qkurungbody', 'STRONG_OPEN', 'Y'): ('qstrong', ('Q', 'Y')),
        ('qstrong', 'CLASS', 'Q'): ('qstrong', 'Q'),
        ('qstrong', 'ID', 'Q'): ('qstrong', 'Q'),
        ('qstrong', 'STYLE', 'Q'): ('qstrong', 'Q'),
        ('qstrong', 'KURUNG_TUTUP', 'Q'): ('qkurungbody', 'Q'),
        ('qstronghead', 'CLASS', 'Q'): ('qstronghead', 'Q'),
        ('qstronghead', 'ID', 'Q'): ('qstronghead', 'Q'),
        ('qstronghead', 'STYLE', 'Q'): ('qstronghead', 'Q'),
        ('qstronghead', 'KURUNG_TUTUP', 'Q'): ('qkurunghead', 'Q'),
        ('qkurungbody', 'VAR', 'Q'): ('qkurungbody', 'Q'),
        ('qkurunghead', 'VAR', 'Q'): ('qkurunghead', 'Q'),
        ('qkurungbody', 'STRONG_CLOSE', 'Q'): ('qkurungbody', 'epsilon'),
        ('qkurunghead', 'STRONG_CLOSE', 'Q'): ('qkurunghead', 'epsilon'),

        ('qkurungbody', 'SMALL_OPEN', 'C'): ('qsmall', ('R', 'C')),
        ('qkurunghead', 'SMALL_OPEN', 'D'): ('qsmallhead', ('R', 'D')),
        ('qkurunghead', 'SMALL_OPEN', 'E'): ('qsmallhead', ('R', 'E')),
        ('qkurungbody', 'SMALL_OPEN', 'F'): ('qsmall', ('R', 'F')),
        ('qkurungbody', 'SMALL_OPEN', 'G'): ('qsmall', ('R', 'G')),
        ('qkurungbody', 'SMALL_OPEN', 'H'): ('qsmall', ('R', 'H')),
        ('qkurungbody', 'SMALL_OPEN', 'I'): ('qsmall', ('R', 'I')),
        ('qkurungbody', 'SMALL_OPEN', 'J'): ('qsmall', ('R', 'J')),
        ('qkurungbody', 'SMALL_OPEN', 'K'): ('qsmall', ('R', 'K')),
        ('qkurungbody', 'SMALL_OPEN', 'L'): ('qsmall', ('R', 'L')),
        ('qkurungbody', 'SMALL_OPEN', 'N'): ('qsmall', ('R', 'N')),
        ('qkurungbody', 'SMALL_OPEN', 'S'): ('qsmall', ('R', 'S')),
        ('qkurungbody', 'SMALL_OPEN', 'T'): ('qsmall', ('R', 'T')),
        ('qkurungbody', 'SMALL_OPEN', 'U'): ('qsmall', ('R', 'U')),
        ('qkurungbody', 'SMALL_OPEN', 'V'): ('qsmall', ('R', 'V')),
        ('qkurungbody', 'SMALL_OPEN', 'W'): ('qsmall', ('R', 'W')),
        ('qkurungbody', 'SMALL_OPEN', 'X'): ('qsmall', ('R', 'X')),
        ('qkurungbody', 'SMALL_OPEN', 'Y'): ('qsmall', ('R', 'Y')),
        ('qsmall', 'CLASS', 'R'): ('qsmall', 'R'),
        ('qsmall', 'ID', 'R'): ('qsmall', 'R'),
        ('qsmall', 'STYLE', 'R'): ('qsmall', 'R'),
        ('qsmall', 'KURUNG_TUTUP', 'R'): ('qkurungbody', 'R'),
        ('qsmallhead', 'CLASS', 'R'): ('qsmallhead', 'R'),
        ('qsmallhead', 'ID', 'R'): ('qsmall', 'R'),
        ('qsmallhead', 'STYLE', 'R'): ('qsmallhead', 'R'),
        ('qsmallhead', 'KURUNG_TUTUP', 'R'): ('qkurunghead', 'R'),
        ('qkurungbody', 'VAR', 'R'): ('qkurungbody', 'R'),
        ('qkurunghead', 'VAR', 'R'): ('qkurunghead', 'R'),
        ('qkurunghead', 'SMALL_CLOSE', 'R'): ('qkurunghead', 'epsilon'),
        ('qkurungbody', 'SMALL_CLOSE', 'R'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'DIV_OPEN', 'C'): ('qdiv', ('S', 'C')),
        ('qkurungbody', 'DIV_OPEN', 'U'): ('qdiv', ('S', 'U')),
        ('qkurungbody', 'DIV_OPEN', 'S'): ('qdiv', ('S', 'S')),
        ('qdiv', 'CLASS', 'S'): ('qdiv', 'S'),
        ('qdiv', 'ID', 'S'): ('qdiv', 'S'),
        ('qdiv', 'STYLE', 'S'): ('qdiv', 'S'),
        ('qdiv', 'KURUNG_TUTUP', 'S'): ('qkurungbody', 'S'),
        ('qkurungbody', 'VAR', 'S'): ('qkurungbody', 'S'),
        ('qkurungbody', 'DIV_CLOSE', 'S'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'A_OPEN', 'C'): ('qa', ('T', 'C')),
        ('qkurungbody', 'A_OPEN', 'S'): ('qa', ('T', 'S')),
        ('qa', 'HREF', 'T'): ('qa', 'T'),
        ('qa', 'CLASS', 'T'): ('qa', 'T'),
        ('qa', 'ID', 'T'): ('qa', 'T'),
        ('qa', 'STYLE', 'T'): ('qa', 'T'),
        ('qa', 'KURUNG_TUTUP', 'T'): ('qkurungbody', 'T'),
        ('qkurungbody', 'VAR', 'T'): ('qkurungbody', 'T'),
        ('qkurungbody', 'A_CLOSE', 'T'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'FORM_OPEN', 'C'): ('qform', ('U', 'C')),
        ('qkurungbody', 'FORM_OPEN', 'S'): ('qform', ('U', 'S')),
        ('qform', 'ACTION', 'U'): ('qform', 'U'),
        ('qform', 'METHOD', 'U'): ('qform', 'U'),
        ('qform', 'CLASS', 'U'): ('qform', 'U'),
        ('qform', 'ID', 'U'): ('qform', 'U'),
        ('qform', 'STYLE', 'U'): ('qform', 'U'),
        ('qform', 'KURUNG_TUTUP', 'U'): ('qkurungbody', 'U'),
        ('qkurungbody', 'VAR', 'U'): ('qkurungbody', 'U'),
        ('qkurungbody', 'FORM_CLOSE', 'U'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'TABLE_OPEN', 'C'): ('qtable', ('V', 'C')),
        ('qkurungbody', 'TABLE_OPEN', 'S'): ('qtable', ('V', 'S')),
        ('qtable', 'CLASS', 'V'): ('qtable', 'V'),
        ('qtable', 'ID', 'V'): ('qtable', 'V'),
        ('qtable', 'STYLE', 'V'): ('qtable', 'V'),
        ('qtable', 'KURUNG_TUTUP', 'V'): ('qkurungbody', 'V'),
        ('qkurungbody', 'VAR', 'V'): ('qkurungbody', 'V'),
        ('qkurungbody', 'TABLE_CLOSE', 'V'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'TR_OPEN', 'V'): ('qtr', ('W', 'V')),
        ('qtr', 'CLASS', 'W'): ('qtr', 'W'),
        ('qtr', 'ID', 'W'): ('qtr', 'W'),
        ('qtr', 'STYLE', 'W'): ('qtr', 'W'),
        ('qtr', 'KURUNG_TUTUP', 'W'): ('qkurungbody', 'W'),
        ('qkurungbody', 'VAR', 'W'): ('qkurungbody', 'W'),
        ('qkurungbody', 'TR_CLOSE', 'W'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'TD_OPEN', 'V'): ('qtd', ('X', 'V')),
        ('qtd', 'CLASS', 'X'): ('qtd', 'X'),
        ('qtd', 'ID', 'X'): ('qtd', 'X'),
        ('qtd', 'STYLE', 'X'): ('qtd', 'X'),
        ('qtd', 'KURUNG_TUTUP', 'X'): ('qkurungbody', 'X'),
        ('qkurungbody', 'VAR', 'X'): ('qkurungbody', 'X'),
        ('qkurungbody', 'TD_CLOSE', 'X'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'TH_OPEN', 'V'): ('qth', ('Y', 'V')),
        ('qth', 'CLASS', 'Y'): ('qth', 'Y'),
        ('qth', 'ID', 'Y'): ('qth', 'Y'),
        ('qth', 'STYLE', 'Y'): ('qth', 'Y'),
        ('qth', 'KURUNG_TUTUP', 'Y'): ('qkurungbody', 'Y'),
        ('qkurungbody', 'VAR', 'Y'): ('qkurungbody', 'Y'),
        ('qkurungbody', 'TH_CLOSE', 'Y'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'LINK', 'C'): ('qlink', ('p', 'a', 'C')),
        ('qkurungbody', 'LINK', 'S'): ('qlink', ('p', 'a', 'S')),
        ('qlink', 'REL', 'p'): ('qlink', 'epsilon'),
        ('qlink', 'HREF', 'a'): ('qlink', 'a'),
        ('qlink', 'HREF', 'p'): ('qlink', 'p'),
        ('qlink', 'CLASS', 'a'): ('qlink', 'a'),
        ('qlink', 'CLASS', 'p'): ('qlink', 'p'),
        ('qlink', 'ID', 'a'): ('qlink', 'a'),
        ('qlink', 'ID', 'p'): ('qlink', 'p'),
        ('qlink', 'STYLE', 'a'): ('qlink', 'a'),
        ('qlink', 'STYLE', 'p'): ('qlink', 'p'),
        ('qlink', 'KURUNG_TUTUP', 'a'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'BR', 'C'): ('qbr', ('b', 'C')),
        ('qkurunghead', 'BR', 'D'): ('qbr', ('b', 'D')),
        ('qkurunghead', 'BR', 'E'): ('qbr', ('b', 'E')),
        ('qkurungbody', 'BR', 'E'): ('qbr', ('b', 'E')),
        ('qkurungbody', 'BR', 'F'): ('qbr', ('b', 'F')),
        ('qkurungbody', 'BR', 'G'): ('qbr', ('b', 'G')),
        ('qkurungbody', 'BR', 'H'): ('qbr', ('b', 'H')),
        ('qkurungbody', 'BR', 'I'): ('qbr', ('b', 'I')),
        ('qkurungbody', 'BR', 'J'): ('qbr', ('b', 'J')),
        ('qkurungbody', 'BR', 'K'): ('qbr', ('b', 'K')),
        ('qkurungbody', 'BR', 'L'): ('qbr', ('b', 'L')),
        ('qkurungbody', 'BR', 'N'): ('qbr', ('b', 'N')),
        ('qkurungbody', 'BR', 'S'): ('qbr', ('b', 'S')),
        ('qkurungbody', 'BR', 'T'): ('qbr', ('b', 'T')),
        ('qkurungbody', 'BR', 'U'): ('qbr', ('b', 'U')),
        ('qkurungbody', 'BR', 'V'): ('qbr', ('b', 'V')),
        ('qkurungbody', 'BR', 'W'): ('qbr', ('b', 'W')),
        ('qkurungbody', 'BR', 'X'): ('qbr', ('b', 'X')),
        ('qkurungbody', 'BR', 'Y'): ('qbr', ('b', 'Y')),
        ('qbr', 'CLASS', 'b'): ('qbr', 'b'),
        ('qbr', 'ID', 'b'): ('qbr', 'b'),
        ('qbr', 'STYLE', 'b'): ('qbr', 'b'),
        ('qbr', 'KURUNG_TUTUP', 'b'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'HR', 'C'): ('qhr', ('c', 'C')),
        ('qkurunghead', 'HR', 'D'): ('qhr', ('c', 'D')),
        ('qkurunghead', 'HR', 'E'): ('qhr', ('c', 'E')),
        ('qkurungbody', 'HR', 'E'): ('qhr', ('c', 'E')),
        ('qkurungbody', 'HR', 'F'): ('qhr', ('c', 'F')),
        ('qkurungbody', 'HR', 'G'): ('qhr', ('c', 'G')),
        ('qkurungbody', 'HR', 'H'): ('qhr', ('c', 'H')),
        ('qkurungbody', 'HR', 'I'): ('qhr', ('c', 'I')),
        ('qkurungbody', 'HR', 'J'): ('qhr', ('c', 'J')),
        ('qkurungbody', 'HR', 'K'): ('qhr', ('c', 'K')),
        ('qkurungbody', 'HR', 'L'): ('qhr', ('c', 'L')),
        ('qkurungbody', 'HR', 'N'): ('qhr', ('c', 'N')),
        ('qkurungbody', 'HR', 'S'): ('qhr', ('c', 'S')),
        ('qkurungbody', 'HR', 'T'): ('qhr', ('c', 'T')),
        ('qkurungbody', 'HR', 'U'): ('qhr', ('c', 'U')),
        ('qkurungbody', 'HR', 'V'): ('qhr', ('c', 'V')),
        ('qkurungbody', 'HR', 'W'): ('qhr', ('c', 'W')),
        ('qkurungbody', 'HR', 'X'): ('qhr', ('c', 'X')),
        ('qkurungbody', 'HR', 'Y'): ('qhr', ('c', 'Y')),
        ('qhr', 'CLASS', 'c'): ('qhr', 'c'),
        ('qhr', 'ID', 'c'): ('qhr', 'c'),
        ('qhr', 'STYLE', 'c'): ('qhr', 'c'),
        ('qhr', 'KURUNG_TUTUP', 'c'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'IMG', 'C'): ('qimg', ('q','d', 'C')),
        ('qkurungbody', 'IMG', 'S'): ('qimg', ('q','d', 'S')),
        ('qimg', 'SRC', 'q'): ('qimg', 'epsilon'),
        ('qimg', 'ALT', 'd'): ('qimg', 'd'),
        ('qimg', 'ALT', 'q'): ('qimg', 'q'),
        ('qimg', 'CLASS', 'd'): ('qimg', 'd'),
        ('qimg', 'CLASS', 'q'): ('qimg', 'q'),
        ('qimg', 'ID', 'd'): ('qimg', 'd'),
        ('qimg', 'ID', 'q'): ('qimg', 'q'),
        ('qimg', 'STYLE', 'd'): ('qimg', 'd'),
        ('qimg', 'STYLE', 'q'): ('qimg', 'q'),
        ('qimg', 'KURUNG_TUTUP', 'd'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'INPUT', 'C'): ('qinput', ('e', 'C')),
        ('qkurungbody', 'INPUT', 'S'): ('qinput', ('e', 'S')),
        ('qkurungbody', 'INPUT', 'U'): ('qinput', ('e', 'U')),
        ('qinput', 'TYPE_INPUT', 'e'): ('qinput', 'e'),
        ('qinput', 'CLASS', 'e'): ('qinput', 'e'),
        ('qinput', 'ID', 'e'): ('qinput', 'e'),
        ('qinput', 'STYLE', 'e'): ('qinput', 'e'),
        ('qinput', 'KURUNG_TUTUP', 'e'): ('qkurungbody', 'epsilon'),

        ('qkurungbody', 'KOMEN', 'A'): ('qkurungbody', 'A'),
        ('qkurungbody', 'KOMEN', 'B'): ('qkurungbody', 'B'),
        ('qkurungbody', 'KOMEN', 'C'): ('qkurungbody', 'C'),
        ('qkurungbody', 'KOMEN', 'D'): ('qkurungbody', 'D'),
        ('qkurungbody', 'KOMEN', 'E'): ('qkurungbody', 'E'),
        ('qkurungbody', 'KOMEN', 'F'): ('qkurungbody', 'F'),
        ('qkurungbody', 'KOMEN', 'G'): ('qkurungbody', 'G'),
        ('qkurungbody', 'KOMEN', 'H'): ('qkurungbody', 'H'),
        ('qkurungbody', 'KOMEN', 'I'): ('qkurungbody', 'I'),
        ('qkurungbody', 'KOMEN', 'J'): ('qkurungbody', 'J'),
        ('qkurungbody', 'KOMEN', 'K'): ('qkurungbody', 'K'),
        ('qkurungbody', 'KOMEN', 'L'): ('qkurungbody', 'L'),
        ('qkurungbody', 'KOMEN', 'M'): ('qkurungbody', 'M'),
        ('qkurungbody', 'KOMEN', 'N'): ('qkurungbody', 'N'),
        ('qkurungbody', 'KOMEN', 'O'): ('qkurungbody', 'O'),
        ('qkurungbody', 'KOMEN', 'P'): ('qkurungbody', 'P'),
        ('qkurungbody', 'KOMEN', 'Q'): ('qkurungbody', 'Q'),
        ('qkurungbody', 'KOMEN', 'R'): ('qkurungbody', 'R'),
        ('qkurungbody', 'KOMEN', 'S'): ('qkurungbody', 'S'),
        ('qkurungbody', 'KOMEN', 'T'): ('qkurungbody', 'T'),
        ('qkurungbody', 'KOMEN', 'U'): ('qkurungbody', 'U'),
        ('qkurungbody', 'KOMEN', 'V'): ('qkurungbody', 'V'),
        ('qkurungbody', 'KOMEN', 'W'): ('qkurungbody', 'W'),
        ('qkurungbody', 'KOMEN', 'X'): ('qkurungbody', 'X'),
        ('qkurungbody', 'KOMEN', 'Y'): ('qkurungbody', 'Y'),

        ('qkurunghead', 'KOMEN', 'A'): ('qkurunghead', 'A'),
        ('qkurunghead', 'KOMEN', 'D'): ('qkurunghead', 'D'),
        ('qkurunghead', 'KOMEN', 'E'): ('qkurunghead', 'E'),
        ('qkurunghead', 'KOMEN', 'M'): ('qkurunghead', 'M'),
        ('qkurunghead', 'KOMEN', 'O'): ('qkurunghead', 'O'),
        ('qkurunghead', 'KOMEN', 'P'): ('qkurunghead', 'P'),
        ('qkurunghead', 'KOMEN', 'Q'): ('qkurunghead', 'Q'),
        ('qkurunghead', 'KOMEN', 'R'): ('qkurunghead', 'R'),

        ('qkurung', 'KOMEN', 'A'): ('qkurung', 'A'),
        ('qkurung', 'KOMEN', 'Z'): ('qkurung', 'Z'),
        


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
    # print(token)
            
   
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

import os

class FileHandler:

    def __init__(self):
        pass

    def readFile(self, filePath):
        lines=[]
        if(os.path.isfile(filePath)):
            try:
                with open(filePath) as file:
                    lines = [line.rstrip() for line in file]
            except IOError as e:
                print("File tidak dapat dibuka.")
                exit(0)
        else:
            print('{} :File tidak ditemukan.'.format(filePath))
            exit(0)
        return lines

    def parseFile(self,lines):
        ''' Line 1: Total States
            Line 2: Input Word Symbols
            Line 3: Stack Symbols
            Line 4: Starting State
            Line 5: Starting Stack
            Line 6: Accepting States
            Line 7: Accept By
            Line 8: List of production
                    (current state, read from word, take from stack, next state, add to stack)
            '''
        states = lines[0].rstrip().split()
        input_symbols = lines[1].rstrip().split()
        stack_symbols = lines[2].rstrip().split()
        starting_state = lines[3].rstrip().split()
        starting_stack = lines[4].rstrip().split()
        accepting_states = lines[5].rstrip().split()
        accept_by = lines[6].rstrip().split()
        productions = lines[7:]
        for i in range(len(productions)):
            productions[i] = productions[i].rstrip().split()

        parsedLines = {'states':states,
                        'input_symbols':input_symbols,
                        'stack_symbols':stack_symbols,
                        'starting_state':starting_state,
                        'starting_stack':starting_stack,
                        'accepting_states':accepting_states,
                        'accept_by':accept_by,
                        'productions':productions}
        return parsedLines

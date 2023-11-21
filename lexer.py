import os
import sys
import re

def lex(text, token_rules):
    pos = 0
    line = 1
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1

        flag = None
        for current_token in token_rules:
            pattern, tag = current_token

            regex = re.compile(pattern)
            flag = regex.match(text,pos)

            if flag:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not flag:
            print("SYNTAX ERROR !!!")
            print(f'Error Expression at line {line}: {text[pos:].splitlines()[0]}')
            sys.exit(1)
        else:
            pos = flag.end(0)

    return tokens

token_rules = [

    # Not Token
    (r'[ \t]+', None),
    (r'//.*', None),
    (r'/\*(.|\n)*?\*/', None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),

    # OPERATOR
    (r'===', 'EQUAL_OPERATOR'),
    (r'==', 'EQUAL_TO_OPERATOR'),
    (r'!==', 'NOT_EQUAL_OPERATOR'),
    (r'!=', 'NOT_EQUAL_TO_OPERATOR'),
    (r'&&', 'AND'),
    (r'\|\|', 'OR'),
    (r'!', 'NOT'),
    (r'\+=', 'SUMPLUS'),
    (r'\-=', 'SUMMIN'),
    (r'\/=', 'SUMDIV'),
    (r'\*=', 'SUMMULT'),
    (r'<=', 'LEQ'),
    (r'<', 'KURUNG_V_BUKA'),
    (r'>=', 'GEQ'),
    (r'>', 'KURUNG_V_TUTUP'),
    (r'=', 'ASSIGN'),
    (r'%', 'MODULO'),
    (r'\,', 'KOMA'),
    (r'\;', 'TITIK_KOMA'),
    (r'\:', 'TITIK_DUA'),
    (r'\{', 'KURUNG_KURAWAL_BUKA'),
    (r'\}', 'KURUNG_KURAWAL_TUTUP'),
    (r'\(', 'KURUNG_BUKA'),
    (r'\)', 'KURUNG_TUTUP'),
    (r'\[', 'OPEN_BRACKET'),
    (r'\]', 'CLOSE_BRACKET'),
    (r'\n', 'ENTER'),
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\/', 'GARIS_MIRING'),
    (r'\*', 'MULT'),
    (r'\.', 'DOT'),
    
    # Type
    (r'[0-9]*\.[0-9]+',  "INT"),
    (r'[0-9][0-9]+',     "INT"),
    (r'[0-9]',           "INT"),
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'\bconst\b',              "VAR"),
    (r'\bvar\b',                "VAR"),

    # KEYWORDS
    (r'\bhtml\b', 'HTML'),
    (r'\bbody\b', 'BODY'),
    (r'\bhead\b', 'HEAD'),
    (r'\btitle\b', 'TITLE'),
    (r'\blink\b', 'LINK'),
    (r'\bscript\b', 'SCRIPT'),
    (r'\bfh1\b', 'H1'),
    (r'\bh2\b', 'H2'),
    (r'\bh3\b', 'H3'),
    (r'\bh4\b', 'H4'),
    (r'\bh5\b', 'H5'),
    (r'\bfh6\b', 'H6'),
    (r'\bp\b', 'P'),
    (r'\babbr\b', 'ABBR'),
    (r'\bstrong\b', 'STRONG'),
    (r'\bsmall\b', 'SMALL'),
    (r'\bhr\b', 'HR'),
    (r'\bdiv\b', 'DIV'),
    (r'\ba\b', 'A'),
    (r'\bimg\b', 'IMG'),
    (r'\bbutton\b', 'BUTTON'),
    (r'\bform\b', 'FORM'),
    (r'\btable\b', 'TABLE'),
    (r'\btr\b', 'TR'),
    (r'\btd\b', 'TD'),
    (r'\bth\b', 'TH'),

    # Untuk Variabel
    (r'[A-Za-z_$][A-Za-z0-9_$]*', 'VAR'),
]

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()

    tokens = lex(characters, token_rules)
    tokenResult = []

    for token in tokens:
        tokenResult.append(token)

    #Write file
    path = os.getcwd()
    fileWrite = open(path + "./tokenResult.txt", 'w')
    for token in tokenResult:
        fileWrite.write(str(token)+" \n")
        print(token)
    fileWrite.close()

    return tokenResult

createToken('tes.html')
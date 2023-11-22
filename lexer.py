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
    (r'>=', 'GEQ'),
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
    (r'<html>', 'HTML_OPEN'),
    (r'</html>', 'HTML_CLOSE'),
    (r'<body>', 'BODY_OPEN'),
    (r'</body>', 'BODY_CLOSE'),
    (r'<head>', 'HEAD_OPEN'),
    (r'</head>', 'HEAD_CLOSE'),
    (r'<title>', 'TITLE_OPEN'),
    (r'</title>', 'TITLE_CLOSE'),
    (r'<link>', 'LINK_OPEN'),
    (r'<script>', 'SCRIPT_OPEN'),
    (r'</script>', 'SCRIPT_CLOSE'),
    (r'<h1>', 'H1_OPEN'),
    (r'</h1>', 'H1_CLOSE'),
    (r'<h2>', 'H2_OPEN'),
    (r'</h2>', 'H2_CLOSE'),
    (r'<h3>', 'H3_OPEN'),
    (r'</h3>', 'H3_CLOSE'),
    (r'<h4>', 'H4_OPEN'),
    (r'</h4>', 'H4_CLOSE'),
    (r'<h5>', 'H5_OPEN'),
    (r'</h5>', 'H5_CLOSE'),
    (r'<h6>', 'H6_OPEN'),
    (r'</h6>', 'H6_CLOSE'),
    (r'<p>', 'P_OPEN'),
    (r'</p>', 'P_CLOSE'),
    (r'<abbr>', 'ABBR_OPEN'),
    (r'</abbr>', 'ABBR_CLOSE'),
    (r'<strong>', 'STRONG_OPEN'),
    (r'</strong>', 'STRONG_CLOSE'),
    (r'<small>', 'SMALL_OPEN'),
    (r'</small>', 'SMALL_CLOSE'),
    (r'<hr>', 'HR_OPEN'),
    (r'</hr>', 'HR_CLOSE'),
    (r'<div>', 'DIV_OPEN'),
    (r'</div>', 'DIV_CLOSE'),
    (r'<a>', 'A_OPEN'),
    (r'</a>', 'A_CLOSE'),
    (r'<img>', 'IMG'),
    (r'</img>', 'IMG'),
    (r'<button>', 'BUTTON_OPEN'),
    (r'</button>', 'BUTTON_CLOSE'),
    (r'<form>', 'FORM_OPEN'),
    (r'</form>', 'FORM_CLOSE'),
    (r'<table>', 'TABLE_OPEN'),
    (r'</table>', 'TABLE_CLOSE'),
    (r'<tr>', 'TR_OPEN'),
    (r'</tr>', 'TR_CLOSE'),
    (r'<td>', 'TD_OPEN'),
    (r'</td>', 'TD_CLOSE'),
    (r'<th>', 'TH_OPEN'),
    (r'</th>', 'TH_CLOSE'),

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
        # print(token)
    fileWrite.close()

    return tokenResult

createToken('tes.html')
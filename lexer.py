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
            print("\033[91mSYNTAX ERROR !!!\033[0m")
            print(f'\033[93mError Expression at line {line}: {text[pos:].splitlines()[0]}\033[0m')
            sys.exit(1)
        else:
            pos = flag.end(0)

    return tokens

token_rules = [

    # Not Token
    (r'[\s]+', None),
    (r'\n', 'ENTER'),
    


    # KEYWORDS
    (r'<!--([\s\S]*?)-->', 'KOMEN'),
    (r'<html', 'HTML_OPEN'),
    (r'>', 'KURUNG_TUTUP'),
    (r'</html>', 'HTML_CLOSE'),
    (r'<body', 'BODY_OPEN'),
    (r'</body>', 'BODY_CLOSE'),
    (r'<head', 'HEAD_OPEN'),
    (r'</head>', 'HEAD_CLOSE'),
    (r'<title', 'TITLE_OPEN'),
    (r'</title>', 'TITLE_CLOSE'),
    (r'<link', 'LINK'),
    (r'<script', 'SCRIPT_OPEN'),
    (r'</script>', 'SCRIPT_CLOSE'),
    (r'<h1', 'H1_OPEN'),
    (r'</h1>', 'H1_CLOSE'),
    (r'<h2', 'H2_OPEN'),
    (r'</h2>', 'H2_CLOSE'),
    (r'<h3', 'H3_OPEN'),
    (r'</h3>', 'H3_CLOSE'),
    (r'<h4', 'H4_OPEN'),
    (r'</h4>', 'H4_CLOSE'),
    (r'<h5', 'H5_OPEN'),
    (r'</h5>', 'H5_CLOSE'),
    (r'<h6', 'H6_OPEN'),
    (r'</h6>', 'H6_CLOSE'),
    (r'<p', 'P_OPEN'),
    (r'</p>', 'P_CLOSE'),
    (r'<br', 'BR'),
    (r'<button', 'BUTTON_OPEN'),
    (r'</button>', 'BUTTON_CLOSE'),
    (r'<b', 'B_OPEN'),
    (r'</b>', 'B_CLOSE'),
    (r'<em', 'EM_OPEN'),
    (r'</em>', 'EM_CLOSE'),
    (r'<abbr', 'ABBR_OPEN'),
    (r'</abbr>', 'ABBR_CLOSE'),
    (r'<strong', 'STRONG_OPEN'),
    (r'</strong>', 'STRONG_CLOSE'),
    (r'<small', 'SMALL_OPEN'),
    (r'</small>', 'SMALL_CLOSE'),
    (r'<hr', 'HR'),
    (r'<div', 'DIV_OPEN'),
    (r'</div>', 'DIV_CLOSE'),
    (r'<a', 'A_OPEN'),
    (r'</a>', 'A_CLOSE'),
    (r'<img','IMG'),
    (r'<input', 'INPUT'),
    (r'<form', 'FORM_OPEN'),
    (r'</form>', 'FORM_CLOSE'),
    (r'<table', 'TABLE_OPEN'),
    (r'</table>', 'TABLE_CLOSE'),
    (r'<tr', 'TR_OPEN'),
    (r'</tr>', 'TR_CLOSE'),
    (r'<td', 'TD_OPEN'),
    (r'</td>', 'TD_CLOSE'),
    (r'<th', 'TH_OPEN'),
    (r'</th>', 'TH_CLOSE'),
    (r'\bid="([^"]+)"', 'ID'),
    (r'\bclass="([^"]+)"', 'CLASS'),
    (r'\bstyle="([^"]+)"', 'STYLE'),
    (r'\btype="(submit|reset|button)"', 'TYPE_BUTTON'),
    (r'\btype="(text|password|email|number|checkbox)"', 'TYPE_INPUT'),
    (r'\bhref="([^"]+)"', 'HREF'),
    (r'\brel="([^"]+)"', 'REL'),
    (r'\bsrc="([^"]+)"', 'SRC'),
    (r'\balt="([^"]+)"', 'ALT'),
    (r'\baction="([^"]+)"', 'ACTION'),
    (r'\bmethod="(GET|POST)"', 'METHOD'),


    #Untuk Variabel
    (r'[^<]+', 'VAR'),
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

    return tokenResult

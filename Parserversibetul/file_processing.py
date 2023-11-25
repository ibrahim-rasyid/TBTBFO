import re
import sys
from vocabulary import token_exp

def lexer(teks, token_exp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            # !!!! DEBUGGING TEST
            # print("match") 
            # print(match)
            ###########################
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            pattern = (r'[^\n]*')
            regex = re.compile(pattern)
            match = regex.match(teks, pos-1)
            print("Error in line " + str(line))
            print(match.group(0))
            # print("ILLEGAL CHARACTER")
            # print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)
    print("TOKEN : " + " ".join(tokenArray))
    return " ".join(tokenArray)

create_token("test/test.html")
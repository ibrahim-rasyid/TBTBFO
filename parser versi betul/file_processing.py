import re
import sys
from vocabulary import token_exp
import linecache

def lexer(filename,teks, token_exp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    tokens = []
    while pos < len(teks):
        match = None

        for t in token_exp:
            pattern, tag = t
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                # !!!! DEBUGGING TEST
                # print(match)
                # print(pattern , tag)
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            temp = pos
            while(teks[temp-1] != '\n'):
                temp -= 1
            line = teks[0:temp].count('\n') + 1
            linetext = linecache.getline(filename,line)
            print("Error in line " + str(line))
            print(linetext)
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(sentence,char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)
    print("TOKEN : " + " ".join(tokenArray))
    return " ".join(tokenArray)

# create_token("test.html")
# ATURAN MENULIS GRAMMAR:
# Head pertama akan menjadi Start Symbol
# Tidak mengandung Useless Production (tidak terdapat Variables yang tidak dapat diderivasi menjadi string dan tidak terdapat Productions yang tidak muncul pada derivasi string)
# Tidak mengandung Null Production (tidak terdapat Variables yang menghasilkan epsilon, kecuali pada Start Symbol)

def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
        head, body = baris.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))

        baris = file.readline()

    file.close()
    print("Grammar : " + str(cfg) + "\n")
    # print(cfg)
    return cfg

def is_terminal(string):
    list_of_terminal = [
        "HTML",
        "HTMLCLOSE",
        "HEAD",
        "HEADCLOSE",
        "BODY",
        "BODYCLOSE",
        "TITLE",
        "TITLECLOSE",
        "LINK" ,
        "LINKCLOSE",
        "SCRIPT" ,
        "SCRIPTCLOSE",
        "H1" ,
        "H1CLOSE",
        "H2" ,
        "H2CLOSE",
        "H3" ,
        "H3CLOSE",
        "H4" ,
        "H4CLOSE",
        "H5" ,
        "H5CLOSE",
        "H6" ,
        "H6CLOSE",
        "P" ,
        "PCLOSE",
        "EM" ,
        "EMCLOSE",
        "B" ,
        "BCLOSE",
        "ABBR" ,
        "ABBRCLOSE",
        "STRONG" ,
        "STRONGCLOSE",
        "SMALL" ,
        "SMALLCLOSE",
        "DIV" ,
        "DIVCLOSE",
        "A" ,
        "ACLOSE",
        "BUTTON" ,
        "BUTTONCLOSE",
        "FORM" ,
        "FORMCLOSE",
        "TABLE" ,
        "TABLECLOSE",
        "TR",
        "TRCLOSE",
        "TD",
        "TDCLOSE",
        "TH",
        "THCLOSE",
        "WORD",
        "LINK",
        "BR",
        "HR",
        "IMG",
        "INPUT",
    ]
    
    return string in list_of_terminal

def is_variables(string):
    return not is_terminal(string)

# def is_variables(string):
#     return len(string) > 0 and string[0].isupper()

# def is_terminal(string):
#     return not is_variables(string)
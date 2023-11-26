token_exp = [
    (r'(?<=>)[\n \t]*(([ \t]*[\w]+[^<]*[ \t]*)+(\n)*)+[\n \t]*(?=<)','TEXT'),
    (r'(?=<!--)((.)+)(?<=-->)', "COMMENT"), # KOMENTAR
    # (r'<', '<'), #KSKI
    (r'>', '>'), #KSKA
    
    # ATTRIBUTE GLOBAL
    (r'[\s]*(id="(.)*?")(\s)*',"ID"),
    (r"[\s]*(id='(.)*?')(\s)*","ID"),
    (r'[\s]*(style="(.)*?")(\s)*',"STYLE"),
    (r"[\s]*(style='(.)*?')(\s)*","STYLE"),
    (r'[\s]*(class="(.)*?")(\s)*',"CLASS"),
    (r"[\s]*(class='(.)*?')(\s)*","CLASS"),
    
    # ATTRIBUTE TAMBAHAN
    (r'[\s]*(rel="(.)*?")(\s)*',"REL"),
    (r"[\s]*(rel='(.)*?')(\s)*","REL"),
    (r'[\s]*(href="(.)*?")(\s)*',"HREF"),
    (r"[\s]*(href='(.)*?')(\s)*","HREF"),
    (r'[\s]*(src="(.)*?")(\s)*',"SRC"),
    (r"[\s]*(src='(.)*?')(\s)*","SRC"),
    (r'[\s]*(alt="(.)*?")(\s)*',"ALT"),
    (r"[\s]*(alt='(.)*?')(\s)*","ALT"),
    (r'[\s]*(type="(submit|reset|button)")(\s)*',"TYPEBUTTON"),
    (r"[\s]*(type='(submit|reset|button)')(\s)*","TYPEBUTTON"),
    (r'[\s]*(type="(text|password|email|number|checkbox)")(\s)*',"TYPEINPUT"),
    (r"[\s]*(type='(text|password|email|number|checkbox)')(\s)*","TYPEINPUT"),
    (r'[\s]*(action="(.)*?")(\s)*',"ACTION"),
    (r"[\s]*(action='(.)*?')(\s)*","ACTION"),
    (r'[\s]*(method="(GET|POST)")(\s)*',"METHOD"),
    (r"[\s]*(method='(GET|POST)')(\s)*","METHOD"),
    
    # HTML TAG
    (r'[\s]*(<html)(\s)*', "HTML"),
    (r'[\s]*(</html>)(\s)*', "HTMLCLOSE"),
    
    # HEAD TAG
    (r'[\s]*(<head)(\s)*', "HEAD"),
    (r'[\s]*(</head>)(\s)*', "HEADCLOSE"),
    
    # BODY TAG
    (r'[\s]*(<body)(\s)*', "BODY"),
    (r'[\s]*(</body>)(\s)*', "BODYCLOSE"),
    
    # TITLE TAG
    (r'[\s]*(<title)(\s)*', "TITLE"),
    (r'[\s]*(</title>)(\s)*', "TITLECLOSE"),
    
    # LINK TAG (Void)
    (r'[\s]*(<link)(\s)*', "LINK"),

    # SCRIPT TAG 
    (r'[\s]*(<script)(\s)*', "SCRIPT"),
    (r'[\s]*(</script>)(\s)*', "SCRIPTCLOSE"),
    
    # H1 TAG
    (r'[\s]*(<h1)(\s)*', "H1"),
    (r'[\s]*(</h1>)(\s)*', "H1CLOSE"),
    
    # H2 TAG
    (r'(?<=<)[\s]*(h2)(\s)*', "H2"),
    (r'(?<=<)[\s]*(/h2)(\s)*', "H2CLOSE"),
    
    # H3 TAG
    (r'(?<=<)[\s]*(h3)(\s)*', "H3"),
    (r'(?<=<)[\s]*(/h3)(\s)*', "H3CLOSE"),
    
    # H4 TAG
    (r'(?<=<)[\s]*(h4)(\s)*', "H4"),
    (r'(?<=<)[\s]*(/h4)(\s)*', "H4CLOSE"),
    
    # H5 TAG
    (r'(?<=<)[\s]*(h5)(\s)*', "H5"),
    (r'(?<=<)[\s]*(/h5)(\s)*', "H5CLOSE"),
    
    # H6 TAG
    (r'(?<=<)[\s]*(h6)(\s)*', "H6"),
    (r'(?<=<)[\s]*(/h6)(\s)*', "H6CLOSE"),
    
    # ABBR TAG
    (r'(?<=<)[\s]*(abbr)(\s)*', "ABBR"),
    (r'(?<=<)[\s]*(/abbr)(\s)*', "ABBRCLOSE"),
    
    # STRONG TAG
    (r'(?<=<)[\s]*(strong)(\s)*', "STRONG"),
    (r'(?<=<)[\s]*(/strong)(\s)*', "STRONGCLOSE"),
    
    # SMALL TAG
    (r'(?<=<)[\s]*(small)(\s)*', "SMALL"),
    (r'(?<=<)[\s]*(/small)(\s)*', "SMALLCLOSE"),
    
    # HR TAG (Void)
    (r'(?<=<)[\s]*(hr)(\s)*', "HR"),
    
    # DIV TAG
    (r'(?<=<)[\s]*(div)(\s)*', "DIV"),
    (r'(?<=<)[\s]*(/div)(\s)*', "DIVCLOSE"),
    
    # IMG TAG (Void)
    (r'(?<=<)[\s]*(img)(\s)*', "IMG"),
    
    # BUTTON TAG
    (r'(?<=<)[\s]*(button)(\s)*', "BUTTON"),
    (r'(?<=<)[\s]*(/button)(\s)*', "BUTTONCLOSE"),
    
    # FORM TAG
    (r'(?<=<)[\s]*(form)(\s)*', "FORM"),
    (r'(?<=<)[\s]*(/form)(\s)*', "FORMCLOSE"),
    
    # INPUT TAG(Void)
    (r'(?<=<)[\s]*(input)(\s)*', "INPUT"),
    
    # TABLE TAG
    (r'(?<=<)[\s]*(table)(\s)*', "TABLE"),
    (r'(?<=<)[\s]*(/table)(\s)*', "TABLECLOSE"),
    
    # TR TAG
    (r'(?<=<)[\s]*(tr)(\s)*', "TR"),
    (r'(?<=<)[\s]*(/tr)(\s)*', "TRCLOSE"),
    
    # TD TAG
    (r'(?<=<)[\s]*(td)(\s)*', "TD"),
    (r'(?<=<)[\s]*(/td)(\s)*', "TDCLOSE"),
    
    # TH TAG
    (r'(?<=<)[\s]*(th)(\s)*',"TH"),
    (r'(?<=<)[\s]*(/th)(\s)*', "THCLOSE"),
    
    # P TAG
    (r'(?<=<)[\s]*(p)(\s)*', "P"),
    (r'(?<=<)[\s]*(/p)(\s)*', "PCLOSE"),
    
    # BR TAG (Void)
    (r'(?<=<)[\s]*(br)(\s)*', "BR"),
    
    # EM TAG
    (r'(?<=<)[\s]*(em)(\s)*', "EM"),
    (r'(?<=<)[\s]*(/em)(\s)*', "EMCLOSE"),
    
    # B TAG
    (r'(?<=<)[\s]*(b)(\s)*', "B"),
    (r'(?<=<)[\s]*(/b)(\s)*', "BCLOSE"),
    
    # A TAG
    (r'(?<=<)[\s]*(a)(\s)*', "A"),
    (r'(?<=<)[\s]*(/a)(\s)*', "ACLOSE"),
    
    
    (r'\n', None), #NEWLINE
    (r'[ \t]+',None),# Whitespaces
    
    ]
# Cara Run Lexer(Tokenizer): 
## 1. uncomment pemanggilan create_token(<filename>) di baris paling bawah file_processing.py
## 2. run dengan command py file_processing.py

# Cara Run Parser(Verdict) : py parser_program <testfile>

## FEATURE
## UNFULFILLED
1. table nested (tr td th hierarchy) (QNA no 24)

## REJECTED TESTING
### Format : Feature -> Testerfile 
### Lokasi testerfile di folder REJECTED 
### TESTING
1. Tag html wajib ada -> nohtml.html
2. Dokumen harus diawali html -> startnonhtml.html
3. Tag head wajib ada -> nohead.html
4. Tag head harus didalam tag html -> headoutsidehtml.html
5. Tag head harus diatas body -> headbelowbody.html
6. Tag body wajib ada -> nobody.html
7. Tag body harus didalam tag html -> bodyoutsidehtml.html
8. Tag body harus dibawah tag head -> bodyabovehead.html
9. Tag title hanya boleh di dalam tag head -> titleinsidebody.html
10. Tag link harus punya atribut rel -> linknorel.html
11. Tag img harus punya atribut src -> imgnosrc.html
12. Tag button atribut submit dibatasi submit, reset dan button -> buttonsubmitnonsubmitresetbutton.html
13. Tag form atribut method dibatasi GET dan POST -> formmethodnongetpost.html
14. Tag input atribut type dibatasi text, password, email, number dan checkbox -> inputtypenontextpasswordemailnumbercheckbox.html
15. Tag title harus di dalam tag head -> titleinbody.html
16. Tag dalam head hanya title, link, dan script -> nonheadtaginhead.html

### FEATURE dari QNA
1. (fulfilled) QNA no 6 -> komen di dalam sebuah tag tidak valid 
ex: <html <!-- Ini komentar -->> (tidak valid)
2. (fulfilled) QNA no 17 -> head, body, html, div, table dan tr tidak menerima text diantara tag buka dan tutup 
ex : <head>abc</head> (tidak valid)
3. (fulfilled) QNA no 25 -> 
<a 

href=""
>
dianggap valid (linebreak  dan whitespace diabaikan dalam tag)
4. (fulfilled) QNA no 57 -> tanda petik satu dan dua di atribut dibedakan
ex: 
- id='fdaf" (tidak valid) 
- id='fafds'(valid)
- id="fadfsd" (valid)
5. (fulfilled) QNA no 29 -> nesting formatting element
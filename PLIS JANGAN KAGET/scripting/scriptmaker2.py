# mystring = """(r'(?<=<)(\s)*({s1})(\s)*({l1}=(\"[^"]*\")+?)?(\s)*({l2}=(\"[^"]*\")+?)?(\s)*({l3}=(\"[^"]*\")+?)?(\s)*(method=("(GET|POST)")+?)?(\s)*(?=>)', "{s2}"),"""
mystring1 = """(r'(?<=<)(\s)*({s1})(\s)*({l1}=(\"[^"]*\")+?)?(\s)*({l2}=(\"[^"]*\")+?)?(\s)*({l3}=(\"[^"]*\")+?)?(\s)*(type=("(text|password|email|number|checkbox)")+?)?(\s)*(?=>)', "{s2}"),"""
mystring2 = """(r'(?<=<)(\s)*({s1})(\s)*({l1}=(\"[^"]*\")+?)?(\s)*({l2}=(\"[^"]*\")+?)?(\s)*(type=("(text|password|email|number|checkbox)")+?)?(\s)*({l3}=(\"[^"]*\")+?)?(\s)*(?=>)', "{s2}"),"""
mystring3 = """(r'(?<=<)(\s)*({s1})(\s)*({l1}=(\"[^"]*\")+?)?(\s)*(type=("(text|password|email|number|checkbox)")+?)?(\s)*({l2}=(\"[^"]*\")+?)?(\s)*({l3}=(\"[^"]*\")+?)?(\s)*(?=>)', "{s2}"),"""
mystring4 = """(r'(?<=<)(\s)*({s1})(\s)*(type=("(text|password|email|number|checkbox)")+?)?(\s)*({l1}=(\"[^"]*\")+?)?(\s)*({l2}=(\"[^"]*\")+?)?(\s)*({l3}=(\"[^"]*\")+?)?(\s)*(?=>)', "{s2}"),"""


myList = ["input"]
myList2 = list(map(str.upper,myList))
listku = ["id","class","style"]
combination = [
    [0,1,2],
    [0,2,1],
    [1,0,2],
    [1,2,0],
    [2,0,1],
    [2,1,0],
]
# combination = [
#     [0,1,2,3],
#     [0,1,3,2],
#     [0,2,1,3],
#     [0,2,3,1],
#     [0,3,1,2],
#     [0,3,2,1],
#     [1,0,2,3],
#     [1,0,3,2],
#     [1,2,0,3],
#     [1,2,3,0],
#     [1,3,0,2],
#     [1,3,2,0],
#     [2,0,1,3],
#     [2,0,3,1],
#     [2,1,0,3],   
#     [2,1,3,0],
#     [2,3,0,1],
#     [2,3,1,0],
#     [3,0,1,2],
#     [3,0,2,1],
#     [3,1,0,2],
#     [3,1,2,0],
#     [3,2,0,1],
#     [3,2,1,0],
#     ]

for i in range(0,len(myList)):
    for itemku in combination:
        print(mystring1.format(s1=myList[i], s2=myList2[i],l1=listku[itemku[0]],l2=listku[itemku[1]],l3=listku[itemku[2]]))
        
for i in range(0,len(myList)):
    for itemku in combination:
        print(mystring2.format(s1=myList[i], s2=myList2[i],l1=listku[itemku[0]],l2=listku[itemku[1]],l3=listku[itemku[2]]))
        
for i in range(0,len(myList)):
    for itemku in combination:
        print(mystring3.format(s1=myList[i], s2=myList2[i],l1=listku[itemku[0]],l2=listku[itemku[1]],l3=listku[itemku[2]]))
        
for i in range(0,len(myList)):
    for itemku in combination:
        print(mystring4.format(s1=myList[i], s2=myList2[i],l1=listku[itemku[0]],l2=listku[itemku[1]],l3=listku[itemku[2]]))
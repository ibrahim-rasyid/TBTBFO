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
                print("File could not be opened.")
                exit(0)
        else:
            print('{} :File was not found in the specified path.'.format(filePath))
            exit(0)
        return lines

    def parseFile(self,lines):
        ''' Line 1: Total States
            Line 2: Input Word Symbols
            Line 3: Stack Symbols
            Line 4: Initial State Symbol
            Line 5: Initial Stack Symbol
            Line 6: List of Final States
            Line 7 and onwards: Productions in form of
                    (Current State, Current Input Symbol, Current Top of Stack, Next State, Push/Pop Operation Symbol)
            '''
        states = lines[0].rstrip().split()
        input_symbols = lines[1].rstrip().split()
        stack_symbols = lines[2].rstrip().split()
        initial_state = lines[3].rstrip().split()[0]
        initial_stack = lines[4][0]
        final_states = lines[5].rstrip().split()
        productions = lines[6:]
        for i in range(len(productions)):
            productionku = productions[i].rstrip().split()                
            productions[i] = [productionku[0], productionku[1], productionku[2], productionku[3],[productionku[4:]]]
        print("List index hapus")
        listindexhapus = []
        for i in range(0,len(productions)):
            production = productions[i]
            for j in range(i+1,len(productions)):
                production2 = productions[j]
                if(production[0] == production2[0] and production[1] == production2[1] and production[2] == production2[2] and production2[4][0] not in production[4]):
                    print(production[4])
                    print(production2[4])
                    listindexhapus.append(j)
                    production[4].append(production2[4][0])
        print(listindexhapus)
        listindexhapus = list(dict.fromkeys(listindexhapus))
        print(productions)
        for item in sorted(listindexhapus, reverse = True): 
            del productions[item]
        # print(productions)
        
        parsedLines = {'states':states,
                        'input_symbols':input_symbols,
                        'stack_symbols':stack_symbols,
                        'initial_state':initial_state,
                        'initial_stack':initial_stack,
                        'final_states':final_states,
                        'productions':productions}
        return parsedLines
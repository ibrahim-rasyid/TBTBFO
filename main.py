from FileHandler import FileHandler
import time
from file_processing import create_token
class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, ListToken, parsedLines):
        #Retrieve all information
        self.stack = []
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']
        ListToken.insert(0,'e')
        ListToken.append('e')

        currentStackSymbol = initStackSymbol
        currentState = initialState

        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, self.stack))
        for token in ListToken:
            #print('Current TOS', currentStackSymbol)
            for production in productions:
                stop = False
                print(token)
                print(" Production State : " + production[0])
                print(" Current State : " + currentState)
                print(" Production Token : " + production[1])
                print(" Current Token : " + token)
                print(" Production Stack Symbol : " + production[2])
                print(" Current Stack Symbol : " + currentStackSymbol)
                print((production[0] == currentState) and (production[1] == token) and (production[2] == currentStackSymbol))
                if ((production[0] == currentState) and (production[1] == token) and (production[2] == currentStackSymbol)):
                    print(production[0])
                    print(production[1])
                    print(production[2])
                    print(production[3])
                    print(production[4])
                    currentState = production[3]
                    self.stack.pop()
                    stop = False
                    production[4].reverse()
                    for symbol in production[4]:
                        if(symbol != 'e'):
                            self.stack.append(symbol)
                    stop = True
                    break
                if stop:
                    break
            if(len(self.stack) - 1 >= 0):
                currentStackSymbol = self.stack[len(self.stack)-1]
            else:
                currentStackSymbol = production[4][0]
            previousStackSymbol = currentStackSymbol
            print('{}\t {}\t {}\t ({}, {})'.format(currentState, token, previousStackSymbol, currentStackSymbol, self.stack))
            time.sleep(0.5)

        if(currentState in finalStates):
            print('String accepted by PDA.')
        else:
            print('String rejected by PDA.')

def main():
    fh = FileHandler()
    pda = PDA()
    automataFilePath = input('Enter the automata file path: ')
    lines = fh.readFile('PDA/' + automataFilePath)
    # print(lines)
    print('Reading Automata File')
    print('Loading Details from Automata File: ')
    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Initial State: ', parsedLines['initial_state'])
    print('Initial Stack Symbol: ', parsedLines['initial_stack'])
    print('Final States: ', parsedLines['final_states'])
    print('Productions List:')
    for production in parsedLines['productions']:
        print('\t', production)
    print('Automata File Successfully Read')
    testFilePath = input('Enter test file path (or end): ')
    ListToken = create_token('TestFile/' + testFilePath)
    print('Reading string from file...')
    print('String successfully read')
    print(ListToken)
    print('Computing the Transition Table:')
    pda.compute(ListToken, parsedLines)

main()
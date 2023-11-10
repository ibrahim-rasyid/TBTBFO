from FileHandler import FileHandler
import time

class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, inputString, parsedLines):
        #Retrieve all information
        self.stack = []
        inputString += 'e'
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        currentStackSymbol = initStackSymbol
        currentState = initialState

        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, self.stack))
        for char in inputString:
            #print('Current TOS', currentStackSymbol)
            for production in productions:
                if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                    currentState = production[3]
                    if(len(production[4]) == 2):
                        self.stack.append(char)
                    elif(len(production[4]) == 3):
                        self.stack.append(char)
                        self.stack.append(char)
                    elif ((production[4] == 'e') and (len(self.stack) != 1)):
                        self.stack.pop()
                        break
            previousStackSymbol = currentStackSymbol
            currentStackSymbol = self.stack[len(self.stack)-1]
            print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, currentStackSymbol, self.stack))
            time.sleep(2)

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
    time.sleep(2)
    print('Loading Details from Automata File: ')
    time.sleep(3)
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
    time.sleep(2)
    print('Automata File Successfully Read')
    time.sleep(2)
    testFilePath = input('Enter test file path (or end): ')
    while testFilePath != "end":
        testString = ""
        testStringLines = fh.readFile('TestFile/' + testFilePath)
        for line in testStringLines:
            testString += line
        print('Reading string from file...')
        time.sleep(2)
        print('String successfully read')
        print('Computing the Transition Table:')
        pda.compute(testString, parsedLines)
        testFilePath = input('Enter test file path (or end): ')

main()
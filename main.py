from FileHandler import FileHandler
import time
from file_processing import create_token

class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, ListToken, parsedLines):
        # Retrieve all information
        self.stack = []
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        productions = parsedLines['productions']
        ListToken.insert(0, 'e')
        ListToken.append('e')

        currentStackSymbol = initStackSymbol
        currentState = initialState

        print('State\tInput\tStack\tMove')
        print('{}\t{}\t{}\t({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, self.stack))

        for token in ListToken:
            stop = False
            for production in productions:
                if (
                    production[0] == currentState
                    and production[1] == token
                    and production[2] == currentStackSymbol
                ):
                    print('{}\t{}\t{}\t({}, {})'.format(currentState, token, production[4], production[3], self.stack))
                    currentState = production[3]
                    self.stack.pop()

                    # Push symbols onto the stack in reverse order
                    for symbol in reversed(production[4]):
                        if symbol != 'e':
                            self.stack.append(symbol)

                    stop = True
                    break

            if stop:
                time.sleep(0.5)
                continue

            if len(self.stack) - 1 >= 0:
                currentStackSymbol = self.stack[len(self.stack) - 1]
            else:
                currentStackSymbol = 'Z'

            print('{}\t{}\t{}\t({}, {})'.format(currentState, token, currentStackSymbol, currentState, self.stack))
            time.sleep(0.5)

        if currentState in finalStates:
            print('String accepted by PDA.')
        else:
            print('String rejected by PDA.')

def main():
    fh = FileHandler()
    pda = PDA()
    automataFilePath = input('Enter the automata file path: ')
    lines = fh.readFile('PDA/' + automataFilePath)
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


if __name__ == "__main__":
    main()

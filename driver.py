from lexer import *
from parser import *
from interpreter import *

def main():
    while True:
        text = input('enter text> ')
        # print(str(text))
        lexerObject = Lexer(text)
        parserObject = Parser(lexerObject)
        ast = parserObject.parse()
        interpreterObject = Interpreter()
        # print(ast.op.type)
        result = interpreterObject.postorder(ast)
        print(result)
if __name__ == '__main__':
    main()
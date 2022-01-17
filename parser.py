from lexer import *
from num import *
from binop import *
from enum import *

INTEGER, PLUS, MUL, MOD, DIV, EOF = ('INTEGER', 'PLUS', 'MUL', 'MOD', 'DIV', 'EOF')


class Parser(object):
    def __init__(self, lexer):
        # print("initializing parser.py")
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    #def error(self):
     #   raise Exception('Invalid syntax')

    def getNextToken(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """basic unit factor : INTEGER """
        token = self.current_token
        if token.type == INTEGER:
            self.getNextToken(INTEGER)
            return Num(token)

    def term(self):
        """term : do multiplication - * """
        node = self.factor()
        while self.current_token.type in (MUL, MOD, DIV):
            token = self.current_token
            if token.type == MUL:
                self.getNextToken(MUL)
            if token.type == MOD:
                self.getNextToken(MOD)
            if token.type == DIV:
                self.getNextToken(DIV)
            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term (PLUS term)*
        term   : factor (MUL term)*
        factor : INTEGER
        """
        node = self.term()
        #print("node val " + str(node.value))

        while self.current_token.type in (PLUS):
            token = self.current_token
            if token.type == PLUS:
                self.getNextToken(PLUS)

            node = BinOp(left=node, op=token, right=self.term())

        #print(left.value)
        #print(right.value)

        return node

    def parse(self):
        xyz=self.expr()
        abc = xyz.op.value if type(xyz) is BinOp else xyz.value
        left = xyz.left.op.value if type(xyz.left) is BinOp else xyz.left.value
        right = xyz.right.op.value if type(xyz.right) is BinOp else xyz.right.value
        # print(abc)
        # print(left)
        # print(right)
        return xyz
    
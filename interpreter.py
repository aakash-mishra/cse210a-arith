from binop import *
from num import *
from enum import *

class Interpreter(object):
    
    def postorder(self, node):
        if type(node) is Num:
            return node.value
        elif type(node) is BinOp:
            if node.op.type == PLUS:
                return (self.postorder(node.left) + self.postorder(node.right))
            elif node.op.type == MUL:
                return (self.postorder(node.left) * self.postorder(node.right))
            elif node.op.type == MOD:
                return (self.postorder(node.left) % self.postorder(node.right))
            elif node.op.type == DIV:
                left = self.postorder(node.left)
                right = self.postorder(node.right)
                if right == 0:
                    print("cant divide by 0")
                return left / right
                

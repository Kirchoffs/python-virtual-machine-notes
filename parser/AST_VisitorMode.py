import sys
import tokenize

class TokenIterator:
    def __init__(self, itr):
        self.__itr = itr
        self.__cur = None
    
    def next(self):
        if self.has_next():
            ret = self.__cur
            self.__cur = None
            return ret
        return None
    
    def peek(self):
        if self.has_next():
            return self.__cur
        return None

    def has_next(self):
        if self.__cur is not None:
            return True
        
        toknum, tokvalue, _, _, _ = next(self.__itr, None)
        self.__cur = Token(toknum, tokvalue) if toknum is not None and tokvalue is not None else None
        if self.__cur is None:
            return False
        return True


class Token:
    def __init__(self, toknum, tokvalue):
        self.toknum = toknum
        self.tokvalue = tokvalue
    
    def __str__(self):
        return "{0}: {1}".format(self.toknum, self.tokvalue)


class BinaryOpNode:
    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def accept(self, visitor):
        visitor.visitBinaryOp(self)


class ConstNode:
    def __init__(self, value):
        self.value = value
    
    def accept(self, visitor):
        visitor.visitConst(self)


class PrintVisitor:
    def visitBinaryOp(self, bin_node):
        bin_node.left.accept(self)
        bin_node.right.accept(self)

        if bin_node.op == BinaryOpNode.ADD:
            print(" ADD")
        elif bin_node.op == BinaryOpNode.SUB:
            print(" SUB")
        elif bin_node.op == BinaryOpNode.MUL:
            print(" MUL")
        elif bin_node.op == BinaryOpNode.DIV:
            print(" DIV")
    
    def visitConst(self, const_node):
        print(const_node.value)


class ASTBuilder:
    @classmethod
    def buildAST(cls, tokens_itr):
        itr = TokenIterator(tokens_itr)
        return cls.__expr(itr)

    @classmethod
    def __expr(cls, itr):
        node = cls.__term(itr)

        toknum = itr.peek().toknum
        tokvalue = itr.peek().tokvalue
        
        while tokvalue == "+" or tokvalue == "-":
            itr.next()
            child = cls.__term(itr)

            if tokvalue == "+":
                node = BinaryOpNode(BinaryOpNode.ADD, node, child)
            else:
                node = BinaryOpNode(BinaryOpNode.SUB, node, child)

            toknum = itr.peek().toknum
            tokvalue = itr.peek().tokvalue
        
        return node
    
    @classmethod
    def __term(cls, itr):
        node = cls.__factor(itr)

        toknum = itr.peek().toknum
        tokvalue = itr.peek().tokvalue

        while tokvalue == "*" or tokvalue == "/":
            itr.next()
            child = cls.__factor(itr)

            if tokvalue == "*":
                node = BinaryOpNode(BinaryOpNode.MUL, node, child)
            else:
                node = BinaryOpNode(BinaryOpNode.DIV, node, child)
            
            toknum = itr.peek().toknum
            tokvalue = itr.peek().tokvalue
        
        return node
    

    @classmethod
    def __factor(cls, itr):
        current = itr.next()
        toknum = current.toknum
        tokvalue = current.tokvalue

        if toknum == tokenize.NUMBER:
            return ConstNode(tokvalue)
            
        elif tokvalue == "(":
            node = cls.__expr(itr)
            if itr.next().tokvalue != ")":
                raise Exception("Bad Expression")

            return node
        

if __name__ == "__main__":
    f = open(sys.argv[1])
    tk = tokenize.generate_tokens(f.readline)
    root = ASTBuilder.buildAST(tk)
    
    pv = PrintVisitor()
    root.accept(pv)
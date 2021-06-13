class ExprIterator:
    def __init__(self, expr):
        self.__itr = iter(expr)
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
        
        self.__cur = next(self.__itr, None)
        if self.__cur is None:
            return False
        return True


class Calculator:
    def calculate(self, expr):
        itr = ExprIterator(expr)
        return self.__expr(itr)
    
    def __expr(self, itr):
        val = self.__term(itr)
        
        symbol = itr.peek()
        while symbol == "+" or symbol == "-":
            itr.next()
            next_val = self.__term(itr)
            if symbol == "+":
                val += next_val
            elif symbol == "-":
                val -= next_val
            symbol = itr.peek()
        
        return val
    
    def __term(self, itr):
        val = self.__factor(itr)

        symbol = itr.peek()
        while symbol == "*" or symbol == "/":
            itr.next()
            next_val = self.__factor(itr)
            if symbol == "*":
                val *= next_val
            elif symbol == "/":
                val //= next_val
            symbol = itr.peek()
        
        return val
    
    def __factor(self, itr):
        val = itr.next()
        if val.isdigit():
            return int(val)
        elif val == "(":
            val = self.__expr(itr)
            if itr.next() != ")":
                raise Exception("Bad Expression")
            return val
        

def test_ExprIterator():
    tokens = ["1", "+", "3", "*", "5", "-", "4", "/", "4"]
    
    itr = ExprIterator(tokens)
    assert itr.peek() == "1"
    assert itr.next() == "1"
    itr.next()
    assert itr.next() == "3"
    assert itr.peek() == "*"
    assert itr.peek() == "*"
    itr.next()
    assert itr.peek() == "5"
    assert itr.peek() == "5"
    assert itr.next() == "5"
    assert itr.next() == "-"

    print("success")


def test_Calculator():
    calculator = Calculator()

    tokens = ["12", "+", "2", "-", "(", "3", "+", "5", ")", "*", "2"]
    res = calculator.calculate(tokens)
    assert res == -2, "The answer should be {0}, not {1}".format(-2, res)

    tokens = ["10", "/", "2", "-", "(", "3", "+", "5", ")", "*", "2", "-", "(", "2", "-", "8", "*", "4", ")", "*", "2"]
    res = calculator.calculate(tokens)
    assert res == 49, "The answer should be {0}, not {1}".format(49, res)

    tokens = ["1", "-", "6", "+", "2"]
    res = calculator.calculate(tokens)
    assert res == -3, "The answer should be {0}, not {1}".format(-3, res)

if __name__ == "__main__":
    # test_ExprIterator()
    test_Calculator()
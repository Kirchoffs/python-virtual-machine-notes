import sys
import tokenize

class Token:
    def __init__(self, tok_num, tok_value):
        self.toknum = tok_num
        self.tokvalue = tok_value
    
global current_token

def current():
    global current_token
    return current_token

def next(tk):
    toknum, tokvalue, _, _, _ = tk.next()
    global current_token
    current_token = Token(toknum, tokvalue)

def expr(tk):
    s1 = term(tk)
    toknum = current().toknum
    tokvalue = current().tokvalue

    value = s1
    while tokvalue == "+" or tokvalue == "-":
        print "expr tokvalue is %s" % tokvalue
        next(tk)

        s2 = term(tk)

        if tokvalue == "+":
            value += s2
        elif tokvalue == "-":
            value -= s2
        
        toknum = current().toknum
        tokvalue = current().tokvalue

    print "expr value is %s" % value
    return value

def term(tk):
    f1 = factor(tk)
    toknum = current().toknum
    tokvalue = current().tokvalue

    value = f1

    while tokvalue == "*" or tokvalue == "/":
        print "term tokvalue is %s" % tokvalue
        next(tk)

        f2 = factor(tk)

        if tokvalue == "*":
            value *= f2
            print "term value is %s" % value
        elif tokvalue == "/":
            value /= f2
            print "term value is %s" % value
        
        toknum = current().toknum
        tokvalue = current().tokvalue
    
    print "term return is %s" % value
    return value

def factor(tk):
    if current().toknum == tokenize.NUMBER:
        value = current().tokvalue
        next(tk)
    elif current().value == "(":
        next(tk)
        f = expr(tk)
        if current().tokvalue != ")":
            print "parser error! value=%s" % current().tokvalue
        value = f
        next(tk)
    return int(value)

if __name__ == "__main__":
    f = open(sys.argv[1])
    tk = tokenize.generate_tokens(f.readline)
    next(tk)
    print expr(tk)
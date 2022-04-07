from . import predicateInterpreter as pi

def complexPredicate(node,complexPredicate):
    lexer = pi.Lexer(complexPredicate)
    tokens = lexer.generate_tokens()
    parser = pi.Parser(tokens)
    tree = parser.parse()
    interpreter = pi.Interpreter(node)
    result = interpreter.visit(tree)
    return result.judge

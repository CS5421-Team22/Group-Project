from enum import Enum
from dataclasses import dataclass

# Lexer
class TokenType(Enum):
    CLAUSE = 0
    LPAREN = 1
    RPAREN = 2
    AND = 3
    OR = 4


@dataclass
class Token:
    type: TokenType
    value: any = None
    
    def __repr__(self):
        return self.type.name + (f"({self.value})" if self.value != None else "")


import re
WHITESPACE = ' \n\t'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
    
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    
    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)            
            else:
                temp = self.generate_expre()
                for tmp in temp:
                    if tmp == "and":
                        yield Token(TokenType.AND)
                    elif tmp == "or":
                        yield Token(TokenType.OR)
                    else:
                        yield Token(TokenType.CLAUSE, tmp)
                
                
    def generate_expre(self):
        expre = self.current_char
        self.advance()
        
        while self.current_char != None and not(self.current_char in "()"):
            expre += self.current_char
            self.advance()
            
        expre = re.split("(and)",expre)
        
        tmp = []
        for e in expre:
            e = re.split("(or)",e)
            tmp.extend(e)        
        expre = [ e.strip() for e in tmp]
        expre = [ e for e in expre if e ]

        return expre


# Parser
@dataclass
class ClauseNode:
    value: str
        
    def __repr__(self):
        return f"{self.value}"

@dataclass
class AndNode:
    node_a: any
    node_b: any
    
    def __repr__(self):
        return f"({self.node_a} and {self.node_b})"

@dataclass
class OrNode:
    node_a: any
    node_b: any
    
    def __repr__(self):
        return f"({self.node_a} or {self.node_b})"


class Parser:
    def __init__(self, tokens ):
        self.tokens = iter(tokens)
        self.advance()

        
    def raise_error(self):
        raise Exception("Invalid syntax")
        
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    
    def parse(self):
        if self.current_token == None:
            return None
        
        result = self.andOr()
        
        if self.current_token != None:
            self.raise_error()
        
        return result
    
    def andOr(self):
        result = self.clause()
        
        while self.current_token != None and self.current_token.type in [TokenType.AND, TokenType.OR]:
                if self.current_token.type == TokenType.AND:
                    self.advance()
                    result = AndNode(result,self.clause())
                else:
                    self.advance()
                    result = OrNode(result,self.clause())

        
        return result
    
    def clause(self):
        token = self.current_token
        
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.andOr()
            
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            
            self.advance()
            return result
        if token.type == TokenType.CLAUSE:
            self.advance()
            return ClauseNode(token.value)
                
        self.raise_error()


# Interpreter 
@dataclass
class Clause:
    value: str
    judge: bool
        
    def __repr__(self):
        return f"{self.value} is {self.judge}"

class Interpreter:
    
    def __init__(self,dataTreeNode):
        self.dataTreeNode = dataTreeNode
    
    def visit(self,node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self,method_name)
        return method(node)
    
    def visit_ClauseNode(self, node):
        return Clause(node.value, singlePredicate(self.dataTreeNode,node.value) )
    
    def visit_AndNode(self,node):
        return Clause(f'( {node.node_a} and {node.node_b})',bool(self.visit(node.node_a).judge and self.visit(node.node_b).judge))
    
    def visit_OrNode(self,node):
        return Clause(f'( {node.node_a} or {node.node_b})',bool(self.visit(node.node_a).judge or self.visit(node.node_b).judge))

    def visit_NoneType(self,node):
        return Clause("None",False)


# singlePredicate
def singlePredicate(node, predicate):

    # node is None
    if node is None:
        return False
    # predicate is white space
    if len(predicate.strip()) < 1:
        return True

    
    # todo: Circumstance 1: position

    # Circumstance 2: evaluate value
    # identify operator
    doubleOperators = ['>=', '<=', '!=']
    singleOperators = ['>', '<', '=']
    operatorIndex = -1
    operator = ''
    cmpVal = ''
    existDoubleOperator = False
    
    for op in doubleOperators:   
        if op in predicate:
            existDoubleOperator = True
            operator = op
            cmpVal = predicate[predicate.index(op) + 2 : ].strip()
            break
    if not existDoubleOperator:       
        for op in singleOperators:   
            if op in predicate:
                operator = op
                cmpVal = predicate[predicate.index(op) + 1 : ].strip()
                break       
            
#     compare values / operands
    selfVal = str(node.getValue())
    if selfVal.isnumeric():
        if not cmpVal.isnumeric():
            return False
        else:
            cmpVal = float(cmpVal)
            selfVal = float(selfVal)
            
    if operator == '>':
        return selfVal > cmpVal
    elif operator == '<':
        return selfVal < cmpVal
    elif operator == '=':
        return selfVal == cmpVal
    elif operator == '>=':
        return selfVal >= cmpVal
    elif operator == '<=':
        return selfVal <= cmpVal
    elif operator == '!=':
        return selfVal != cmpVal
    return False

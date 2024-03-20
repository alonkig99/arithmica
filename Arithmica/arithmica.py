from consts import *
from nodes import *
from Token import *


# this module includes the following classes: Dict, Parser, Lexer, Interpreter
class Dict:
    def __init__(self):
        self.dict = {}

    def get(self, name):
        value = self.dict.get(name, None)
        return value

    def set(self, var_name, value):
        self.dict[var_name] = value

    def remove(self, name):
        del self.dict[name]


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def make_identifier(self):
        id_str = ''

        while self.current_char is not None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance()

        tok_type = T_KEYWORD if id_str in KEYWORDS else T_IDENTIFIER
        return Token(tok_type, id_str)

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in "-+" and self.text[self.pos + 1] in DIGITS:
                sign = self.current_char
                num_str = sign + ''
                self.advance()
                while self.current_char is not None and self.current_char.isdigit():
                    num_str += self.current_char
                    self.advance()
                tokens.append(Token(T_INT, int(num_str), sign))
            elif self.current_char in DIGITS:
                # If the current character is a digit, tokenize a multi-digit number
                num_str = ''
                while self.current_char is not None and self.current_char.isdigit():
                    num_str += self.current_char
                    self.advance()
                tokens.append(Token(T_INT, int(num_str)))
            elif self.current_char == '+':
                tokens.append(Token(T_PLUS))
                self.advance()
                if self.current_char not in ' \t':
                    raise Exception("Invalid syntax: Space expected after '+' operator")
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
                # self.advance()
            elif self.current_char == '-':
                tokens.append(Token(T_MINUS))
                self.advance()
                if self.current_char not in ' \t':
                    raise Exception("Invalid syntax: Space expected after '-' operator")
            elif self.current_char == '*':
                tokens.append(Token(T_MUL))
                self.advance()
                if self.current_char not in ' \t':
                    raise Exception("Invalid syntax: Space expected after '*' operator")
            elif self.current_char == '/':
                tokens.append(Token(T_DIV))
                self.advance()
                if self.current_char not in ' \t':
                    raise Exception("Invalid syntax: Space expected after '/' operator")
            elif self.current_char == '=':  # MAKE either = or ==
                tokens.append(self.make_equals())
            elif self.current_char == '<':
                tokens.append(Token(T_LT))
                self.advance()
            elif self.current_char == '>':
                tokens.append(Token(T_GT))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(T_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(T_RPAREN))
                self.advance()

            else:
                # Handle unrecognized characters or syntax errors
                raise Exception("Invalid syntax: Unrecognized character")

        return tokens

    def make_equals(self):
        tok_type = T_ASSIGN
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = T_EQUALS

        return Token(tok_type)


class Interpreter:

    def eval_op(self, x, op, y):
        if op.type == T_PLUS:
            return x + y
        if op.type == T_MINUS:
            return x - y
        if op.type == T_MUL:
            return x * y
        if op.type == T_DIV:
            return x // y
        if op.type == T_EQUALS:
            return int(x == y)
        if op.type == T_GT:
            return int(x > y)
        if op.type == T_LT:
            return int(x < y)

    def evaluate_expr(self, e, varDict):
        if isinstance(e, NumberNode):
            res = e.val
            return res
        elif isinstance(e, int):
            return e
        elif isinstance(e, VarAssignNode):
            var_value = varDict.get(e.var_name_tok.value)
            if var_value is None:
                raise Exception(f"Variable '{e.var_name_tok}' is not defined")
            return var_value
        elif isinstance(e, VarAccessNode):
            var_value = varDict.get(e.var_name_tok)
            if var_value is None:
                raise Exception(f"Variable '{e.var_name_tok.value}' is not defined")
            return var_value
        elif isinstance(e, ComparisonNode):  # Handle comparison operations
            left_value = self.evaluate_expr(e.left_expr, varDict)
            right_value = self.evaluate_expr(e.right_expr, varDict)
            if e.op_tok.type == T_EQUALS:
                return int(left_value == right_value)
            elif e.op_tok.type == T_LT:
                return int(left_value < right_value)
            elif e.op_tok.type == T_GT:
                return int(left_value > right_value)
        elif isinstance(e, binOpNode):
            l = self.evaluate_expr(e.left_node, varDict)
            r = self.evaluate_expr(e.right_node, varDict)
            return self.eval_op(l, e.op_tok, r)

    def eval_assign(self, node, global_dict):
        var_name = node.var_name_tok.value
        value = self.evaluate_expr(node.expr,
                                   global_dict)  # Evaluate the expression on the right side of the assignment
        global_dict.set(var_name, value)  # Set the variable in the global dictionary
        return value  # Return the assigned value


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'


class Parser:
    def __init__(self, tokens):
        self.current_tok = None
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
            return self.current_tok

    def parse_operand(self):
        # Check the type of the current token
        if self.current_tok.type == T_INT:

            # If the token is an integer, parse it as a number
            operand = NumberNode(self.current_tok.value, self.current_tok.sign)
            self.advance()  # Consume the token
        elif self.current_tok.type == T_IDENTIFIER:
            # If the token is an identifier, parse it as a variable
            var_name = self.current_tok.value
            operand = VarAccessNode(var_name)

            self.advance()  # Consume the token
        else:
            # Handle syntax error: unexpected token for operand
            operand = None
            self.advance()

        return operand

    def parse_operator(self):
        # Check if the current token is an operator
        if self.current_tok.type in [T_PLUS, T_MINUS, T_MUL, T_DIV]:
            # Get the operator token
            op_tok = self.current_tok
            self.advance()  # Consume the operator token
            return op_tok

        # If the current token is not an operator, raise an error
        raise Exception("Expected an operator token")

    def parse_assignment(self):  # we know its VAR at the beginning
        self.advance()
        var_name = self.current_tok
        self.advance()
        if self.current_tok.type != T_ASSIGN:
            raise Exception("Invalid syntax")
        self.advance()
        expr = self.parse_expression()
        return VarAssignNode(var_name, expr)

    def parse_expression(self):
        if self.current_tok.type == T_LPAREN:
            # Consume the '(' token
            self.advance()

            # Parse the expression within the parentheses
            expr = self.parse_expression()

            # Ensure there is a closing ')' token
            if self.current_tok.type != T_RPAREN:
                raise Exception("Expected ')'")

            # Consume the ')' token
            self.advance()

            return expr

        elif self.current_tok.type in [T_PLUS, T_MINUS, T_MUL, T_DIV, T_LT, T_GT, T_EQUALS]:
            op_tok = self.current_tok
            self.advance()

            # Parse the left and right operands
            left_node = self.parse_expression()
            right_node = self.parse_expression()

            # Create a binary operation node
            return binOpNode(left_node, op_tok, right_node)

        # If the current token is a number or identifier, parse it as an operand
        return self.parse_operand()

    def parse(self):
        # Parse the expression
        if self.current_tok.matches(T_KEYWORD, 'VAR'):
            return self.parse_assignment()

        return self.parse_expression()
    #######################################
    # RUN
    #######################################


global_dict = Dict()


def run(text):
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
    print(tokens)

    parser = Parser(tokens)
    ast = parser.parse()  # Parsing the entire input

    interpreter = Interpreter()

    if isinstance(ast, VarAssignNode):
        interpreter.eval_assign(ast, global_dict)  # If it's a variable assignment, evaluate it

    result = interpreter.evaluate_expr(ast, global_dict)  # Evaluate the entire expression

    return result  # Return the result

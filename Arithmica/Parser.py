from consts import *
from nodes import *


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
            raise Exception("Invalid operand: Expected an integer or identifier")

        return operand


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

        elif self.current_tok.type in [T_PLUS, T_MINUS, T_MUL, T_LT, T_GT, T_EQUALS]:
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

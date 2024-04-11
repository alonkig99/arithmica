from Token import *
from consts import *


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

        while self.current_char is not None and self.current_char in LETTERS + '_':
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
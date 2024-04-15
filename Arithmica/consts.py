import string

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
T_INT = 'INT'
T_PLUS = 'PLUS'
T_MINUS = 'MINUS'
T_MUL = 'MUL'
T_IDENTIFIER = 'IDENTIFIER'
T_KEYWORD = 'KEYWORD'
T_ASSIGN = 'ASSIGN'  # =
T_EQUALS = 'EQUALS'  # ==
T_LT = 'LT'  # less than
T_GT = 'GT'  # Greater than
T_LPAREN = 'LPAREN'  # (
T_RPAREN = 'RPAREN'  # )
KEYWORDS = ['VAR']
MAX_VARS = 20
MAX_RES_VAL= 1000000000
MIN_RES_VAL= -1000000000
MAX_VAR_NAME_LEN = 10
#RESTRICTED_VAR_CHARS = ['(', ')', '=', '@', '#', '%', '^', '*', '-', '~', '+', '-', '>', '<', '/']

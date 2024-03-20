class binOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class NumberNode:
    def __init__(self, val, sign=None):
        self.val = val
        self.sign = sign

    def __repr__(self):
        return f'{self.val}'


class VarAssignNode:
    def __init__(self, var_name_tok, expr):
        self.var_name_tok = var_name_tok
        self.expr = expr


class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok


class VariableNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'VariableNode({self.name})'


class ComparisonNode:
    def __init__(self, left_expr, op_tok, right_expr):
        self.left_expr = left_expr
        self.op_tok = op_tok
        self.right_expr = right_expr

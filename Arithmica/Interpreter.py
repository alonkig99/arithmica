
from consts import *
from nodes import *


class Interpreter:

    def eval_op(self, x, op, y):
        if op.type == T_PLUS:
            return x + y
        if op.type == T_MINUS:
            return x - y
        if op.type == T_MUL:
            return x * y
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
                                   global_dict)
        # Evaluate the expression on the right side of the assignment
        if len(global_dict.dict) > MAX_VARS-1:
            print("Error: Variable not assigned, exceeded maximum number of variables!")
        else:
            global_dict.set(var_name, value)  # Set the variable in the global dictionary
        return value  # Return the assigned value


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'
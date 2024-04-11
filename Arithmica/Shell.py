from Dict import *
from Parser import *
from Lexer import *
from Interpreter import *
from nodes import *

global_dict = Dict()


def run(text):
    lexer = Lexer(text)

    tokens = lexer.make_tokens()
    #print(tokens)

    parser = Parser(tokens)
    ast = parser.parse()  # Parsing the entire input
    print(ast)
    interpreter = Interpreter()

    if isinstance(ast, VarAssignNode):
        interpreter.eval_assign(ast, global_dict)  # If it's a variable assignment, evaluate it and put result in the dict

    result = interpreter.evaluate_expr(ast, global_dict)  # Evaluate the entire expression

    return result  # Return the result


# print("Welcome To Arithmica Interpreter")
# while True:
#     user_input = input(">>> ").strip()
#     if user_input.lower() == 'exit':
#         break
#
#     try:
#         result = run(user_input)
#         print(result)
#     except Exception as e:
#         print("Error:", e)


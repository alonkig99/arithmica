  # Arithmica

Arithmica is an interpreter written in Python that supports calculation of prefix math expressions, variable assignments and boolean comparsions. 
It is a final project for "Progamming Languages" course in our Computer Science degree in college.




**Supported datatypes:**
* `Integer`

**Supported math operators:**
* `Multiplication  '*'`
* `Addition  '+'`
* `Substraction  '-'`

**Supported boolean operators:**
* `Greater than  '>'`
* `Less than '<'`
* `Equals  '=='`



**Variable assignment examples:**


```python

VAR a = 5
VAR b = - 33 4

```
**Boolean expression examples:**



input:
```
> a b
```
output:
```
```
meaning:\
is 'a' greater than 'b'?\
output:
```
```
input:
```
< 5 4
```
meaning:\
is 5 less than 4?\
input:
```
== (+ 4 5) (- 3 8)
```
output:
```
```
meaning:\
does 4 plus 5 equal 3 minus 8?


**Math expression examples**:


## How it works:
The program prompts the user for input. The input text is saved into a variable and then tokenized, parsed and interpreted:\
```python
lexer = Lexer(text)
tokens = lexer.make_tokens()
parser = Parser(tokens)
ast = parser.parse()  # Parsing the entire input
interpreter = Interpreter()

if isinstance(ast, VarAssignNode):
    interpreter.eval_assign(ast, global_dict)  # If it's a variable assignment, evaluate it and put result in the dict

result = interpreter.evaluate_expr(ast, global_dict)  # Evaluate the entire expression

```

Let's take the following input as an example:
```
+ * -34 4 9
```
The lexer object produces the following tokens:
```
[PLUS, MUL, INT:-:-34, INT:None:4, INT:None:9]
```

The parser object produces the following Abstract Syntax Tree(ast):
```
((-34, MUL, 4), PLUS, 9)
```
The interpeter object produces the following result:
```
-127
```

Variable assignments are stored in a dictonary data structure and can be later used in calculations:



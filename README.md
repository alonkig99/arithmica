Arithmica is a basic interpreter written in Python that supports calculation of prefix math expressions, variable assignments and boolean comparsions. 
It is a final project for "Progamming Languages" course in our Computer Science degree in college.

**How it works:**\
The program prompts the user for input. The input, whether it's a variable assignment, a math expression or a boolean expression, goes through the following process:\
Lexer- The Lexer processes raw input text, breaking it down into tokens with specific types and values.\
Parser-The Parser constructs a parse tree from tokens, ensuring they adhere to the language's syntax rules and producing a structured representation of the input.\
Interpeter-The Interpreter evaluates the parse tree produced by the Parser, executing actions or computations based on the input's meaning and context.



**Supported datatypes:**\
`Integer`

**Supported math operators:**\
`Multiplication  '*'`\
`Addition  '+'`\
`Substraction  '-'`

**Supported boolean operators:**\
`Greater than  '>'`\
`Less than '<'`\
`Equals  '=='`

to be continued...

Variable assignment:\



```
VAR x = 5
```

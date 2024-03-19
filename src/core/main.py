import re

# Expresiones regulares para cada token
tokens = [
    ('NUMBER', r'\d+(\.\d*)?'),       # Números
    ('STRING', r'".*?"'),             # Cadenas de texto
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Identificadores
    ('PLUS', r'\+'),                   # Suma
    ('MINUS', r'-'),                  # Resta
    ('TIMES', r'\*'),                 # Multiplicación
    ('DIVIDE', r'/'),                 # División
    ('LPAREN', r'\('),                # Paréntesis izquierdo
    ('RPAREN', r'\)'),                # Paréntesis derecho
    ('SEMICOLON', r';'),              # Punto y coma
    ('COMMA', r','),                  # Coma
    ('ASSIGN', r'='),                 # Asignación
    ('WHITESPACE', r'\s+'),           # Espacios en blanco
]

# Función para tokenizar el código fuente
def tokenize(code):
    tokens_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    token_regex = re.compile(tokens_regex)
    pos = 0
    while pos < len(code):
        match = token_regex.match(code, pos)
        if not match:
            raise SyntaxError('Invalid syntax at position %d: %s' % (pos, code[pos:pos+10]))
        token_type = match.lastgroup
        value = match.group(token_type)
        if token_type != 'WHITESPACE':
            yield (token_type, value)
        pos = match.end()

# Ejemplo de uso:
code = '''
  var x = 10 + 20;
  let c = "hola";
'''
for token in tokenize(code):
    print(token)
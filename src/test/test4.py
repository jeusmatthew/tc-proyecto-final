import re

# Definición de patrones de expresiones regulares para cada tipo de token
patterns = [
    (r'PROGRAMA', 'PROGRAMA'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'id'),  # Identificador
    (r'0x[0-9A-Fa-f]+', 'val'),  # Valor hexadecimal
    (r'\d+', 'val'),  # Valor decimal
    (r'LEE', 'LEE'),
    (r'REPITE', 'REPITE'),
    (r'VECES', 'VECES'),
    (r'FINREP', 'FINREP'),
    (r'IMPRIME', 'IMPRIME'),
    (r'"[^"]*"', 'txt'),  # Cadena de texto
    (r'[\+\-\*/]', 'op_ar'),  # Operadores aritméticos
    (r'\s+', None),  # Espacios en blanco
]

def lexer(code):
    tokens = []
    code = code.split('\n')  # Dividir el código en líneas
    for line in code:
        for pattern, token_type in patterns:
            match = re.match(pattern, line)
            if match:
                value = match.group()
                if token_type:
                    tokens.append((token_type, value))
                break
    return tokens

# Ejemplo de uso con el código proporcionado
code = """
PROGRAMA factorial
    VarX = 0x1
    VarY = 0x0
    LEE Num
    REPITE Num VECES
        VarY = VarY + 0x1
        VarX = VarX * VarY
    FINREP
    IMPRIME "Factorial de "
    IMPRIME Num
    IMPRIME " es "
    IMPRIME VarX
FINPROG
"""

tokens = lexer(code)

# Imprimir la salida de tokens
for token in tokens:
    print(token)

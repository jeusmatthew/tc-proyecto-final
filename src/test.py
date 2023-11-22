import re

# Definición de la gramática y patrones regulares
gramatica = {
    'PROGRAMA': r'PROGRAMA',
    'FINPROG': r'FINPROG',
    'id': r'[a-zA-Z][a-zA-Z0-9]*',
    'val': r'0[xX][0-9a-fA-F]+|\d+',
    'op_ar': r'[*+/-]',
    'op_rel': r'[=<>]',
    'LEE': r'LEE',
    'REPITE': r'REPITE',
    'VECES': r'VECES',
    'SI': r'SI',
    'ENTONCES': r'ENTONCES',
    'SINO': r'SINO',
    'FINSI': r'FINSI',
    'FINREP': r'FINREP',
    'IMPRIME': r'IMPRIME',
    'txt': r'"[^"]*"',
    'comentario': r'#.*',
    '=': r'=',
}

# Función para tokenizar el código fuente
def tokenizar(codigo_fuente):
    tokens = []
    for token, patron in gramatica.items():
        regex = re.compile(patron)
        match = regex.match(codigo_fuente)
        while match:
            valor = match.group()
            if token != 'comentario':
                tokens.append(f'{token} {valor}')
            codigo_fuente = codigo_fuente[match.end():].lstrip()
            match = regex.match(codigo_fuente)
    return tokens

# Código fuente de ejemplo
codigo_fuente = '''
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
'''

# Tokenizar el código fuente
tokens = tokenizar(codigo_fuente)

# Imprimir los tokens
for token in tokens:
    print(token)

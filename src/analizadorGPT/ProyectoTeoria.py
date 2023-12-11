import re

def is_valid_identifier(token):
    # Verifica si el token es un identificador válido
    return re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,15}$', token)

def is_valid_text_literal(token):
    # Verifica si el token es un literal de texto válido
    return re.match(r'^"[^"]*"$', token)

def is_valid_numeric_literal(token):
    # Verifica si el token es un literal numérico válido
    return re.match(r'^(0x[0-9A-Fa-f]+|\d+)$', token)

def lexical_analysis(input_code):
    # Palabras reservadas y operadores
    keywords = set(['PROGRAMA', 'FINPROG', 'SI', 'ENTONCES', 'SINO', 'FINSI', 'REPITE', 'VECES', 'FINREP', 'IMPRIME', 'LEE'])
    relational_operators = set(['>', '<', '=='])
    arithmetic_operators = set(['+', '-', '*', '/'])
    
    lines = input_code.split('\n')
    tokens = []

    for line_number, line in enumerate(lines, start=1):
        # Eliminar comentarios
        line = re.sub(r'#.*$', '', line)
        
        # Tokenizar la línea
        for token in re.findall(r'[A-Za-z0-9]+|"[^"]+"|==|>|<|=|[-+*/]', line):
            if token in keywords:
                tokens.append(('KEYWORD', token, line_number))
            elif token in relational_operators:
                tokens.append(('REL_OP', token[0], line_number))
            elif token in arithmetic_operators:
                tokens.append(('ARITH_OP', token, line_number))
            elif token == '=':
                tokens.append(('ASSIGNMENT', token, line_number))
            elif is_valid_identifier(token):
                tokens.append(('ID', token, line_number))
            elif is_valid_text_literal(token):
                tokens.append(('TEXT_LITERAL', token, line_number))
            elif is_valid_numeric_literal(token):
                tokens.append(('NUMERIC_LITERAL', token, line_number))
            else:
                print(f"Error en la línea {line_number}: Unidad léxica no válida '{token}'")

    with open('programa.lex', 'w') as lex_file:
        for token in tokens:
            lex_file.write(f"{token[0]}: {token[1]}, Línea {token[2]}\n")

    print("Análisis léxico completado.")

# Ejemplo de uso
input_code = """
# Programa que calcula el factorial de un número
PROGRAMA factorial
# VarX acumula los productos por iteración
VarX = 0x1
# VarY contiene el iterador del factor
VarY = 0x0
LEE Num
#  Aplica Num! = 1 * 2 * 3 * ... * Num
REPITE NumVECES
VarY = VarY + 0x1
VarX = VarX * VarY
FINREP
IMPRIME “Factorial de ”
IMPRIME Num
IMPRIME “ es “
IMPRIME VarX
FINPROG 
"""

lexical_analysis(input_code)
